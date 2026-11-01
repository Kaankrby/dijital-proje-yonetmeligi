# Kaynaklar ve aktarım durumu

## Kaynak arşivi

| Dosya | Kaynak / açıklama |
| --- | --- |
| [Ana metin HTML](sources/20260805-2.htm.txt) | [Resmî URL](https://www.resmigazete.gov.tr/eskiler/2026/08/20260805-2.htm); dosya uzantısı `.txt` olsa da özgün HTML baytları korunur, UTF-8 varsayılmamalıdır |
| [Ek PDF](sources/20260805-2-1.pdf) | [Resmî URL](https://www.resmigazete.gov.tr/eskiler/2026/08/20260805-2-1.pdf); 241 kaynak sayfası |

Kaynak künyesi: Resmî Gazete 05.08.2026 / 33331. Ana metnin aktarım kaydındaki alınma tarihi: 01.11.2026. Bağımsız depo hazırlanırken resmî adreslere canlı erişim başarısız oldu; arşivin resmî sunucudaki güncel dosyayla eşitliği bu işlem sırasında yeniden doğrulanamadı.

Ek PDF SHA-256: `7dc88971d3a7a8ae837ef148169fa5bf6c9ce7a01cc8fcd560ae3d342bb0ecb3`.

Ana metin HTML SHA-256: `ac662505610e9a8b34ecc9116a04d0843992d5b95820eaba1b4c12e9679c2703`.

`manifest.json` her içerik dosyasının özetini, bayt boyutunu ve ilk aktarım kökenini kaydeder. Özet eşleşmesi yalnız dosya bütünlüğünü gösterir. PDF ve HTML arşiv özetleri kontrol aracında ayrıca sabittir.

## İlk aktarım

Kaynak proje: [Kaankrby/14_PyRevit_Parametrically](https://github.com/Kaankrby/14_PyRevit_Parametrically), `Parametrically.extension/lib/parametrically/data/standards/` çalışma klasörü, 01.11.2026.

Aktarılan yeni dosyalar kaynak projenin çalışma ağacında henüz commit edilmemişti. Bu nedenle kaynak deponun HEAD commit'i bu dosyaların köken commit'i olarak sunulmaz. Ana metin, EK-1–EK-9, `figures/` ve `sources/` ilk aktarımda baytları korunarak kopyalanmıştır. Başlangıç özetleri `provenance/initial-import.json` içinde sabit bir kayıt olarak bulunur. Ofis sözlükleri, pyRevit kodu ve üretilmiş okuyucu bu aktarımın kapsamında değildir.

## Makinece okunabilir dosyalar

- `sources/structured-annexes.json`: `schema_version`, `source_sha256`, `source_pages`, `pages`, `finalization` ve inceleme geçmişi içerir. `pages[].page` 1 tabanlı PDF sayfasıdır. `tables[].id` tablo parçasını tanımlar; `cells[]` hücre metni, sıfır tabanlı satır/sütun, `rowspan`, `colspan`, `bbox` ve OCR izlerini taşır. Koordinatlar ilgili kaynak PDF sayfasıyla birlikte kullanılmalıdır. Bir tablo birden fazla sayfa/parçaya yayılabilir; Markdown okuma metni parçaları birleştirir.
- `sources/ocr-provenance.json`: ilk 225 dpi Türkçe/İngilizce sayfa OCR geçmişidir. Güncel hücre çalışmasını tek başına temsil etmez.
- `sources/transcription-corrections.json`: önceki metin özetleri, kaynak sınırları, düzeltmeler ve inceleme gruplarıdır. `review_batches` sonraki teknik incelemeleri içerir. Bazı tarihsel `evidence` alanları yerel çalışma sırasında üretilmiş kırpım dosyalarının adıdır; bu kırpımlar bu depoda bulunmaz. Arşiv PDF ve hücre koordinatları yeniden karşılaştırma için kullanılır. Eksik kırpımları mevcut kanıt gibi sunmayın.
- `provenance/initial-import.json`: ilk aktarım dosyalarının değişmez boyut ve SHA-256 kayıtlarıdır.
- `manifest.json`: mevcut içerik dosyalarının güncellenebilir bütünlük dizinidir; OCR durumları ve kaynak bağlantılarını da içerir.

## İnceleme sınırları

Mevcut kaynak kaydı, 176 numaralı tablo, 246 tablo parçası, bir tablosal şekil ve toplam 9.614 hücre bildirir. İlk çalışma geçmişi 799 hücre için görsel teyit ve 13 hücre için kısmi teknik belirteç incelemesi kaydeder. Bunlar bu bağımsız depo hazırlanırken yeniden yapılmış incelemeler değildir. Bu sayıların kapsamı sınırlıdır; bütün metin, değer, koşul, birleşik hücre, şekil veya hukuki yorum için tam doğruluk iddiası yoktur.

Ana metin konsolide güncel nüsha olarak teyit edilmemiştir. Eklerin tümü için **TEYİT BEKLİYOR** durumu korunur. Kontrol aracı aktarım bütünlüğünü denetler; kaynak PDF'nin resmîliği, OCR doğruluğu ve proje uygunluğu hakkında karar vermez.
