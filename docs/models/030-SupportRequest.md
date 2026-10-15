[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-30"></a>

## 30 — SupportRequest / Destek talebi

Destek talebi için Ürün destek süreçleri grubundaki model. Somut factory tipi NebimV3.ProductSupport.SupportRequest. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.ProductSupport.SupportRequest`. Grup: Ürün destek süreçleri. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 30,
  "CurrAccCode": "{{CurrAccCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "ColorCode": "{{ColorCode}}",
  "ItemDim1Code": "{{ItemDim1Code}}",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "ItemDim2Code": "{{ItemDim2Code}}",
  "ItemDim3Code": "{{ItemDim3Code}}",
  "ProductTypeCode": 0,
  "DocumentNumber": "{{DocumentNumber}}",
  "ShipmentMethodCode": "{{ShipmentMethodCode}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "ItemTypeCode": 1,
      "ColorCode": "{{ColorCode}}",
      "ItemDim1Code": "{{ItemDim1Code}}",
      "Price": 1,
      "DocCurrencyCode": "TRY",
      "Qty2": 0,
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
  "ModelType": 30,
  "HeaderID": "{{exampleGuid}}",
  "CurrAccCode": "{{CurrAccCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "ColorCode": "{{ColorCode}}",
  "ItemDim1Code": "{{ItemDim1Code}}",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "ItemDim2Code": "{{ItemDim2Code}}",
  "ItemDim3Code": "{{ItemDim3Code}}",
  "ProductTypeCode": 0,
  "DocumentNumber": "{{DocumentNumber}}",
  "ShipmentMethodCode": "{{ShipmentMethodCode}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "ItemTypeCode": 1,
      "ColorCode": "{{ColorCode}}",
      "ItemDim1Code": "{{ItemDim1Code}}",
      "Price": 1,
      "DocCurrencyCode": "TRY",
      "Qty2": 0,
      "ItemDim2Code": "{{ItemDim2Code}}",
      "ItemDim3Code": "{{ItemDim3Code}}"
    }
  ]
}
```

### Okuma / silme / şablon

Yazılabilir anahtar yok; kaynak LoadEntity normal setter yolundan aday belge numarası gösterilir. Model bazında yükleme akışı doğrulanmış değildir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 30,
  "DocumentNumber": "{{DocumentNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=30` → `{"ModelType":30}`.

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
| Lines | `NebimV3.ProductSupport.SupportRequestLineList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-22c392cca4dd) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| SetDefaultLotForItem | `System.Boolean` | true | true | — | — | Scalar |
| ApplicationLineID | `System.Guid` | true | true | — | — | Scalar |
| BatchCode | `System.String` | true | true | — | — | Scalar |
| BillingPostalAddressID | `System.Guid` | true | true | — | — | Scalar |
| CanChangeProduct | `System.Byte` | true | true | — | — | Scalar |
| ColorCode | `System.String` | true | true | — | 10 | Scalar |
| ConfirmationTypeCode | `System.Byte` | true | true | — | — | Scalar |
| ContactID | `System.Guid` | true | true | — | — | Scalar |
| CurrAccCode | `System.String` | true | true | — | — | Scalar |
| CurrAccTypeCode | `System.Byte` | true | true | — | — | Scalar |
| Date | `System.DateTime` | true | true | — | — | Scalar |
| DeliveryCompanyCode | `System.String` | true | true | — | — | Scalar |
| DeliveryDate | `System.DateTime` | true | true | — | — | Scalar |
| DeliveryTime | `System.TimeSpan` | true | true | — | — | Scalar |
| Description | `System.String` | true | true | — | 200 | Scalar |
| DocCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| DocumentNumber | `System.String` | true | true | — | 30 | Scalar |
| EMailAddress | `System.String` | true | true | — | — | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| IgnoreSerialNumber | `System.Boolean` | true | true | — | — | Scalar |
| IsClosed | `System.Boolean` | true | true | — | — | Scalar |
| IsSupportRequestForInventory | `System.Boolean` | true | true | — | — | Scalar |
| IsSupportResolved | `System.Boolean` | false | true | — | — | readonly-scalar |
| ItemDim1Code | `System.String` | true | true | — | — | Scalar |
| ItemDim2Code | `System.String` | true | true | — | — | Scalar |
| ItemDim3Code | `System.String` | true | true | — | — | Scalar |
| LocalCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| Number | `System.String` | true | true | — | — | Scalar |
| POSTerminalID | `System.Int16` | true | true | — | — | Scalar |
| PhoneNumberForSMS | `System.String` | true | true | — | — | Scalar |
| PriorityCode | `System.Byte` | true | true | — | — | Scalar |
| ProductCode | `System.String` | true | true | — | 30 | Scalar |
| ProductSerialNumber | `System.String` | true | true | — | — | Scalar |
| ProductTypeCode | `System.Byte` | true | true | — | — | Scalar |
| RequestDate | `System.DateTime` | true | true | — | — | Scalar |
| RequestTime | `System.TimeSpan` | true | true | — | — | Scalar |
| RoundsmanCode | `System.String` | true | true | — | — | Scalar |
| SalespersonCode | `System.String` | true | true | — | 10 | Scalar |
| SendResultsByEMail | `System.Boolean` | true | true | — | — | Scalar |
| SendResultsBySMS | `System.Boolean` | true | true | — | — | Scalar |
| ShipmentMethodCode | `System.String` | true | true | — | — | Scalar |
| ShippingPostalAddressID | `System.Guid` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| SubCurrAccID | `System.Guid` | true | true | — | — | Scalar |
| SupportRequestConfirmations | `NebimV3.v3Entities.v3ElementItemList<NebimV3.ProductSupport.SupportRequestConfirmation>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-a0db20f7918d) |
| SupportRequestDecisionLetter | `NebimV3.v3Entities.v3ElementItemList<NebimV3.ProductSupport.SupportRequestDecisionLetter>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-29eeedceefdf) |
| SupportRequestHeaderID | `System.Guid` | true | true | — | — | Scalar |
| SupportRequestNumber | `System.String` | true | true | — | 30 | Scalar |
| SupportResolves | `NebimV3.v3Entities.v3ElementItemList<NebimV3.ProductSupport.SupportResolve>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-9164a3574f5c) |
| SupportStatusHistories | `NebimV3.v3Entities.v3ElementItemList<NebimV3.ProductSupport.SupportStatusHistory>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-417e25d9228c) |
| SupportTypeCode | `System.Byte` | true | true | — | — | Scalar |
| Time | `System.TimeSpan` | true | true | — | — | Scalar |
| UsedBarcode | `System.String` | true | true | — | — | Scalar |
| WarehouseCode | `System.String` | true | true | — | 10 | Scalar |
