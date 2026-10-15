[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-35"></a>

## 35 — Journal / Muhasebe fişi

Muhasebe fişi için Muhasebe grubundaki model. Somut factory tipi NebimV3.GL.Journal. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.GL.Journal`. Grup: Muhasebe. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 35,
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "ApplicationCode": "{{ApplicationCode}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "CurrAccCode": "{{CurrAccCode}}",
      "CurrAccDescription": "ÖRNEK CurrAccDescription",
      "DocumentDate": "2026-01-01T00:00:00",
      "CountryCode": "{{CountryCode}}",
      "DocCurrencyCode": "TRY",
      "Debit": 0,
      "Credit": 0,
      "DueDate": "2026-01-01T00:00:00",
      "GLAccCode": "{{GLAccCode}}",
      "DocumentNumber": "{{DocumentNumber}}",
      "RefNumber": "{{RefNumber}}"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 35,
  "HeaderID": "{{exampleGuid}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "CurrAccCode": "{{CurrAccCode}}",
      "CurrAccDescription": "ÖRNEK CurrAccDescription",
      "DocumentDate": "2026-01-01T00:00:00",
      "CountryCode": "{{CountryCode}}",
      "DocCurrencyCode": "TRY",
      "Debit": 0,
      "Credit": 0,
      "DueDate": "2026-01-01T00:00:00",
      "GLAccCode": "{{GLAccCode}}",
      "DocumentNumber": "{{DocumentNumber}}",
      "RefNumber": "{{RefNumber}}"
    }
  ]
}
```

### Okuma / silme / şablon

GetModel için güvenilir yazılabilir anahtar adayı çıkarılamadı; uydurma HeaderID/Code gönderilmez.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=35` → `{"ModelType":35}`.

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
| Lines | `NebimV3.GL.JournalLineList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-6bcb5242b14a) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| ATAttributes | `NebimV3.GL.JournalATAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-ab1c542de791) |
| AddRecordToJournalLineExtension | `System.Boolean` | true | true | — | — | Scalar |
| AllowWithoutJournalTypeSubLoad | `System.Boolean` | true | true | — | — | Scalar |
| CashGLAccCode | `System.String` | true | true | — | 30 | Scalar |
| CreatedDate | `System.DateTime` | true | true | — | — | Scalar |
| CreatedUserName | `System.String` | true | true | — | — | Scalar |
| DebitIntegrator | `NebimV3.v3Entities.Integration.IIntegrator` | true | true | — | — | Scalar |
| DefATAttributes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.GL.JournalDefATAttribute>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-84b6d882062a) |
| Description | `System.String` | true | true | — | 1000 | Scalar |
| DisableCostCenterValidation | `System.Boolean` | true | true | — | — | Scalar |
| DisableGLTypeValidation | `System.Boolean` | true | true | — | — | Scalar |
| DoCheckDebitCredit | `System.Boolean` | true | true | — | — | Scalar |
| DocCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| EledgerInfo | `NebimV3.GL.JournalEledgerInfo` | true | true | — | — | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| ForceGenerateNumber | `System.Boolean` | true | true | — | — | Scalar |
| FromOfficeCode | `System.String` | true | true | — | 5 | Scalar |
| FromStoreCode | `System.String` | true | true | — | 30 | Scalar |
| IsDiffCurrencyEachLine | `System.Boolean` | true | true | — | — | Scalar |
| IsForeignCurrencyTransaction | `System.Boolean` | true | true | — | — | Scalar |
| IsGLPrinted | `System.Boolean` | true | true | — | — | Scalar |
| IsJournalPrinted | `System.Boolean` | true | true | — | — | Scalar |
| IsPostingApproved | `System.Boolean` | true | true | — | — | Scalar |
| JournalDate | `System.DateTime` | true | true | — | — | Scalar |
| JournalNumber | `System.String` | true | true | — | — | Scalar |
| JournalTypeSubCode | `System.Int16` | true | true | — | — | Scalar |
| LastUpdatedDate | `System.DateTime` | true | true | — | — | Scalar |
| LastUpdatedUserName | `System.String` | true | true | — | — | Scalar |
| LedgerEntryNumber | `System.Int64` | true | true | — | — | Scalar |
| LocalCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| RoundingErrorInfo | `NebimV3.ApplicationCommon.RoundingErrorLineInfo` | true | true | — | — | Scalar |
