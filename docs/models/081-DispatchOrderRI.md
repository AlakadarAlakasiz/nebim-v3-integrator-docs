[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-81"></a>

## 81 — DispatchOrderRI / Taksitli perakende satış sevk emri

Taksitli perakende satış sevk emri için Sevk emirleri grubundaki model. Somut factory tipi NebimV3.DispOrders.RetailInstallmentSale. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.DispOrders.RetailInstallmentSale`. Grup: Sevk emirleri. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.DispatchOrderController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 81,
  "CustomerCode": "{{CustomerCode}}",
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
  "ModelType": 81,
  "HeaderID": "{{exampleGuid}}",
  "CustomerCode": "{{CustomerCode}}",
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
  "ModelType": 81,
  "DispOrderNumber": "{{DispOrderNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=81` → `{"ModelType":81}`.

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
| Lines | `NebimV3.DispOrders.DispOrderLineList<NebimV3.DispOrders.RetailSaleLine>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-c8cfa4337099) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| AddRemainingOrdersOnInventory | `System.Boolean` | true | true | — | — | Scalar |
| ContactID | `System.Guid` | true | true | — | — | Scalar |
| CustomerASNNumber | `System.String` | true | true | — | 20 | Scalar |
| Description | `System.String` | true | true | — | — | Scalar |
| DisableValidatingItemInventory | `System.Boolean` | true | true | — | — | Scalar |
| DispOrderDate | `System.DateTime` | true | true | — | — | Scalar |
| DispOrderNumber | `System.String` | true | true | — | 30 | Scalar |
| DispOrderTime | `System.TimeSpan` | true | true | — | — | Scalar |
| FirstUseRemainingTolerance | `System.Boolean` | true | true | — | — | Scalar |
| ForceDeleteConfirmed | `System.Boolean` | true | true | — | — | Scalar |
| InternalDescription | `System.String` | true | true | — | — | Scalar |
| IsReturn | `System.Boolean` | true | true | — | — | Scalar |
| RoundsmanCode | `System.String` | true | true | — | 10 | Scalar |
| ShippingDate | `System.DateTime` | true | true | — | — | Scalar |
| ShippingTime | `System.TimeSpan` | true | true | — | — | Scalar |
| ShouldCustomValidateIntegratedTransaction | `System.Boolean` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| ToWarehouseCode | `System.String` | true | true | — | — | Scalar |
| WarehouseCode | `System.String` | true | true | — | 10 | Scalar |
| CustomerCode | `System.String` | true | true | — | 30 | Scalar |
| CustomerTypeCode | `System.Byte` | true | true | — | — | Scalar |
| UseProcessFlow | `System.Boolean` | true | true | — | — | Scalar |
