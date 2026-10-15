[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-221"></a>

## 221 — DiscountVoucherBulkCreator / Toplu indirim çeki oluşturma

Toplu indirim çeki oluşturma için İndirim ve kampanya grubundaki model. Somut factory tipi NebimV3.DiscountOffers.DiscountVoucherBulkCreator. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.DiscountOffers.DiscountVoucherBulkCreator`. Grup: İndirim ve kampanya. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 221,
  "CurrencyCode": "TRY",
  "Amount": 1,
  "CustomerTypeCode": 0,
  "DiscountRate": 0,
  "DiscountVoucherCount": 0,
  "DiscountVoucherQuantity": 0
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 221,
  "CurrencyCode": "TRY",
  "Amount": 1,
  "CustomerTypeCode": 0,
  "DiscountRate": 0,
  "DiscountVoucherCount": 0,
  "DiscountVoucherQuantity": 0
}
```

### Okuma / silme / şablon

GetModel için güvenilir yazılabilir anahtar adayı çıkarılamadı; uydurma HeaderID/Code gönderilmez.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=221` → `{"ModelType":221}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| Amount | `System.Decimal` | true | true | — | — | Scalar |
| Barcode | `NebimV3.DiscountOffers.DiscountVoucherGenerateBarcode` | true | true | — | — | İç nesne [tip](../TYPES.md#t-cd5a335a51b4) |
| CurrencyCode | `System.String` | true | true | — | — | Scalar |
| CustomerCodes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.DiscountOffers.DiscountVoucherCustomerInfo>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-ed0310df0019) |
| CustomerTypeCode | `System.Byte` | true | true | — | — | Scalar |
| DiscountRate | `System.Decimal` | true | true | — | — | Scalar |
| DiscountVoucherCount | `System.Int32` | true | true | — | — | Scalar |
| DiscountVoucherQuantity | `System.Int32` | true | true | — | — | Scalar |
| DiscountVoucherTypeCode | `System.String` | true | true | — | — | Scalar |
| FirstValidDate | `System.DateTime` | true | true | — | — | Scalar |
| GenerateType | `System.Byte` | true | true | — | — | Scalar |
| LastValidDate | `System.DateTime` | true | true | — | — | Scalar |
| Manual | `NebimV3.DiscountOffers.DiscountVoucherGenerateManual` | true | true | — | — | İç nesne [tip](../TYPES.md#t-429df72d1899) |
| Random | `NebimV3.DiscountOffers.DiscountVoucherGenerateRandom` | true | true | — | — | İç nesne [tip](../TYPES.md#t-49b23897391e) |
