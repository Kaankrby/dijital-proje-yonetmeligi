"""Offline integrity checks; no claim of legal or OCR accuracy. Python 3.10+."""

import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
ARCHIVES = {
    "sources/20260805-2-1.pdf":
        "7dc88971d3a7a8ae837ef148169fa5bf6c9ce7a01cc8fcd560ae3d342bb0ecb3",
    "sources/20260805-2.htm.txt":
        "ac662505610e9a8b34ecc9116a04d0843992d5b95820eaba1b4c12e9679c2703",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def record(path):
    raw = path.read_bytes()
    return {"sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}


def content_files():
    paths = [ROOT / "yonetmelik.md"]
    paths.extend(ROOT / f"ek-{number}.md" for number in range(1, 10))
    for folder in ("sources", "figures"):
        paths.extend(p for p in (ROOT / folder).rglob("*") if p.is_file())
    return {p.relative_to(ROOT).as_posix(): record(p) for p in sorted(paths)}


class Markup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.tables = 0
        self.cells = 0

    def handle_starttag(self, tag, attrs):
        self.tables += tag == "table"
        self.cells += tag in ("td", "th")
        self.links.extend(value for name, value in attrs
                          if name in ("href", "src") and value)


def check_links(path, links):
    for link in links:
        url = urlsplit(link)
        if url.scheme or url.netloc or not url.path:
            continue
        target = (path.parent / unquote(url.path)).resolve()
        require(target.is_relative_to(ROOT), f"Link outside repository: {path.name}: {link}")
        require(target.exists(), f"Missing local link: {path.name}: {link}")


def verify(update_manifest=False):
    for name, digest in ARCHIVES.items():
        require(record(ROOT / name)["sha256"] == digest,
                f"Original archive changed: {name}")
    require((ROOT / "sources/20260805-2-1.pdf").read_bytes().startswith(b"%PDF-"),
            "Invalid PDF signature")

    for path in (ROOT / "sources").glob("*.json"):
        load_json(path)
    structured = load_json(ROOT / "sources/structured-annexes.json")
    corrections = load_json(ROOT / "sources/transcription-corrections.json")
    ocr = load_json(ROOT / "sources/ocr-provenance.json")
    for name, data in (("structured", structured), ("corrections", corrections), ("OCR", ocr)):
        require(data["source_sha256"] == ARCHIVES["sources/20260805-2-1.pdf"],
                f"Source hash mismatch in {name}")
    pages = structured["pages"]
    require(structured["source_pages"] == len(pages) == 241,
            "Expected all 241 source pages")
    require([p["page"] for p in pages] == list(range(1, 242)),
            "Missing, duplicate or unordered source pages")
    require(structured["finalization"]["corrections_sha256"] ==
            record(ROOT / "sources/transcription-corrections.json")["sha256"],
            "Corrections and structured data are out of sync")

    main = (ROOT / "yonetmelik.md").read_text(encoding="utf-8")
    require(re.findall(r"^## MADDE (\d+)\s*$", main, re.M) ==
            [str(i) for i in range(1, 18)], "Expected articles 1 through 17")
    require(len(re.findall(r"^## GEÇİCİ MADDE \d+", main, re.M)) == 2,
            "Expected two temporary articles")
    tables = cells = 0
    for number in range(1, 10):
        path = ROOT / f"ek-{number}.md"
        text = path.read_text(encoding="utf-8")
        require(text.startswith(f"# EK-{number}"), f"Annex heading mismatch: {path.name}")
        require("TEYİT BEKLİYOR" in text, f"Review warning missing: {path.name}")
        markup = Markup()
        markup.feed(text)
        tables += markup.tables
        cells += markup.cells
    summary = structured["finalization"]
    require(tables == summary["numbered_tables"] + summary["tabular_figures"],
            f"Markdown table count mismatch: {tables}")
    require(cells == summary["cells"], f"Markdown cell count mismatch: {cells}")

    for path in ROOT.rglob("*.md"):
        if ".git" in path.relative_to(ROOT).parts:
            continue
        text = path.read_text(encoding="utf-8")
        markup = Markup()
        markup.feed(text)
        links = re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", text)
        check_links(path, links + markup.links)
    for path in (ROOT / "figures").glob("*.svg"):
        require(ET.parse(path).getroot().tag.endswith("svg"), f"Invalid SVG: {path.name}")

    baseline = load_json(ROOT / "provenance/initial-import.json")
    manifest_path = ROOT / "manifest.json"
    manifest = load_json(manifest_path)
    require(baseline["files"], "Initial import record is empty")
    for name, digest in ARCHIVES.items():
        require(baseline["files"][name]["sha256"] == digest,
                f"Initial archive record changed: {name}")
    require(manifest["initial_import_sha256"] ==
            record(ROOT / "provenance/initial-import.json")["sha256"],
            "Initial import record changed; preserve historical provenance")
    current = content_files()
    if update_manifest:
        manifest["files"] = current
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
                                 encoding="utf-8", newline="\n")
        print("Updated content hashes. Review the diff and source evidence before committing.")
    require(manifest["files"] == current,
            "Content differs from manifest; inspect changes before --update-manifest")
    print(f"PASS: {len(current)} content files; 241 source pages; "
          f"17 + 2 articles; {tables} tables; {cells} cells; local links and SVG XML.")
    print("Integrity only. OCR, current legal status and compliance remain unverified.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--update-manifest", action="store_true",
                        help="Refresh editable content hashes after reviewing source changes")
    args = parser.parse_args()
    try:
        verify(args.update_manifest)
    except (ValueError, KeyError, OSError, ET.ParseError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
