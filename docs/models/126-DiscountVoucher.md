[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-126"></a>

## 126 — DiscountVoucher / İndirim çeki

İndirim çeki için İndirim ve kampanya grubundaki model. Somut factory tipi NebimV3.DiscountOffers.DiscountVoucher. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.DiscountOffers.DiscountVoucher`. Grup: İndirim ve kampanya. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 126,
  "DiscountVoucherTypeCode": "{{DiscountVoucherTypeCode}}",
  "SerialNumber": "{{SerialNumber}}",
  "CustomerCode": "{{CustomerCode}}",
  "CurrencyCode": "TRY",
  "Amount": 1,
  "CancelDate": "2026-01-01T00:00:00"
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 126,
  "DiscountVoucherTypeCode": "{{DiscountVoucherTypeCode}}",
  "SerialNumber": "{{SerialNumber}}",
  "CustomerCode": "{{CustomerCode}}",
  "CurrencyCode": "TRY",
  "Amount": 1,
  "CancelDate": "2026-01-01T00:00:00"
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 126,
  "DiscountVoucherTypeCode": "{{DiscountVoucherTypeCode}}",
  "SerialNumber": "{{SerialNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=126` → `{"ModelType":126}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| Amount | `System.Decimal` | true | true | — | — | Scalar |
| CancelDate | `System.DateTime` | true | true | — | — | Scalar |
| CancelDescription | `System.String` | true | true | — | — | Scalar |
| CurrencyCode | `System.String` | true | true | — | — | Scalar |
| CustomerCode | `System.String` | true | true | — | 30 | Scalar |
| CustomerTypeCode | `System.Byte` | true | true | — | — | Scalar |
| DiscountRate | `System.Single` | true | true | — | — | Scalar |
| DiscountVoucherTypeCode | `System.String` | true | true | evet | — | Scalar |
| FirstValidDate | `System.DateTime` | true | true | — | — | Scalar |
| InvoiceHeaderID | `System.Guid` | true | true | — | — | Scalar |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| IsCanceled | `System.Boolean` | true | true | — | — | Scalar |
| IsReturnVoucher | `System.Boolean` | true | true | — | — | Scalar |
| IsUsed | `System.Boolean` | true | true | — | — | Scalar |
| LastValidDate | `System.DateTime` | true | true | — | — | Scalar |
| MinAmount | `System.Decimal` | true | true | — | — | Scalar |
| OrderHeaderID | `System.Guid` | true | true | — | — | Scalar |
| SerialNumber | `System.String` | true | true | evet | — | Scalar |
| UsedAmount | `System.Decimal` | true | true | — | — | Scalar |
