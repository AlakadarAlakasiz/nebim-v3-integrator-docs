[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-28"></a>

## 28 — Material / Malzeme

Malzeme için Ürün ve tanımlar grubundaki model. Somut factory tipi NebimV3.Items.Material. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Items.Material`. Grup: Ürün ve tanımlar. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 28,
  "ItemCode": "{{ItemCode}}",
  "ItemDescription": "ÖRNEK ItemDescription",
  "ItemDimTypeCode": 0,
  "UnitOfMeasureCode1": "{{UnitOfMeasureCode1}}",
  "ItemTaxGrCode": "{{ItemTaxGrCode}}",
  "BOMEntityCode": "{{BOMEntityCode}}",
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
  "ModelType": 28,
  "ItemCode": "{{ItemCode}}",
  "ItemDescription": "ÖRNEK ItemDescription",
  "ItemDimTypeCode": 0,
  "UnitOfMeasureCode1": "{{UnitOfMeasureCode1}}",
  "ItemTaxGrCode": "{{ItemTaxGrCode}}",
  "BOMEntityCode": "{{BOMEntityCode}}",
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
  "ModelType": 28,
  "ItemCode": "{{ItemCode}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=28` → `{"ModelType":28}`.

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
| Attributes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.MaterialAttribute>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-25bae3f3282c) |
| BOMEntityCode | `System.String` | true | true | — | — | Scalar |
| Barcodes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemBarcode>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-5384dab1661d) |
| BasePrices | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemBasePrice>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f08d36671246) |
| BatchBarcodes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemBatchBarcode>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-d83aed23d31a) |
| ColorFabricBlend | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemColorFabricBlend>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-400cb0927e44) |
| CrossUnitOfMeasures | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemCrossUnitOfMeasure>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-1c4250f7b8db) |
| CustomsProductGroupCode | `System.Byte` | true | true | — | — | Scalar |
| DoNotLoadSectionTypeCodeAndDescriptionOnLoadItemSection | `System.Boolean` | true | true | — | — | Scalar |
| IsPurchaseOrderClosed | `System.Boolean` | true | true | — | — | Scalar |
| IsSalesOrderClosed | `System.Byte` | true | true | — | — | Scalar |
| IsStoreOrderClosed | `System.Boolean` | true | true | — | — | Scalar |
| ItemAirportSalesCommissionGroups | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemAirportSalesCommissionGroup>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-bb66148afcbd) |
| ItemAlike | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| ItemAlikes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemAlike>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-0ec85e6f13e5) |
| ItemColorAttribute | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemColorAttributes>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f66f48b7bfa6) |
| ItemDimTypeCode | `System.Byte` | true | true | — | — | Scalar |
| ItemMeasuresOfVolume | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemMeasuresOfVolume>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-3ab27ecab9fc) |
| ItemSection | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| ItemSections | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemSection>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-c939c076f1e5) |
| MaterialDescription | `System.String` | true | true | — | 200 | Scalar |
| MaxCreditCardInstallmentCount | `System.Byte` | true | true | — | — | Scalar |
| SupplyPeriod | `System.Int16` | true | true | — | — | Scalar |
| TextileCareSymbols | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemTextileCareSymbol>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-825016f4cbf3) |
| UnitConvertRate | `System.Single` | true | true | — | — | Scalar |
| UnitConvertRateNotFixed | `System.Boolean` | true | true | — | — | Scalar |
| UnitOfMeasureCode2 | `System.String` | true | true | — | 10 | Scalar |
| UseBatch | `System.Boolean` | true | true | — | — | Scalar |
| UseManufacturing | `System.Boolean` | true | true | — | — | Scalar |
| UseRoll | `System.Boolean` | true | true | — | — | Scalar |
| UseStore | `System.Boolean` | true | true | — | — | Scalar |
| VariantList | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| Variants | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemVariant>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-efb3ab5355ba) |
