[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-29"></a>

## 29 — FixedAsset / Sabit kıymet

Sabit kıymet için Sabit kıymetler grubundaki model. Somut factory tipi NebimV3.FixedAssets.FixedAsset. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.FixedAssets.FixedAsset`. Grup: Sabit kıymetler. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 29,
  "ItemCode": "{{ItemCode}}",
  "ItemDescription": "ÖRNEK ItemDescription",
  "UnitOfMeasureCode1": "{{UnitOfMeasureCode1}}",
  "ItemTaxGrCode": "{{ItemTaxGrCode}}",
  "CustomsTariffNumberCode": "{{CustomsTariffNumberCode}}",
  "FixedAssetDescription": "{{FixedAssetDescription}}",
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
  "ModelType": 29,
  "ItemCode": "{{ItemCode}}",
  "ItemDescription": "ÖRNEK ItemDescription",
  "UnitOfMeasureCode1": "{{UnitOfMeasureCode1}}",
  "ItemTaxGrCode": "{{ItemTaxGrCode}}",
  "CustomsTariffNumberCode": "{{CustomsTariffNumberCode}}",
  "FixedAssetDescription": "{{FixedAssetDescription}}",
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
  "ModelType": 29,
  "ItemCode": "{{ItemCode}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=29` → `{"ModelType":29}`.

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
| AttributeList | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| Attributes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.FixedAssetAttribute>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-fffd677dd4ce) |
| Barcodes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemBarcode>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-5384dab1661d) |
| BasePrices | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemBasePrice>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f08d36671246) |
| DoNotLoadSectionTypeCodeAndDescriptionOnLoadItemSection | `System.Boolean` | true | true | — | — | Scalar |
| FixedAssetDescription | `System.String` | true | true | — | 200 | Scalar |
| GuaranteePeriod | `System.Int16` | true | true | — | — | Scalar |
| ItemMeasuresOfVolume | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemMeasuresOfVolume>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-3ab27ecab9fc) |
| ItemSection | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| SupplyPeriod | `System.Int16` | true | true | — | — | Scalar |
| UsePOS | `System.Boolean` | true | true | — | — | Scalar |
| FixedAssetDepreciationInfo | `NebimV3.FixedAssets.FixedAssetDepreciationInfo` | true | true | — | — | İç nesne [tip](../TYPES.md#t-22821c6c2b82) |
| FixedAssetEmployeeList | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| FixedAssetEmployees | `NebimV3.v3Entities.v3ElementItemList<NebimV3.FixedAssets.FixedAssetEmployee>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-634c7a0a062f) |
| FixedAssetExpenses | `NebimV3.v3Entities.v3ElementItemList<NebimV3.FixedAssets.FixedAssetExpense>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-67926fe698be) |
| FixedAssetPurchases | `NebimV3.v3Entities.v3ElementItemList<NebimV3.FixedAssets.FixedAssetPurchases>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-0936318a63a0) |
| FixedAssetReassessmentRates | `NebimV3.v3Entities.v3ElementItemList<NebimV3.FixedAssets.FixedAssetReassessmentRates>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-04a6e796a256) |
| FixedAssetReassessmentRatesList | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| FixedAssetSales | `NebimV3.v3Entities.v3ElementItemList<NebimV3.FixedAssets.FixedAssetSales>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-1472d39e5f7f) |
| InsuranceList | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| Insurances | `NebimV3.v3Entities.v3ElementItemList<NebimV3.FixedAssets.FixedAssetInsurance>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-a0abf557edbb) |
