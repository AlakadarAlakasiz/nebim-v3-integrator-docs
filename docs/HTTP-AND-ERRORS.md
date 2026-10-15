# Özgün Nebim V3 Entegratör — 238 model API rehberi

Referans sürüm **25.4.1.0**. Kodlar **1–238** eksiksiz kapsanır. **0 / None** işlem modeli olmayan sentinel’dır.

Bu paket yalnız özgün IIS üzerinde çalışan Nebim V3 Entegratör HTTP sözleşmesini belgeler. Bağımsız, resmi olmayan teknik referanstır. Örnekler kaynak/metadata şablonudur;238 başarılı canlı işlem yakalaması veya bütün iş kurallarını karşılayan istek garantisi değildir. Gövdeler önemli alanların alt kümesini gösterir; tam alan envanteri model tabloları ve TYPES.md içindedir. Bilinmeyen zorunluluklar, varsayılanlar, dinamik tipler ve prosedür kolonları uydurulmaz.

## Kullanım

- [Aranabilir çevrimdışı rehber](index.html), [tip sözlüğü](TYPES.md), [sözleşme verisi](contracts.json).
- [Postman koleksiyonu](Nebim-V3-238-model.postman_collection.json) ve [ortam dosyası](Nebim-V3.postman_environment.json) birlikte içe aktarılır.
- baseUrl özgün Entegratör adresidir; sanal IIS uygulama dizini varsa korunur. Varsayılan localhost:3019 yalnız örnektir.
- DatabaseName, UserGroupCode, UserName, Password ortamda doldurulur. Connect tokenını test betiği seçili ortama aktarır. Gerçek parola/token/sunucu IP’si veya müşteri verisi pakete gömülmez.
- Sayısal0/1, örnek tarihler ve GUID’ler varsayılan/iş kuralı iddiası değildir. Yer tutucuları geçerli tanım kodları ve gerçek işlem kimlikleriyle değiştirin.
- Post oluşturma/güncelleme; Delete, iptal, onay, dönüştürme ve ödeme işlemleri veri değiştirebilir. Paket hazırlanırken servis/SQL işlemi yapılmadı.

## Giriş ve HTTP

POST /IntegratorService/Connect doğrudan JSON alır. ModelType1, DatabaseName, UserGroupCode, UserName, Password, Validate:true kullanılır. DatabaseServer kuruluma göre eklenebilir. Nebim hesabı ile SQL hesabı farklıdır. Validate false/eksik ise özgün ayar ve auto-login akışına göre doğrulama ertelenebilir; token varlığını tek başına başarılı kimlik doğrulama saymayın.

Content-Type: application/json; charset=utf-8. {"model":...} zarfı veya /api/ öneki yoktur. URL tokenı JWT/Bearer değildir. Cookie/session kurulumları farklılaşabilir. GET/PUT binder davranışı POST ile aynı değildir; gövdeli örnekler POST kullanır.

Başarı evrensel data zarfına sahip değildir: entity, dizi, JSON string, null veya özel işlem nesnesi olabilir. Hata bazı yollarda HTTP200 ile gelebilir; ExceptionMessage, Exception ve gövdedeki StatusCode birlikte denetlenir. Generic null scalar yanıt alanı atlanabilir; yokluk, null,0,false eşit sayılmamalıdır. Enum/model sayısal, decimal JSON sayı, GUID metindir. ISO tarih istekleri ve özgün /Date(milisaniye)/ yanıtları ayrı ele alınır.

GetModel yazılabilir iş anahtarlarıyla Load çağırır; yazılabilir anahtar yoksa normal setter yolunu kullanır. Her modele aynı HeaderID/Code atanmaz. NewModel yalnız {"ModelType":N} döndürür; tam şablon değildir. Koleksiyondan bir satırı çıkarmak silme talebi değildir; kaynak generic IsDeleted akışı ve modelin silme kuralları geçerlidir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

## Hatalar

Özgün global hata zarfının örnek biçimi:

```json
{"ModelType":0,"ExceptionMessage":"HATA_METNI","StackTrace":"","ErrorSource":"NebimV3IntegratorService","StatusCode":400}
```

StackTrace Base64 UTF-8 olabilir; InnerException iç içe gelebilir. Hassas SQL, parola, token ve müşteri gövdelerini loga taşımayın. Aşağıdaki sınıflar bütün lisans/iş doğrulama hatalarının eksiksiz kataloğu değildir. Temsili mesajlar gerçek yerelleştirilmiş hata metni olarak sunulmaz. HTTP durumu, gövdedeki StatusCode ve endpoint ayrımı korunur.

| Hata | Örnek durum | Açıklama | İstemci davranışı |
|---|---|---|---|
| Giriş bilgileri doğrulanamadı | 400 | Kullanıcı grubu, Nebim kullanıcısı/parolası veya veritabanı erişimi doğrulanamadı. HTTP durumuyla birlikte gövdedeki StatusCode kontrol edilir. | Nebim hesabını ve DatabaseName bilgisini doğrulayın; SQL hesabı/parolasını kullanıcı girişiyle karıştırmayın. |
| Geçersiz / süresi dolmuş oturum | Değişken | URL tokenı geçersiz, kaldırılmış veya oturum süresi dolmuş olabilir. invalid token mesajı da görülebilir. | Connect ile oturum oluşturun; tokenı URL segmentinde gönderin. Belirsiz bir yazmayı otomatik tekrar göndermeyin. |
| Model / alan / iş kuralı reddi | 400 | Yanlış ModelType, controller/model uyuşmazlığı, alan türü, eksik anahtar, bloke kod veya iş doğrulaması isteği reddedebilir. Mesaj temsili olup bütün modellerin gerçek hata metni değildir. | Modelin somut tipini, endpointini ve kurulumdaki referans kodlarını kontrol edin. |
| Kayıt bulunamadı | 400 | İstenen iş anahtarıyla kayıt yüklenemedi. Yerelleştirilmiş metinde tablo ve anahtar bulunabilir; metin burada temsili gösterilir. | Doğru yazılabilir anahtar veya modelin belge numarası yoluyla okuyun; her modele aynı HeaderID/Code alanını göndermeyin. |
| SQL ilişki / kayıt doğrulama hatası | 400 | Olmayan referans, ilişki kısıtı veya iş doğrulaması kaydı engelleyebilir. Birden çok hata && ile birleşebilir; Message/Detail JSON metni içerebilir. | İlgili tanım kodlarını ve iş anahtarlarını kontrol edin. JSON Detail içindeki && nedeniyle yalnız metin bölmeyle kesin hata sayısı çıkarmayın. |
| Gövde / binder sorunu | Değişken | Özgün binder geçersiz JSON’u boş modele çevirebilir; görünen eksik ModelType hatasının asıl nedeni bozuk gövde olabilir. | Doğrudan JSON ve UTF-8 application/json kullanın. GET/PUT binder davranışını standart POST gibi varsaymayın. |
| Kuyruk anahtarı çakışması | 409 | Idempotent-Key daha önce request/response kuyruğunda bulunmuş olabilir. Yanıt düz metin olabilir; ilk başarı otomatik tekrar döndürülmez. | Queue/Read veya iş anahtarıyla ilk işlemi kontrol edin; farklı anahtarla körlemesine tekrar yazmayın. |
| Asenkron istek kabulü | 202 | Call-Type:Async ve kuyruk anahtarıyla kabul yanıtı, iş kaydının tamamlandığını kanıtlamaz. Worker akışı bu sözleşme incelemesinde sertifikalanmamıştır. | Kuyruk sonucunu izleyin;202 yanıtını kayıt başarı yanıtı olarak işlemeyin. |
| Kuyruk kaydı bulunamadı | 404 | Queue/Read için request/response dosyası bulunamamış olabilir. Bu evrensel entity GetModel hata kodu değildir. | Doğru kuyruk anahtarını ve işlem durumunu kontrol edin. |

