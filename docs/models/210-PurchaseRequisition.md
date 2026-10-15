[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-210"></a>

## 210 — PurchaseRequisition / Satın alma talebi

Satın alma talebi için Talepler grubundaki model. Somut factory tipi NebimV3.Requisitions.PurchaseRequisition. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Requisitions.PurchaseRequisition`. Grup: Talepler. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.RequisitionController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 210,
  "CurrAccCode": "{{CurrAccCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "ApplicationCode": "{{ApplicationCode}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "ItemTypeCode": 1,
      "ItemCode": "{{ItemCode}}",
      "ColorCode": "{{ColorCode}}",
      "ItemDim1Code": "{{ItemDim1Code}}",
      "ItemDim2Code": "{{ItemDim2Code}}",
      "ItemDim3Code": "{{ItemDim3Code}}",
      "Price": 1,
      "Amount": 1,
      "CurrencyCode": "TRY"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 210,
  "HeaderID": "{{exampleGuid}}",
  "CurrAccCode": "{{CurrAccCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "ItemTypeCode": 1,
      "ItemCode": "{{ItemCode}}",
      "ColorCode": "{{ColorCode}}",
      "ItemDim1Code": "{{ItemDim1Code}}",
      "ItemDim2Code": "{{ItemDim2Code}}",
      "ItemDim3Code": "{{ItemDim3Code}}",
      "Price": 1,
      "Amount": 1,
      "CurrencyCode": "TRY"
    }
  ]
}
```

### Okuma / silme / şablon

GetModel için güvenilir yazılabilir anahtar adayı çıkarılamadı; uydurma HeaderID/Code gönderilmez.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=210` → `{"ModelType":210}`.

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
| Lines | `NebimV3.Requisitions.PurchaseRequisitionLineList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-3055fa2eed75) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| SetDefaultLotForItem | `System.Boolean` | true | true | — | — | Scalar |
| ATAttributes | `NebimV3.Requisitions.PurchaseRequisitionATAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-e512819d0faf) |
| CompanyName | `System.String` | true | true | — | 200 | Scalar |
| ContractStatusCode | `System.String` | true | true | — | 10 | Scalar |
| CurrAccCode | `System.String` | true | true | — | 30 | Scalar |
| DeliveryOfficeCode | `System.String` | true | true | — | 20 | Scalar |
| DeliveryStoreCode | `System.String` | true | true | — | 30 | Scalar |
| DeliveryWarehouseCode | `System.String` | true | true | — | 10 | Scalar |
| Description | `System.String` | true | true | — | 200 | Scalar |
| IdentityNum | `System.String` | true | true | — | 20 | Scalar |
| PurchaseRequisitionDate | `System.DateTime` | true | true | — | — | Scalar |
| PurchaseRequisitionNumber | `System.String` | true | true | — | 30 | Scalar |
| PurchaseRequisitionTime | `System.TimeSpan` | true | true | — | — | Scalar |
| RequesterEmployeeCode | `System.String` | true | true | — | 30 | Scalar |
| RequesterFirstLastName | `System.String` | true | true | — | 200 | Scalar |
| RequesterJobDepartmentCode | `System.String` | true | true | — | 10 | Scalar |
| RequesterWorkplaceCode | `System.String` | true | true | — | 10 | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| TaxNumber | `System.String` | true | true | — | 10 | Scalar |
| TaxOfficeCode | `System.String` | true | true | — | 10 | Scalar |
| UserLocked | `System.Boolean` | true | true | — | — | Scalar |
