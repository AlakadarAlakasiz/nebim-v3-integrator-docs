[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-151"></a>

## 151 — InnerCT / Gümrükten mal transferi

Gümrükten mal transferi için İç stok işlemleri grubundaki model. Somut factory tipi NebimV3.InnerTransactions.TransferGoodsFromCustoms. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.InnerTransactions.TransferGoodsFromCustoms`. Grup: İç stok işlemleri. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.InnerController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 151,
  "InvoiceNumber": "{{InvoiceNumber}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "OperationDate": "2026-01-01T00:00:00",
  "IsReturn": false,
  "OperationTime": "00:00:00",
  "ShipmentMethodCode": "{{ShipmentMethodCode}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "ItemTypeCode": 1,
      "ItemCode": "{{ItemCode}}",
      "ColorCode": "{{ColorCode}}",
      "ItemDim1Code": "{{ItemDim1Code}}",
      "ItemDim2Code": "{{ItemDim2Code}}",
      "ItemDim3Code": "{{ItemDim3Code}}",
      "Qty1": 1,
      "Qty2": 0,
      "CurrencyCode": "TRY"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 151,
  "HeaderID": "{{exampleGuid}}",
  "InvoiceNumber": "{{InvoiceNumber}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "OperationDate": "2026-01-01T00:00:00",
  "IsReturn": false,
  "OperationTime": "00:00:00",
  "ShipmentMethodCode": "{{ShipmentMethodCode}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "ItemTypeCode": 1,
      "ItemCode": "{{ItemCode}}",
      "ColorCode": "{{ColorCode}}",
      "ItemDim1Code": "{{ItemDim1Code}}",
      "ItemDim2Code": "{{ItemDim2Code}}",
      "ItemDim3Code": "{{ItemDim3Code}}",
      "Qty1": 1,
      "Qty2": 0,
      "CurrencyCode": "TRY"
    }
  ]
}
```

### Okuma / silme / şablon

Yazılabilir anahtar yok; kaynak LoadEntity normal setter yolundan aday belge numarası gösterilir. Model bazında yükleme akışı doğrulanmış değildir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 151,
  "InvoiceNumber": "{{InvoiceNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=151` → `{"ModelType":151}`.

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
| Lines | `NebimV3.InnerTransactions.InnerLineList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-72dff8b065df) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| SetDefaultLotForItem | `System.Boolean` | true | true | — | — | Scalar |
| DeliveryCompanyCode | `System.String` | true | true | — | 10 | Scalar |
| Description | `System.String` | true | true | — | 200 | Scalar |
| DisableArrangeShipmentType | `System.Boolean` | true | true | — | — | Scalar |
| DisableItemValidation | `System.Boolean` | true | true | — | — | Scalar |
| EShipmentNumber | `System.String` | true | true | — | — | Scalar |
| EShipmentStatusCode | `System.Byte` | true | true | — | — | Scalar |
| ExportFileNumber | `System.String` | true | true | — | 30 | Scalar |
| FirstUseRemainingTolerance | `System.Boolean` | true | true | — | — | Scalar |
| ImportFileNumber | `System.String` | true | true | — | 30 | Scalar |
| InnerNumber | `System.String` | true | true | — | 30 | Scalar |
| InnerProcessType | `NebimV3.ApplicationCommon.InnerProcessTypes` | true | true | — | — | Scalar |
| InnerVehicleDrivers | `NebimV3.v3Entities.v3ElementItemList<NebimV3.InnerTransactions.InnerVehicleDrivers>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-a5cace201f40) |
| IsInnerOrderBase | `System.Boolean` | true | true | — | — | Scalar |
| IsPostingJournal | `System.Boolean` | true | true | — | — | Scalar |
| IsTransferApproved | `System.Boolean` | true | true | — | — | Scalar |
| JournalDate | `System.DateTime` | true | true | — | — | Scalar |
| LogisticsCompanyBOL | `System.String` | true | true | — | 30 | Scalar |
| OperationDate | `System.DateTime` | true | true | — | — | Scalar |
| OperationTime | `System.TimeSpan` | true | true | — | — | Scalar |
| RoundsmanCode | `System.String` | true | true | — | 10 | Scalar |
| SectionCode | `System.String` | true | true | — | — | Scalar |
| ServicemanCode | `System.String` | true | true | — | 10 | Scalar |
| ShipmentMethodCode | `System.String` | true | true | — | 10 | Scalar |
| ShouldValidateProductSerialNumber | `System.Boolean` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| TransportModeDetail | `NebimV3.InnerTransactions.InnerTransportModeDetail` | true | true | — | — | İç nesne [tip](../TYPES.md#t-3090e5bade58) |
| WarehouseCode | `System.String` | true | true | — | 10 | Scalar |
| CustomsDocumentNumber | `System.String` | true | true | — | 30 | Scalar |
| InvoiceHeaderID | `System.Guid` | true | true | — | — | Scalar |
| InvoiceNumber | `System.String` | true | true | — | — | Scalar |
| IsReturn | `System.Boolean` | true | true | — | — | Scalar |
| Series | `System.String` | true | true | — | 5 | Scalar |
| SeriesNumber | `System.Decimal` | true | true | — | — | Scalar |
| ToOfficeCode | `System.String` | true | true | — | 20 | Scalar |
| ToWarehouseCode | `System.String` | true | true | — | 30 | Scalar |
