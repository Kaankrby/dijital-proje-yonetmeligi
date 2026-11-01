# Katkı rehberi

Türkçe veya İngilizce issue ve pull request açabilirsiniz. Kaynak metinler Türkçe korunur.

## Hata bildirme

1. Belgeyi, maddeyi veya tablo/hücreyi belirtin.
2. Arşiv PDF'sindeki 1'den başlayan sayfa numarasını ekleyin. Ana metin için arşiv HTML paragrafını veya maddeyi kullanın.
3. Mevcut ve önerilen metni yazın. Kaynak görüntüsü veya resmî bağlantıyla destekleyin.
4. Düzeltmenin OCR, tablo yapısı, kaynak güncellemesi veya yorum önerisi olduğunu açıklayın.

Kişisel proje, müşteri veya başvuru bilgisi paylaşmayın. İnceleme kanıtı veremiyorsanız kaydı `TEYİT BEKLİYOR` olarak bırakın.

## Pull request

1. Depoyu fork edin ve değişikliğiniz için bir dal açın.
2. Değişikliği küçük tutun; özgün resmî arşiv dosyalarını değiştirmeyin.
3. Markdown düzeltmesinin karşılığı teknik JSON'da varsa ilgili kaydı da inceleyin. Kaynak izini ve eski düzeltmeleri koruyun. Uygun kayda bağlanamıyorsanız önce issue açın.
4. Yeni aktarım incelemelerini `sources/community-reviews.json` dosyasının `reviews` listesine ekleyebilirsiniz. Dosya ilk katkıda `{"schema_version": 1, "reviews": []}` biçiminde oluşturulur. Kayıtta belge, sayfa, tablo/hücre veya madde, önceki/sonraki metin, kanıt bağlantısı ve inceleme durumu bulunsun. Bu kayıt eski OCR inceleme geçmişini değiştirmez.
5. İçerik değişikliklerinin özetlerini yenileyin ve kontrol edin:

```sh
python scripts/verify.py --update-manifest
python scripts/verify.py
git diff --check
```

6. Pull request açıklamasına kaynak kanıtını ve kontrol sonucunu yazın. Özetleri yenilemek, değişikliğin doğruluğunu kanıtlamaz; inceleyen kişinin kaynağı karşılaştırması gerekir.

GitHub Actions aynı bütünlük kontrolünü çalıştırır. Tablo/hücre bütünlüğü veya OCR yeniden üretimi bu kontrolün kapsamı değildir. İlk kaynak üretim hattı bu depoya henüz taşınmamıştır.

## Güncel mevzuat değişiklikleri

Değişiklik yayınının resmî URL'sini, tarih/sayısını ve etkilediği maddeleri ekleyin. Eski yayım nüshasını sessizce güncellemeyin; önce sürümleme yaklaşımını issue üzerinden tartışın. Bir mevzuat yorumunu kaynak metin içine yerleştirmeyin.

## Lisans ve iletişim

Özgün katkılarınızı MIT lisansıyla sunun; üçüncü taraf içeriklerde kaynağı ve kullanım koşullarını belirtin. Resmî metinlerin kapsamı NOTICES.md içindedir. Saygılı ve kanıta dayalı tartışın; teknik itirazları kişiselleştirmeyin.
