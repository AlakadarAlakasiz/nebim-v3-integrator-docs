[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-47"></a>

## 47 — DiscountPoint / İndirim puanı

İndirim puanı için İndirim ve kampanya grubundaki model. Somut factory tipi NebimV3.DiscountOffers.IntegratorDiscountPoint. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.DiscountOffers.IntegratorDiscountPoint`. Grup: İndirim ve kampanya. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 47,
  "CustomerCode": "{{CustomerCode}}",
  "Description": "ÖRNEK Description",
  "AvailablePoint": 0,
  "CustomerTypeCode": 0,
  "DiscountPointID": "{{exampleGuid}}",
  "DiscountPointTypeCode": "{{DiscountPointTypeCode}}"
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 47,
  "CustomerCode": "{{CustomerCode}}",
  "Description": "ÖRNEK Description",
  "AvailablePoint": 0,
  "CustomerTypeCode": 0,
  "DiscountPointID": "{{exampleGuid}}",
  "DiscountPointTypeCode": "{{DiscountPointTypeCode}}"
}
```

### Okuma / silme / şablon

GetModel için güvenilir yazılabilir anahtar adayı çıkarılamadı; uydurma HeaderID/Code gönderilmez.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=47` → `{"ModelType":47}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| AvailablePoint | `System.Decimal` | true | true | — | — | Scalar |
| CustomerCode | `System.String` | true | true | — | — | Scalar |
| CustomerTypeCode | `System.Byte` | true | true | — | — | Scalar |
| Description | `System.String` | true | true | — | — | Scalar |
| DiscountPointID | `System.Guid` | true | true | — | — | Scalar |
| DiscountPointTypeCode | `System.String` | true | true | — | — | Scalar |
| FirstValidDate | `System.DateTime` | true | true | — | — | Scalar |
| LastValidDate | `System.DateTime` | true | true | — | — | Scalar |
| OrderHeaderID | `System.Guid` | true | true | — | — | Scalar |
| PendingPoint | `System.Decimal` | true | true | — | — | Scalar |
| Point | `System.Decimal` | true | true | — | — | Scalar |
| PointModifyReasonCode | `System.String` | true | true | — | — | Scalar |
| PointRecordTypeCode | `System.Byte` | true | true | — | — | Scalar |
