[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-72"></a>

## 72 — ExpenseSlip / Gider pusulası

Gider pusulası için Gider ve borç/alacak belgeleri grubundaki model. Somut factory tipi NebimV3.ExpenseSlips.ExpenseSlip. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.ExpenseSlips.ExpenseSlip`. Grup: Gider ve borç/alacak belgeleri. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.ExpenseSlipController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 72,
  "CurrAccCode": "{{CurrAccCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "IsReturn": false,
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "DocumentNumber": "{{DocumentNumber}}",
  "RefNumber": "{{RefNumber}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "ItemCode": "{{ItemCode}}",
      "CurrAccDescription": "ÖRNEK CurrAccDescription",
      "DocumentDate": "2026-01-01T00:00:00",
      "ItemTypeCode": 1,
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
  "ModelType": 72,
  "HeaderID": "{{exampleGuid}}",
  "CurrAccCode": "{{CurrAccCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "IsReturn": false,
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "DocumentNumber": "{{DocumentNumber}}",
  "RefNumber": "{{RefNumber}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "ItemCode": "{{ItemCode}}",
      "CurrAccDescription": "ÖRNEK CurrAccDescription",
      "DocumentDate": "2026-01-01T00:00:00",
      "ItemTypeCode": 1,
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
  "ModelType": 72,
  "DocumentNumber": "{{DocumentNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=72` → `{"ModelType":72}`.

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
| Lines | `NebimV3.ExpenseSlips.ExpenseSlipLineList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-7585ab7c86f0) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| ATAttributes | `NebimV3.ExpenseSlips.ExpenseSlipATAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-cc2b3ff54de4) |
| AverageDueDate | `System.DateTime` | true | true | — | — | Scalar |
| ContactID | `System.Guid` | true | true | — | — | Scalar |
| CurrAccCode | `System.String` | true | true | — | 30 | Scalar |
| CurrAccTypeCode | `System.Byte` | true | true | — | — | Scalar |
| Description | `System.String` | true | true | — | 200 | Scalar |
| DocCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| DocumentDate | `System.DateTime` | true | true | — | — | Scalar |
| DocumentNumber | `System.String` | true | true | — | 30 | Scalar |
| DocumentTime | `System.TimeSpan` | true | true | — | — | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| ExpenseSlipNumber | `System.String` | true | true | — | — | Scalar |
| ExpenseSlipTypeCode | `System.Byte` | true | true | — | — | Scalar |
| ForceGenerateNumber | `System.Boolean` | true | true | — | — | Scalar |
| InternalDescription | `System.String` | true | true | — | 200 | Scalar |
| IsPostingJournal | `System.Boolean` | true | true | — | — | Scalar |
| IsReturn | `System.Boolean` | true | true | — | — | Scalar |
| JournalDate | `System.DateTime` | true | true | — | — | Scalar |
| LocalCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| PaymentTerm | `System.Int16` | true | true | — | — | Scalar |
| RefNumber | `System.String` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| SubCurrAccID | `System.Guid` | true | true | — | — | Scalar |
