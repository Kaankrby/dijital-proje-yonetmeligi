# Dijital Proje Yönetmeliği · Açık Mevzuat Kaynağı

**Mimarlık ve Mühendislik Projelerinin Dijital Olarak Hazırlanması Hakkında Yönetmelik** için topluluk tarafından geliştirilebilen Markdown metinleri, tablolar, SVG şekilleri ve kaynak izleri.

İnsanların okuması, katkı yapması ve yapay zekâ ajanlarının kaynak göstererek kullanması için hazırlanmıştır. Revit veya pyRevit kurulumu gerektirmez.

> Bu depo resmî yayın veya konsolide güncel mevzuat değildir. Ana metin arşivlenmiş yayımlanma nüshasının aktarımıdır. Ekler OCR içerir; bütün karakterler, tablolar ve hukuki anlamlar için **TEYİT BEKLİYOR**. Metinlerin bulunması bir yazılım kontrolünün uygulandığını ya da projenin mevzuata uygunluğunu göstermez.

## Belgeler

| Belge | İçerik |
| --- | --- |
| [Yönetmelik](yonetmelik.md) | Ana metin: 17 madde ve 2 geçici madde |
| [EK-1](ek-1.md) | Proje kodu belirleme |
| [EK-2](ek-2.md) | Dosya isimlendirme |
| [EK-3](ek-3.md) | Mahal isimlendirme |
| [EK-4](ek-4.md) | CAD ortamında çizim hazırlama |
| [EK-5](ek-5.md) | Sınıflar ve varlık isimlendirme |
| [EK-6](ek-6.md) | Öznitelikler ve özellikler |
| [EK-7](ek-7.md) | Proje öznitelikleri |
| [EK-8](ek-8.md) | Gelişim seviyesi |
| [EK-9](ek-9.md) | Kalite kontrol formları |

Ek aktarımı 241 kaynak sayfayı kapsar. Mevcut kaynak kaydı 176 numaralı tablo, bir tablosal şekil ve 9.614 hücre bildirir. Birleşik hücreler Markdown içindeki HTML tablolarında, çizimler [11 SVG dosyasında](figures/) korunur. Bu sayılar doğruluk veya eksiksiz hukuki anlam teyidi değildir.

## Kaynak ve güven düzeyi

Kaynak belgelerdeki yayın künyesi **Resmî Gazete, 05.08.2026 / 33331**, ana metnin alınma tarihi **01.11.2026** olarak kayıtlıdır:

- [Resmî ana metin adresi](https://www.resmigazete.gov.tr/eskiler/2026/08/20260805-2.htm) · [Arşivlenmiş HTML baytları](sources/20260805-2.htm.txt)
- [Resmî ek PDF adresi](https://www.resmigazete.gov.tr/eskiler/2026/08/20260805-2-1.pdf) · [Arşivlenmiş 241 sayfalık PDF](sources/20260805-2-1.pdf)
- [Kaynak, aktarım ve doğrulama durumu](SOURCES.md) · [Makinece okunabilir manifest](manifest.json)

Bağımsız deponun hazırlanması sırasında 01.11.2026 tarihinde resmî adreslere canlı erişim sağlanamadı. Yayın künyesi mevcut kaynak arşivinden aktarılmıştır; sonraki değişikliklerin bulunmadığı teyit edilmemiştir.

## pyRevit içinde okumak ve MCP ile kullanmak

[Parametrically Compass](https://github.com/Kaankrby/Parametrically-Compass), bu kaynakların sabitlenmiş bir kopyasını taşıyan bağımsız pyRevit eklentisidir. Revit içinde çevrimdışı okuma, Türkçe arama, tablo/şekil görünümü ve ajanlar için salt okunur MCP araçları sağlar. Kurulum ZIP'i, CLI komutu ve test edilen sürümler eklentinin deposunda açıklanır. Kaynak metin katkıları bu depoda geliştirilir; eklentiyle otomatik eşitleme yoktur.

## Ajanlar ve geliştiriciler

Önce [AGENTS.md](AGENTS.md) ve [SOURCES.md](SOURCES.md) okuyun. `yonetmelik.md` ve `ek-*.md` okunabilir metinlerdir. `sources/structured-annexes.json` sayfa, tablo, hücre koordinatları, OCR ve inceleme izlerini taşır; hukuki kural motoru değildir. JSON alanlarının açıklaması için [kaynak rehberine](SOURCES.md#makinece-okunabilir-dosyalar) bakın.

Alıntılarda dosya, madde veya tablo, kaynak PDF sayfası ve kullanılan commit kimliğini belirtin. `OCR_UNREVIEWED`, kısmi teyit ve `TEYİT BEKLİYOR` durumlarını sonuçlarınıza taşıyın. Kaynak metni, yorumunuzu ve yazılımda uygulanmış kontrolü ayrı ifade edin.

```sh
git clone https://github.com/Kaankrby/dijital-proje-yonetmeligi.git
cd dijital-proje-yonetmeligi
python scripts/verify.py
```

Python 3.10+ ve standart kütüphane yeterlidir. Kontrol, dosya bütünlüğünü, kaynak özetlerini, JSON yapısını ve yerel bağlantıları denetler; OCR veya hukuki doğruluğu teyit etmez.

## Katkı

Hataları [issue açarak](https://github.com/Kaankrby/dijital-proje-yonetmeligi/issues/new/choose) bildirebilir veya fork üzerinden pull request gönderebilirsiniz. Bir harf ya da kod düzeltmesi de değerlidir. Kaynak sayfa, tablo/hücre, önceki ve önerilen metin ile kanıtı ekleyin. Adımlar [CONTRIBUTING.md](CONTRIBUTING.md) içindedir.

Proje ilk olarak [Parametrically pyRevit](https://github.com/Kaankrby/14_PyRevit_Parametrically) içindeki mevzuat kitaplığından ayrılmıştır. İlk aktarımda ana metin, ekler, şekiller ve kaynak dosyaları baytları korunarak kopyalanmıştır. Bu depo kendi sürüm geçmişini izler; iki depo arasında otomatik eşitleme yoktur.

## Lisans

Özgün araçlar, rehberler ve katkılar [MIT](LICENSE) lisanslıdır. Resmî kaynak belgeler ve bunların aktarımları için kapsam ve kaynak ayrımı [NOTICES.md](NOTICES.md) içindedir. Atıf yapılan ISO/TSE ve diğer üçüncü taraf standartlarına ait tam metinler bu projenin lisansına dahil değildir.
