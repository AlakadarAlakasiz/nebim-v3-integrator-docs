[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-59"></a>

## 59 — StoreTransfer / Mağazalar arası transfer

Mağazalar arası transfer için Sevkiyat ve irsaliyeler grubundaki model. Somut factory tipi NebimV3.Shipments.StoreTransfer. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Shipments.StoreTransfer`. Grup: Sevkiyat ve irsaliyeler. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.ShipmentController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 59,
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
      "Qty2": 0
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 59,
  "HeaderID": "{{exampleGuid}}",
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
      "Qty2": 0
    }
  ]
}
```

### Okuma / silme / şablon

GetModel için güvenilir yazılabilir anahtar adayı çıkarılamadı; uydurma HeaderID/Code gönderilmez.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=59` → `{"ModelType":59}`.

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
| Lines | `NebimV3.Shipments.ShipmentLineList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-1fbbf67720ab) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| SetDefaultLotForItem | `System.Boolean` | true | true | — | — | Scalar |
| AddRemainingOrdersOnInventory | `System.Boolean` | true | true | — | — | Scalar |
| CanAcceptUnDeliveredEShipments | `System.Boolean` | true | true | — | — | Scalar |
| ContactID | `System.Guid` | true | true | — | — | Scalar |
| CustomerASNNumber | `System.String` | true | true | — | 20 | Scalar |
| DeliveryCompanyCode | `System.String` | true | true | — | 10 | Scalar |
| Description | `System.String` | true | true | — | — | Scalar |
| DisableArrangeShipmentType | `System.Boolean` | true | true | — | — | Scalar |
| DisableLineUpdateValidation | `System.Boolean` | true | true | — | — | Scalar |
| DisablePossibleShipmentOrderQty | `System.Boolean` | true | true | — | — | Scalar |
| DisableProcessFlowValidation | `System.Boolean` | true | true | — | — | Scalar |
| DisableReturnReasonValidation | `System.Boolean` | true | true | — | — | Scalar |
| DisableValidatingItemInventory | `System.Boolean` | true | true | — | — | Scalar |
| EShipmentNumber | `System.String` | true | true | — | — | Scalar |
| EShipmentStatusCode | `NebimV3.Shipments.EShipmentStatus` | true | true | — | — | Scalar |
| EnableValidatingItemInventoryForPicking | `System.Boolean` | true | true | — | — | Scalar |
| ExportFileNumber | `System.String` | true | true | — | 30 | Scalar |
| FirstUseRemainingTolerance | `System.Boolean` | true | true | — | — | Scalar |
| ForceValidatingProductSerialNumberInventory | `System.Boolean` | true | true | — | — | Scalar |
| ImportFileNumber | `System.String` | true | true | — | 30 | Scalar |
| InternalDescription | `System.String` | true | true | — | — | Scalar |
| IsInstant | `System.Boolean` | true | true | — | — | Scalar |
| IsInstantWithRemainings | `System.Boolean` | true | true | — | — | Scalar |
| IsOrderBase | `System.Boolean` | true | true | — | — | Scalar |
| IsPickingBase | `System.Boolean` | true | true | — | — | Scalar |
| IsReturn | `System.Boolean` | true | true | — | — | Scalar |
| JournalDate | `System.DateTime` | true | true | — | — | Scalar |
| LogisticsCompanyBOL | `System.String` | true | true | — | 30 | Scalar |
| OperationDate | `System.DateTime` | true | true | — | — | Scalar |
| OperationTime | `System.TimeSpan` | true | true | — | — | Scalar |
| RoundsmanCode | `System.String` | true | true | — | 10 | Scalar |
| SectionCode | `System.String` | true | true | — | — | Scalar |
| Series | `System.String` | true | true | — | 5 | Scalar |
| SeriesNumber | `System.Decimal` | true | true | — | — | Scalar |
| ShipmentMethodCode | `System.String` | true | true | — | 10 | Scalar |
| ShipmentUBLExtensionsList | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Shipments.ShipmentUBLExtensions>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-580747938f06) |
| ShipmentVehicleDrivers | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Shipments.ShipmentVehicleDrivers>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-3651f12f8f45) |
| ShippingDate | `System.DateTime` | true | true | — | — | Scalar |
| ShippingNumber | `System.String` | true | true | — | 30 | Scalar |
| ShippingTime | `System.TimeSpan` | true | true | — | — | Scalar |
| ShouldCustomValidateIntegratedTransaction | `System.Boolean` | true | true | — | — | Scalar |
| ShouldValidateProductSerialNumber | `System.Boolean` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| TransportModeDetail | `NebimV3.Shipments.ShipmentTransportModeDetail` | true | true | — | — | İç nesne [tip](../TYPES.md#t-5107edd62a95) |
| UseOrderPrice | `System.Boolean` | true | true | — | — | Scalar |
| WarehouseCode | `System.String` | true | true | — | 10 | Scalar |
| IsTransferApproved | `System.Boolean` | true | true | — | — | Scalar |
| ShippingPostalAddressID | `System.Guid` | true | true | — | — | Scalar |
| StoreTransferType | `NebimV3.Shipments.StoreTransferTypes` | true | true | — | — | Scalar |
| ToStoreCode | `System.String` | true | true | — | 30 | Scalar |
| ToWarehouseCode | `System.String` | true | true | — | 30 | Scalar |
