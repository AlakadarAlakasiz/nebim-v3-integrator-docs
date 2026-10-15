[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-68"></a>

## 68 — GiftCard / Hediye kartı

Hediye kartı için Ürün ve tanımlar grubundaki model. Somut factory tipi NebimV3.Items.GiftCard. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Items.GiftCard`. Grup: Ürün ve tanımlar. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.GiftCardController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 68,
  "SerialNumber": "{{SerialNumber}}",
  "ItemCode": "{{ItemCode}}",
  "CurrencyCode": "TRY",
  "ItemTypeCode": 1,
  "Amount": 1,
  "AfterSaleAvailableDay": 0
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 68,
  "SerialNumber": "{{SerialNumber}}",
  "ItemCode": "{{ItemCode}}",
  "CurrencyCode": "TRY",
  "ItemTypeCode": 1,
  "Amount": 1,
  "AfterSaleAvailableDay": 0
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 68,
  "SerialNumber": "{{SerialNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=68` → `{"ModelType":68}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| AfterSaleAvailableDay | `System.Int32` | true | true | — | — | Scalar |
| Amount | `System.Decimal` | true | true | — | — | Scalar |
| CannotReturn | `System.Boolean` | true | true | — | — | Scalar |
| CurrencyCode | `System.String` | true | true | — | — | Scalar |
| FirstValidDate | `System.DateTime` | true | true | — | — | Scalar |
| IgnoreSMSVerificationOnUse | `System.Boolean` | true | true | — | — | Scalar |
| InvoiceHeaderID | `System.Guid` | true | true | — | — | Scalar |
| IsAmountToBeEnteredOnSale | `System.Boolean` | true | true | — | — | Scalar |
| IsBearerVoucher | `System.Boolean` | true | true | — | — | Scalar |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| IsDisposable | `System.Boolean` | true | true | — | — | Scalar |
| IsSold | `System.Boolean` | true | true | — | — | Scalar |
| ItemCode | `System.String` | true | true | — | — | Scalar |
| ItemTypeCode | `System.Byte` | true | true | — | — | Scalar |
| LastValidDate | `System.DateTime` | true | true | — | — | Scalar |
| MaxSaleAmount | `System.Decimal` | true | true | — | — | Scalar |
| MessageResponseID | `System.String` | true | true | — | — | Scalar |
| MinSaleAmount | `System.Decimal` | true | true | — | — | Scalar |
| OrderHeaderID | `System.Guid` | true | true | — | — | Scalar |
| SaleMultiplesOfValue | `System.Double` | true | true | — | — | Scalar |
| SerialNumber | `System.String` | true | true | evet | — | Scalar |
| UseSMSVerificationOnUse | `System.Boolean` | true | true | — | — | Scalar |
| UsedAmount | `System.Decimal` | true | true | — | — | Scalar |
| VerifiedPhoneNumber | `System.String` | true | true | — | — | Scalar |
