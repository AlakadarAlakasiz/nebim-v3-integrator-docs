[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-193"></a>

## 193 — DepartmentReceipt / Departman makbuzu

Departman makbuzu için Faturalar grubundaki model. Somut factory tipi NebimV3.Invoices.DepartmentReceipt. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Invoices.DepartmentReceipt`. Grup: Faturalar. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.InvoiceController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 193,
  "CustomerCode": "{{CustomerCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "ItemCode": "{{ItemCode}}",
      "WarehouseCode": "{{WarehouseCode}}",
      "ItemTypeCode": 1,
      "ColorCode": "{{ColorCode}}",
      "ItemDim1Code": "{{ItemDim1Code}}",
      "ItemDim2Code": "{{ItemDim2Code}}",
      "ItemDim3Code": "{{ItemDim3Code}}"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 193,
  "HeaderID": "{{exampleGuid}}",
  "CustomerCode": "{{CustomerCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "ItemCode": "{{ItemCode}}",
      "WarehouseCode": "{{WarehouseCode}}",
      "ItemTypeCode": 1,
      "ColorCode": "{{ColorCode}}",
      "ItemDim1Code": "{{ItemDim1Code}}",
      "ItemDim2Code": "{{ItemDim2Code}}",
      "ItemDim3Code": "{{ItemDim3Code}}"
    }
  ]
}
```

### Okuma / silme / şablon

GetModel için güvenilir yazılabilir anahtar adayı çıkarılamadı; uydurma HeaderID/Code gönderilmez.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=193` → `{"ModelType":193}`.

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
| Lines | `NebimV3.Invoices.DepartmentReceiptLineList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-db2bc5292fb3) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| CustomerCode | `System.String` | true | true | — | 30 | Scalar |
| CustomerTypeCode | `NebimV3.ApplicationCommon.CurrAccTypes` | true | true | — | — | Scalar |
| DepartmentReceiptNumber | `System.String` | true | true | — | 30 | Scalar |
| Description | `System.String` | true | true | — | 200 | Scalar |
| DocumentDate | `System.DateTime` | true | true | — | — | Scalar |
| DocumentTime | `System.TimeSpan` | true | true | — | — | Scalar |
| IsTransformed | `System.Boolean` | true | true | — | — | Scalar |
| SalesHeaderID | `System.Guid` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| StoreTypeCode | `System.Byte` | true | true | — | — | Scalar |
