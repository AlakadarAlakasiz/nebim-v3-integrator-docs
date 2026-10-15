[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-4"></a>

## 4 — Product / Ürün

Ürün için Ürün ve tanımlar grubundaki model. Somut factory tipi NebimV3.Items.Product. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Items.Product`. Grup: Ürün ve tanımlar. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 4,
  "ItemCode": "{{ItemCode}}",
  "ItemDescription": "ÖRNEK ItemDescription",
  "ProductTypeCode": 0,
  "ItemDimTypeCode": 0,
  "UnitOfMeasureCode1": "{{UnitOfMeasureCode1}}",
  "ItemTaxGrCode": "{{ItemTaxGrCode}}",
  "Descriptions": [
    {
      "Description": "ÖRNEK Description",
      "DataLanguageCode": "TR",
      "DataLanguageDescription": "{{DataLanguageDescription}}"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 4,
  "ItemCode": "{{ItemCode}}",
  "ItemDescription": "ÖRNEK ItemDescription",
  "ProductTypeCode": 0,
  "ItemDimTypeCode": 0,
  "UnitOfMeasureCode1": "{{UnitOfMeasureCode1}}",
  "ItemTaxGrCode": "{{ItemTaxGrCode}}",
  "Descriptions": [
    {
      "Description": "ÖRNEK Description",
      "DataLanguageCode": "TR"
    }
  ]
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 4,
  "ItemCode": "{{ItemCode}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=4` → `{"ModelType":4}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| CustomsTariffNumberCode | `System.String` | true | true | — | — | Scalar |
| Descriptions | `NebimV3.Items.ItemLanguageDescriptionList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f31bc69161d4) |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| IsITSDeclaratedItem | `System.Boolean` | true | true | — | — | Scalar |
| ItemAccountGrCode | `System.String` | true | true | — | 10 | Scalar |
| ItemCode | `System.String` | true | true | evet | 30 | Scalar |
| ItemCompanyBrands | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemCompanyBrand>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-a6b95519fa31) |
| ItemDescription | `System.String` | true | true | — | 200 | Scalar |
| ItemDiscountGrCode | `System.String` | true | true | — | 10 | Scalar |
| ItemInformations | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemInformation>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-95571e7e069c) |
| ItemNotes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemNotes>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-3733b9d36c25) |
| ItemPaymentPlanGrCode | `System.String` | true | true | — | 10 | Scalar |
| ItemRequisitions | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemRequisition>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-865cad1e047b) |
| ItemTaxGrCode | `System.String` | true | true | — | 10 | Scalar |
| ItemVendorGrCode | `System.String` | true | true | — | 10 | Scalar |
| ProductCareWarnings | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ProductCareWarning>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-7da53c5169bd) |
| ShelfLife | `System.Int16` | true | true | — | — | Scalar |
| UnitOfMeasureCode1 | `System.String` | true | true | — | 10 | Scalar |
| Attributes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ProductAttribute>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-6181ba12dc78) |
| BOMEntityCode | `System.String` | true | true | — | — | Scalar |
| Barcodes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemBarcode>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-5384dab1661d) |
| BasePrices | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemBasePrice>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f08d36671246) |
| BatchBarcodes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemBatchBarcode>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-d83aed23d31a) |
| ByWeight | `System.Boolean` | true | true | — | — | Scalar |
| ColorFabricBlend | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemColorFabricBlend>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-400cb0927e44) |
| CommercialRoleCode | `System.Byte` | true | true | — | — | Scalar |
| Contents | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.LinkedProductContent>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f4867b2a2b21) |
| CrossUnitOfMeasures | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemCrossUnitOfMeasure>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-1c4250f7b8db) |
| CustomsProductGroupCode | `System.Byte` | true | true | — | — | Scalar |
| DoNotLoadSectionTypeCodeAndDescriptionOnLoadItemSection | `System.Boolean` | true | true | — | — | Scalar |
| EraID | `System.Guid` | true | true | — | — | Scalar |
| GenerateOpticalDataMatrixCode | `System.Boolean` | true | true | — | — | Scalar |
| GenerateSerialNumber | `System.Boolean` | true | true | — | — | Scalar |
| GuaranteePeriod | `System.Int16` | true | true | — | — | Scalar |
| IsPurchaseOrderClosed | `System.Boolean` | true | true | — | — | Scalar |
| IsSalesOrderClosed | `System.Byte` | true | true | — | — | Scalar |
| IsStoreOrderClosed | `System.Boolean` | true | true | — | — | Scalar |
| IsSubsequentDeliveryForR | `System.Byte` | true | true | — | — | Scalar |
| IsSubsequentDeliveryForRI | `System.Byte` | true | true | — | — | Scalar |
| IsUTSDeclaratedItem | `System.Boolean` | true | true | — | — | Scalar |
| ItemAirportSalesCommissionGroups | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemAirportSalesCommissionGroup>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-bb66148afcbd) |
| ItemAlike | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| ItemAlikes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemAlike>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-0ec85e6f13e5) |
| ItemColorAttribute | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemColorAttributes>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f66f48b7bfa6) |
| ItemColorFabricBlend | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemColorFabricBlend>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-400cb0927e44) |
| ItemDimTypeCode | `System.Byte` | true | true | — | — | Scalar |
| ItemMeasuresOfVolume | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemMeasuresOfVolume>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-3ab27ecab9fc) |
| ItemSections | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemSection>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-c939c076f1e5) |
| ItemSerialNumberProperties | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemSerialNumberProperty>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-be63afb5a24b) |
| ItemUBLExtensionsList | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| LinkedProductProperties | `NebimV3.Items.LinkedProductProperties` | true | true | — | — | İç nesne [tip](../TYPES.md#t-140b01163fa0) |
| MarketPlaceProductInformations | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.MarketPlaceProductInformation>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-464874e2a9fc) |
| MaxCreditCardInstallmentCount | `System.Byte` | true | true | — | — | Scalar |
| MedicalProductImportCountries | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.MedicalProductImportCountries>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-2ea6952d28dc) |
| MedicalProductOriginCountries | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.MedicalProductOriginCountries>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-b75bd815803d) |
| MedicalProductPropertiesList | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.MedicalProductProperties>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-650c14c35aec) |
| OrderLeadTime | `System.Int32` | true | true | — | — | Scalar |
| OriginCountryCode | `System.String` | true | true | — | 10 | Scalar |
| PerceptionOfFashionCode | `System.Byte` | true | true | — | — | Scalar |
| ProductCollectionGrCode | `System.Int32` | true | true | — | — | Scalar |
| ProductColorAttributes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.AttributeProductColor>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-57fa3ee1f8d9) |
| ProductDescription | `System.String` | true | false | — | 200 | Scalar |
| ProductFrameProperties | `NebimV3.Items.ProductFrameProperties` | true | true | — | — | İç nesne [tip](../TYPES.md#t-64abda020cf8) |
| ProductHierarchyID | `System.Int32` | true | true | — | — | Scalar |
| ProductImageUrls | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ProductImageUrls>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-8120fbe78718) |
| ProductLensProperties | `NebimV3.Items.ProductLensProperties` | true | true | — | — | İç nesne [tip](../TYPES.md#t-a1078415fa16) |
| ProductLotBarcodes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ProductLotBarcode>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-9a85e7400140) |
| ProductLots | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ProductLot>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f89cf9349a14) |
| ProductPoints | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ProductPoint>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-820946221730) |
| ProductTypeCode | `System.Byte` | true | true | — | — | Scalar |
| PromotionGroupCode | `System.String` | true | true | — | 10 | Scalar |
| PromotionGroupCode2 | `System.String` | true | true | — | 10 | Scalar |
| StoreCapacityLevelCode | `System.String` | true | true | — | 5 | Scalar |
| StorePriceLevelCode | `System.Byte` | true | true | — | — | Scalar |
| SumLineContents | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.LinkedProductContentSum>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-98b58bcd3af2) |
| SupplyPeriod | `System.Int16` | true | true | — | — | Scalar |
| TextileCareSymbols | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemTextileCareSymbol>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-825016f4cbf3) |
| UnitConvertRate | `System.Single` | true | true | — | — | Scalar |
| UnitConvertRateNotFixed | `System.Boolean` | true | true | — | — | Scalar |
| UnitOfMeasureCode2 | `System.String` | true | true | — | 10 | Scalar |
| UseBatch | `System.Boolean` | true | true | — | — | Scalar |
| UseInternet | `System.Boolean` | true | true | — | — | Scalar |
| UseManufacturing | `System.Boolean` | true | true | — | — | Scalar |
| UsePOS | `System.Boolean` | true | true | — | — | Scalar |
| UseRoll | `System.Boolean` | true | true | — | — | Scalar |
| UseSerialNumber | `System.Boolean` | true | true | — | — | Scalar |
| UseStore | `System.Boolean` | true | true | — | — | Scalar |
| Variants | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemVariant>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-efb3ab5355ba) |
