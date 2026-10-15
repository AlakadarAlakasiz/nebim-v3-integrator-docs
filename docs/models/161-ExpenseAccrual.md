[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-161"></a>

## 161 — ExpenseAccrual / Gider tahakkuku

Gider tahakkuku için Muhasebe grubundaki model. Somut factory tipi NebimV3.GL.ExpenseAccrual. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.GL.ExpenseAccrual`. Grup: Muhasebe. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.ExpenseAccrualController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 161,
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "Amount": 1,
  "RefNumber": "{{RefNumber}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "DocCurrencyCode": "TRY",
      "Amount": 1,
      "DueDate": "2026-01-01T00:00:00",
      "CostCenterCode": "{{CostCenterCode}}",
      "CreditGLAccCode": "{{CreditGLAccCode}}"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 161,
  "HeaderID": "{{exampleGuid}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "Amount": 1,
  "RefNumber": "{{RefNumber}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "DocCurrencyCode": "TRY",
      "Amount": 1,
      "DueDate": "2026-01-01T00:00:00",
      "CostCenterCode": "{{CostCenterCode}}",
      "CreditGLAccCode": "{{CreditGLAccCode}}"
    }
  ]
}
```

### Okuma / silme / şablon

GetModel için güvenilir yazılabilir anahtar adayı çıkarılamadı; uydurma HeaderID/Code gönderilmez.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=161` → `{"ModelType":161}`.

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
| Lines | `NebimV3.GL.ExpenseAccrualLineList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-01edf92e21d3) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| ATAttributes | `NebimV3.GL.ExpenseAccrualATAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-e8b635b75e42) |
| Amount | `System.Decimal` | true | true | — | — | Scalar |
| Description | `System.String` | true | true | — | — | Scalar |
| DocCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| DocumentDate | `System.DateTime` | true | true | — | — | Scalar |
| DocumentTime | `System.TimeSpan` | true | true | — | — | Scalar |
| DueDayCount | `System.Int16` | true | true | — | — | Scalar |
| EndDate | `System.DateTime` | true | true | — | — | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| ExportFileNumber | `System.String` | true | true | — | — | Scalar |
| ImportFileNumber | `System.String` | true | true | — | — | Scalar |
| InstallmentCount | `System.Int16` | true | true | — | — | Scalar |
| IsExpense | `System.Boolean` | true | true | — | — | Scalar |
| LocalCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| RefNumber | `System.String` | true | true | — | — | Scalar |
| StartDate | `System.DateTime` | true | true | — | — | Scalar |
