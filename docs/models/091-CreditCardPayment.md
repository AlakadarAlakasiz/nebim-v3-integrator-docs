[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-91"></a>

## 91 — CreditCardPayment / Kredi kartı ödemesi

Kredi kartı ödemesi için Ödemeler grubundaki model. Somut factory tipi NebimV3.Payments.CreditCardPayment. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Payments.CreditCardPayment`. Grup: Ödemeler. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.CreditCardPaymentController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 91,
  "CurrAccCode": "{{CurrAccCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "PaymentDate": "2026-01-01T00:00:00",
  "DocumentNumber": "{{DocumentNumber}}",
  "RefNumber": "{{RefNumber}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "DocCurrencyCode": "TRY",
      "Amount": 1,
      "AcquirerBankCode": "{{AcquirerBankCode}}",
      "BankCardTypeCode": 0,
      "CancelBankCode": "{{CancelBankCode}}"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 91,
  "HeaderID": "{{exampleGuid}}",
  "CurrAccCode": "{{CurrAccCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "PaymentDate": "2026-01-01T00:00:00",
  "DocumentNumber": "{{DocumentNumber}}",
  "RefNumber": "{{RefNumber}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "DocCurrencyCode": "TRY",
      "Amount": 1,
      "AcquirerBankCode": "{{AcquirerBankCode}}",
      "BankCardTypeCode": 0,
      "CancelBankCode": "{{CancelBankCode}}"
    }
  ]
}
```

### Okuma / silme / şablon

Yazılabilir anahtar yok; kaynak LoadEntity normal setter yolundan aday belge numarası gösterilir. Model bazında yükleme akışı doğrulanmış değildir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 91,
  "DocumentNumber": "{{DocumentNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=91` → `{"ModelType":91}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| ApplicationCode | `System.String` | true | true | — | — | Scalar |
| ApplicationID | `System.Guid` | true | true | — | — | Scalar |
| AutoGenerateUniqueNumber | `System.Boolean` | true | true | — | — | Scalar |
| BlockCheckOutProcess | `System.Boolean` | true | true | — | — | Scalar |
| CheckByOperationDate | `System.Boolean` | true | false | — | — | Scalar |
| CompanyCode | `System.Decimal` | true | true | — | — | Scalar |
| DisableInsertDefaultAttributes | `System.Boolean` | true | true | — | — | Scalar |
| HeaderID | `System.Guid` | false | true | evet | — | readonly-scalar |
| IsCompleted | `System.Boolean` | true | true | — | — | Scalar |
| IsLocked | `System.Boolean` | true | true | — | — | Scalar |
| IsPrinted | `System.Boolean` | true | true | — | — | Scalar |
| Lines | `NebimV3.Payments.CreditCardPaymentLineList<NebimV3.Payments.CreditCardPaymentLine>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-2497be2ceb4d) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| ATAttributes | `NebimV3.Payments.CreditCardPaymentATAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-1bda36b75f98) |
| ContactID | `System.Guid` | true | true | — | — | Scalar |
| CreditCardPaymentNumber | `System.String` | true | true | — | — | Scalar |
| CreditCardPaymentTypeCode | `NebimV3.Payments.CreditCardPaymentTypes` | true | true | — | — | Scalar |
| CurrAccCode | `System.String` | true | true | — | 30 | Scalar |
| CurrAccTypeCode | `System.Byte` | true | true | — | — | Scalar |
| DefATAttributes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Payments.CreditCardPaymentDefATAttribute>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-bb14b4c0892f) |
| Description | `System.String` | true | true | — | 200 | Scalar |
| DoSeparateCurrAccBook | `System.Boolean` | true | true | — | — | Scalar |
| DocCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| DocumentNumber | `System.String` | true | true | — | — | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| GLTypeCode | `System.String` | true | true | — | 20 | Scalar |
| IsZeroAmountAcceptedOnLine | `System.Boolean` | true | true | — | — | Scalar |
| LocalCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| PaymentDate | `System.DateTime` | true | true | — | — | Scalar |
| PaymentTime | `System.TimeSpan` | true | true | — | — | Scalar |
| PosTerminalID | `System.Int16` | true | true | — | — | Scalar |
| RefNumber | `System.String` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| SubCurrAccID | `System.Guid` | true | true | — | — | Scalar |
