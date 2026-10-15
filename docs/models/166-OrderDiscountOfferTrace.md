[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-166"></a>

## 166 — OrderDiscountOfferTrace / Sipariş indirim izi

Sipariş indirim izi için Siparişler grubundaki model. Somut factory tipi NebimV3.Orders.OrderDiscountOffer. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Orders.OrderDiscountOffer`. Grup: Siparişler. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 166,
  "CustomerDiscountPointID": "{{exampleGuid}}",
  "DiscountAmount": 0,
  "DiscountOfferCode": "{{DiscountOfferCode}}",
  "DiscountPointTypeCode": "{{DiscountPointTypeCode}}",
  "DiscountRate": 0,
  "DiscountVoucherTypeCode": "{{DiscountVoucherTypeCode}}"
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 166,
  "CustomerDiscountPointID": "{{exampleGuid}}",
  "DiscountAmount": 0,
  "DiscountOfferCode": "{{DiscountOfferCode}}",
  "DiscountPointTypeCode": "{{DiscountPointTypeCode}}",
  "DiscountRate": 0,
  "DiscountVoucherTypeCode": "{{DiscountVoucherTypeCode}}"
}
```

### Okuma / silme / şablon

GetModel için güvenilir yazılabilir anahtar adayı çıkarılamadı; uydurma HeaderID/Code gönderilmez.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=166` → `{"ModelType":166}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| CustomerDiscountPointID | `System.Guid` | true | true | — | — | Scalar |
| DiscountAmount | `System.Decimal` | true | true | — | — | Scalar |
| DiscountOfferCode | `System.String` | true | true | — | — | Scalar |
| DiscountPointTypeCode | `System.String` | true | true | — | — | Scalar |
| DiscountRate | `System.Double` | true | true | — | — | Scalar |
| DiscountVoucherTypeCode | `System.String` | true | true | — | — | Scalar |
| EarnedAmount | `System.Decimal` | true | true | — | — | Scalar |
| EarnedPoint | `System.Decimal` | true | true | — | — | Scalar |
| IsBooster | `System.Boolean` | true | true | — | — | Scalar |
| IsEarned | `System.Boolean` | true | true | — | — | Scalar |
| OrderCancelDetailHeaderID | `System.Guid` | true | true | — | — | Scalar |
| OrderHeaderID | `System.Guid` | true | true | — | — | Scalar |
| OrderLineID | `System.Guid` | true | true | — | — | Scalar |
| Password | `System.String` | true | true | — | 30 | Scalar |
| PaymentTypeCode | `System.Byte` | true | true | — | — | Scalar |
| SerialNumber | `System.String` | true | true | — | — | Scalar |
| UsedAmount | `System.Decimal` | true | true | — | — | Scalar |
| UsedAsPayment | `System.Boolean` | true | true | — | — | Scalar |
| UsedPoint | `System.Decimal` | true | true | — | — | Scalar |
