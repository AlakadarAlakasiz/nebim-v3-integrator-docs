[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-160"></a>

## 160 — BankPaymentInstruction / Banka ödeme talimatı

Banka ödeme talimatı için Banka işlemleri grubundaki model. Somut factory tipi NebimV3.Banks.BankPaymentInstruction. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Banks.BankPaymentInstruction`. Grup: Banka işlemleri. Örnek kanıtı: `metadata-template`.

Alternatif kök / somut satır tipleri: `NebimV3.Banks.BankPaymentInstructionLine`. Factory daha özel satır seçebilir; bütün varyantların eksiksizliği sertifikalanmamıştır.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.BankController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 160,
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "BankCurrAccCode": "{{BankCurrAccCode}}",
  "DocCurrencyCode": "TRY",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "CurrAccCode": "{{CurrAccCode}}",
      "DocCurrencyCode": "TRY",
      "Amount": 1,
      "DueDate": "2026-01-01T00:00:00",
      "BankAccNo": "{{BankAccNo}}"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 160,
  "HeaderID": "{{exampleGuid}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "BankCurrAccCode": "{{BankCurrAccCode}}",
  "DocCurrencyCode": "TRY",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "CurrAccCode": "{{CurrAccCode}}",
      "DocCurrencyCode": "TRY",
      "Amount": 1,
      "DueDate": "2026-01-01T00:00:00",
      "BankAccNo": "{{BankAccNo}}"
    }
  ]
}
```

### Okuma / silme / şablon

GetModel için güvenilir yazılabilir anahtar adayı çıkarılamadı; uydurma HeaderID/Code gönderilmez.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=160` → `{"ModelType":160}`.

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
| Lines | `NebimV3.Banks.BankPaymentInstructionLineList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-d6f9c38bd1ed) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| ATAttributes | `NebimV3.Banks.BankPaymentInstructionATAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-a999894488dc) |
| Attributes | `NebimV3.Attributes.TransactionAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-fcfa773935b9) |
| BankCurrAccCode | `System.String` | true | true | — | 30 | Scalar |
| BankPaymentInstructionNumber | `System.String` | true | true | — | — | Scalar |
| ConfirmedDate | `System.DateTime` | true | true | — | — | Scalar |
| ConfirmedUserName | `System.String` | true | true | — | — | Scalar |
| CreateWithDocCurrencyCode | `System.Boolean` | true | true | — | — | Scalar |
| Description | `System.String` | true | true | — | 200 | Scalar |
| DocCurrencyCode | `System.String` | true | true | — | — | Scalar |
| DocumentDate | `System.DateTime` | true | true | — | — | Scalar |
| DocumentTime | `System.TimeSpan` | true | true | — | — | Scalar |
| IsConfirmed | `System.Boolean` | true | true | — | — | Scalar |
| IsFileCreated | `System.Boolean` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | — | Scalar |
| StoreTypeCode | `System.Byte` | true | true | — | — | Scalar |
