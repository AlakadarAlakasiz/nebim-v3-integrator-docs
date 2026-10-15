[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-162"></a>

## 162 — AdjustCostInner / İç işlem maliyet düzeltmesi

İç işlem maliyet düzeltmesi için Maliyet işlemleri grubundaki model. Somut factory tipi NebimV3.Cost.AdjustCostHeaderInner. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Cost.AdjustCostHeaderInner`. Grup: Maliyet işlemleri. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.AdjustCostController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 162,
  "AdjustCostHeaderID": "{{exampleGuid}}",
  "InvoiceNumber": "{{InvoiceNumber}}",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "OperationDate": "2026-01-01T00:00:00",
  "BankTransNumber": "{{BankTransNumber}}",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "Amount": 1,
  "Rate": 0,
  "OperationTime": "00:00:00",
  "RefNumber": "{{RefNumber}}"
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 162,
  "AdjustCostHeaderID": "{{exampleGuid}}",
  "InvoiceNumber": "{{InvoiceNumber}}",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "OperationDate": "2026-01-01T00:00:00",
  "BankTransNumber": "{{BankTransNumber}}",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "Amount": 1,
  "Rate": 0,
  "OperationTime": "00:00:00",
  "RefNumber": "{{RefNumber}}"
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 162,
  "AdjustCostHeaderID": "{{exampleGuid}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=162` → `{"ModelType":162}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| AdjustAllEPInvoiceLine | `System.Boolean` | true | true | — | — | Scalar |
| AdjustCostHeaderID | `System.Guid` | true | true | evet | — | Scalar |
| AdjustCostMethodCode | `System.Byte` | true | true | — | — | Scalar |
| AdjustCostNumber | `System.String` | true | true | — | — | Scalar |
| Amount | `System.Decimal` | true | true | — | — | Scalar |
| BankHeaderID | `System.Guid` | true | true | — | — | Scalar |
| BankTransNumber | `System.String` | true | true | — | — | Scalar |
| CompanyCode | `System.Decimal` | true | true | — | — | Scalar |
| DisableLockOperation | `System.Boolean` | true | true | — | — | Scalar |
| DocCurrencyCode | `System.String` | true | true | — | — | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| ExpenseSlipHeaderID | `System.Guid` | true | true | — | — | Scalar |
| ExportFileNumber | `System.String` | true | true | — | — | Scalar |
| ImportFileNumber | `System.String` | true | true | — | — | Scalar |
| InvoiceHeaderID | `System.Guid` | true | true | — | — | Scalar |
| InvoiceNumber | `System.String` | true | true | — | — | Scalar |
| IsCompleted | `System.Boolean` | true | true | — | — | Scalar |
| IsLocked | `System.Boolean` | true | true | — | — | Scalar |
| LocalCurrencyCode | `System.String` | true | true | — | — | Scalar |
| OfficeCode | `System.String` | true | true | — | — | Scalar |
| OperationDate | `System.DateTime` | true | true | — | — | Scalar |
| OperationTime | `System.TimeSpan` | true | true | — | — | Scalar |
| Rate | `System.Single` | true | true | — | — | Scalar |
| RefNumber | `System.String` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | — | Scalar |
| AdjustCostTransactions | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| InnerProcessCode | `System.String` | true | true | — | — | Scalar |
| ProcessCode | `System.String` | true | true | — | — | Scalar |
| AdjustCostInners | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Cost.AdjustCostInner>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-4889ad9525e7) |
