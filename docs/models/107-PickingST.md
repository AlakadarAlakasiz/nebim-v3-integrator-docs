[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-107"></a>

## 107 — PickingST / Mağaza transferi toplama emri

Mağaza transferi toplama emri için Pickings grubundaki model. Somut factory tipi NebimV3.Pickings.StoreTransfer. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Pickings.StoreTransfer`. Grup: Pickings. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.PickingController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 107,
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "IsReturn": false,
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
  "ModelType": 107,
  "HeaderID": "{{exampleGuid}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "IsReturn": false,
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

Yazılabilir anahtar yok; kaynak LoadEntity normal setter yolundan aday belge numarası gösterilir. Model bazında yükleme akışı doğrulanmış değildir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 107,
  "PickingNumber": "{{PickingNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=107` → `{"ModelType":107}`.

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
| Lines | `NebimV3.Pickings.PickingLineList<NebimV3.Pickings.StoreTransferLine>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-e6eea569e326) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| ContactID | `System.Guid` | true | true | — | — | Scalar |
| CustomerASNNumber | `System.String` | true | true | — | 20 | Scalar |
| DeliveryCompanyBarcode | `System.String` | true | true | — | 30 | Scalar |
| Description | `System.String` | true | true | — | — | Scalar |
| DisableItemValidation | `System.Boolean` | true | true | — | — | Scalar |
| DisableValidateCanDeleteLine | `System.Boolean` | true | true | — | — | Scalar |
| FirstUseRemainingTolerance | `System.Boolean` | true | true | — | — | Scalar |
| ForceDeleteConfirmed | `System.Boolean` | true | true | — | — | Scalar |
| InternalDescription | `System.String` | true | true | — | — | Scalar |
| IsReturn | `System.Boolean` | true | true | — | — | Scalar |
| LogisticsCompanyBOL | `System.String` | true | true | — | 30 | Scalar |
| LogisticsPackageNumber | `System.String` | true | true | — | 30 | Scalar |
| PackageBrandCode | `System.String` | true | true | — | — | Scalar |
| PackageNumber | `System.String` | true | true | — | — | Scalar |
| PackageVolumeCode | `System.String` | true | true | — | 5 | Scalar |
| PackagingTypeCode | `System.String` | true | true | — | — | Scalar |
| PackedWeight | `System.Single` | true | true | — | — | Scalar |
| PickingDate | `System.DateTime` | true | true | — | — | Scalar |
| PickingNumber | `System.String` | true | true | — | 30 | Scalar |
| PickingTime | `System.TimeSpan` | true | true | — | — | Scalar |
| ShouldCustomValidateIntegratedTransaction | `System.Boolean` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| WarehouseCode | `System.String` | true | true | — | 10 | Scalar |
| WeightUnitOfMeasureCode | `System.String` | true | true | — | 10 | Scalar |
| ToStoreCode | `System.String` | true | true | — | 30 | Scalar |
| ToWarehouseCode | `System.String` | true | true | — | 30 | Scalar |
