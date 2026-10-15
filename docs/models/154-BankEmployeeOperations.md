[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-154"></a>

## 154 — BankEmployeeOperations / Personel banka işlemleri

Personel banka işlemleri için Banka işlemleri grubundaki model. Somut factory tipi NebimV3.Banks.BankEmployeeOperations. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Banks.BankEmployeeOperations`. Grup: Banka işlemleri. Örnek kanıtı: `metadata-template`.

Alternatif kök / somut satır tipleri: `NebimV3.Banks.BankEmployeeOperationsLine`. Factory daha özel satır seçebilir; bütün varyantların eksiksizliği sertifikalanmamıştır.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.BankController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 154,
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "BankCurrAccCode": "{{BankCurrAccCode}}",
  "BankTransNumber": "{{BankTransNumber}}",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "DocumentNumber": "{{DocumentNumber}}",
  "RefNumber": "{{RefNumber}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "CurrAccCode": "{{CurrAccCode}}",
      "CompanyCode": 1,
      "BankCurrAccCode": "{{BankCurrAccCode}}",
      "BankAccountCode": "{{BankAccountCode}}",
      "DocCurrencyCode": "TRY",
      "Amount": 1,
      "DueDate": "2026-01-01T00:00:00",
      "GLAccCode": "{{GLAccCode}}",
      "DocumentNumber": "{{DocumentNumber}}"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 154,
  "HeaderID": "{{exampleGuid}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "BankCurrAccCode": "{{BankCurrAccCode}}",
  "BankTransNumber": "{{BankTransNumber}}",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "DocumentNumber": "{{DocumentNumber}}",
  "RefNumber": "{{RefNumber}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "CurrAccCode": "{{CurrAccCode}}",
      "CompanyCode": 1,
      "BankCurrAccCode": "{{BankCurrAccCode}}",
      "BankAccountCode": "{{BankAccountCode}}",
      "DocCurrencyCode": "TRY",
      "Amount": 1,
      "DueDate": "2026-01-01T00:00:00",
      "GLAccCode": "{{GLAccCode}}",
      "DocumentNumber": "{{DocumentNumber}}"
    }
  ]
}
```

### Okuma / silme / şablon

Yazılabilir anahtar yok; kaynak LoadEntity normal setter yolundan aday belge numarası gösterilir. Model bazında yükleme akışı doğrulanmış değildir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 154,
  "DocumentNumber": "{{DocumentNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=154` → `{"ModelType":154}`.

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
| Lines | `NebimV3.Banks.BankLineList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-a080508233ea) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| ATAttributes | `NebimV3.Banks.BankATAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-501d3f0d1a5c) |
| BankCurrAccCode | `System.String` | true | true | — | — | Scalar |
| BankTransNumber | `System.String` | true | true | — | — | Scalar |
| BankTransTypeCode | `NebimV3.Banks.BankTransTypes` | true | true | — | — | Scalar |
| DefATAttributes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Banks.BankDefATAttribute>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-069ffc3e65dc) |
| Description | `System.String` | true | true | — | — | Scalar |
| DoSeparateCurrAccBook | `System.Boolean` | true | true | — | — | Scalar |
| DocCurrencyCode | `System.String` | true | true | — | — | Scalar |
| DocumentDate | `System.DateTime` | true | true | — | — | Scalar |
| DocumentNumber | `System.String` | true | true | — | 30 | Scalar |
| DocumentTime | `System.TimeSpan` | true | true | — | — | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| ExchangeTypeCode | `System.Byte` | true | true | — | — | Scalar |
| ExportFileNumber | `System.String` | true | true | — | 30 | Scalar |
| GLTypeCode | `System.String` | true | true | — | 20 | Scalar |
| ImportFileNumber | `System.String` | true | true | — | 30 | Scalar |
| IsCreateEmployeeDebit | `System.Boolean` | true | true | — | — | Scalar |
| JournalDate | `System.DateTime` | true | true | — | — | Scalar |
| LocalCurrencyCode | `System.String` | true | true | — | — | Scalar |
| PosTerminalID | `System.Int16` | true | true | — | — | Scalar |
| RefNumber | `System.String` | true | true | — | — | Scalar |
| SetDocumentTypeAsJournal | `System.Boolean` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | — | Scalar |
