[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-237"></a>

## 237 — WholesaleSellingVehicleLoading / Toptan satış araç yükleme

Toptan satış araç yükleme için Sevkiyat ve irsaliyeler grubundaki model. Somut factory tipi NebimV3.Shipments.WholesaleSellingVehicleLoading. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Shipments.WholesaleSellingVehicleLoading`. Grup: Sevkiyat ve irsaliyeler. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.ShipmentController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 237,
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "ApplicationCode": "{{ApplicationCode}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "ShipmentHeaderID": "{{exampleGuid}}",
      "ShippingNumber": "{{ShippingNumber}}",
      "SortOrder": 0
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 237,
  "HeaderID": "{{exampleGuid}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "ShipmentHeaderID": "{{exampleGuid}}",
      "ShippingNumber": "{{ShippingNumber}}",
      "SortOrder": 0
    }
  ]
}
```

### Okuma / silme / şablon

GetModel için güvenilir yazılabilir anahtar adayı çıkarılamadı; uydurma HeaderID/Code gönderilmez.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=237` → `{"ModelType":237}`.

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
| Lines | `NebimV3.Shipments.VehicleLoadingLineList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-857a0b240168) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| DeliveryCompanyCode | `System.String` | true | true | — | 10 | Scalar |
| Description | `System.String` | true | true | — | 200 | Scalar |
| IsClosed | `System.Boolean` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| UserLocked | `System.Boolean` | true | true | — | — | Scalar |
| VehicleCode | `System.String` | true | true | — | 10 | Scalar |
| VehicleLoadingDate | `System.DateTime` | true | true | — | — | Scalar |
| VehicleLoadingDrivers | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Shipments.VehicleLoadingDriver>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f65b50f986c8) |
| VehicleLoadingNumber | `System.String` | true | true | — | 30 | Scalar |
| VehicleLoadingRoundsmans | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Shipments.VehicleLoadingRoundsman>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-ea2a777fd10e) |
| VehicleLoadingTime | `System.TimeSpan` | true | true | — | — | Scalar |
| WarehouseCode | `System.String` | true | true | — | 10 | Scalar |
