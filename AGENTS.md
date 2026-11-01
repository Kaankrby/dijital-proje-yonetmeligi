# Ajanlar için çalışma talimatları

Bu depo kaynak metin ve kaynak izleri barındırır. Revit modeli, doğrulanmış hukuki kural motoru veya ruhsat onay sistemi değildir.

## Okuma ve yanıt üretme

- Önce README.md, SOURCES.md ve manifest.json içindeki durumları okuyun.
- `yonetmelik.md` yayımlanma nüshasıdır; yürürlükteki konsolide metin olduğunu varsaymayın. Tarihe bağlı cevaplarda resmî değişiklikleri ayrıca araştırın.
- Eklerde OCR hataları bulunabilir. `OCR_UNREVIEWED`, kısmi teknik belirteç teyidi ve `TEYİT BEKLİYOR` etiketlerini kaldırmayın veya tam teyide dönüştürmeyin.
- Alıntıya belge adı, madde/tablo, mümkünse PDF sayfası ve commit kimliğini ekleyin. Kaynak PDF sayfası, PDF içindeki 1'den başlayan sıra numarasıdır.
- Kaynakta bulunmayan değerleri, kodları ve zorunlulukları üretmeyin. Eksik veya çelişkili bilgiyi açıkça belirtin.
- Kaynak hükmünü, yorum/inferansı ve yazılımda uygulanmış kontrolü ayrı ifade edin. Bir metnin bulunması uygunluk testi yapıldığı anlamına gelmez.
- HTML tablolarındaki `rowspan`/`colspan` ilişkilerini koruyun. Düz satır bölerek sütun eşleştirmesi yapmayın.

## Değişiklik yapma

- Arşivlenmiş `sources/20260805-2-1.pdf` ve `sources/20260805-2.htm.txt` dosyalarını değiştirmeyin. Yeni yayınlar ayrı dosya ve açık tarih/sürüm bilgisiyle eklenmelidir.
- Toplu yeniden OCR veya otomatik yazım düzeltmesiyle incelenmiş kayıtların üzerine yazmayın.
- Düzeltmelerde kaynak sayfa ve hücre sınırı, önceki metin, önerilen metin ve inceleme kanıtını kaydedin; CONTRIBUTING.md yolunu izleyin.
- Kaynak dosyalardaki eski düzeltme geçmişini silmeyin. Yeni kayıtları ekleyin; kanıtınız yoksa inceleme durumunu yükseltmeyin.
- Teknik JSON ve Markdown birlikte değişiyorsa eşleşmelerini kaynaktan kontrol edin. Bu depoda OCR/Markdown üretim hattı henüz taşınmış değildir; eksik üretim kanıtını tamamlanmış gibi sunmayın.
- Katkıdan sonra `python scripts/verify.py` çalıştırın. Beklenen içerik değiştiyse `python scripts/verify.py --update-manifest` ile özetleri yenileyin ve diff'i inceleyin. Bu komut resmî arşivleri değiştirmeye izin vermez.
- Geçen bütünlük kontrolünü OCR doğruluğu, güncellik veya hukuki uygunluk kanıtı olarak sunmayın.
- Kişisel/ofis verileri, lisanslı standart tam metinleri veya erişim anahtarları eklemeyin.
