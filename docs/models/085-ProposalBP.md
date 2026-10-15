[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-85"></a>

## 85 — ProposalBP / Toplu alış teklifi

Toplu alış teklifi için Teklifler grubundaki model. Somut factory tipi NebimV3.Proposals.BulkPurchase. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Proposals.BulkPurchase`. Grup: Teklifler. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.ProposalController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 85,
  "VendorCode": "{{VendorCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "ProposalNumber": "{{ProposalNumber}}",
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
  "ModelType": 85,
  "HeaderID": "{{exampleGuid}}",
  "VendorCode": "{{VendorCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "ProposalNumber": "{{ProposalNumber}}",
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
      "Price": 1,
      "Amount": 1,
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
  "ModelType": 85,
  "ProposalNumber": "{{ProposalNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=85` → `{"ModelType":85}`.

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
| Lines | `NebimV3.Proposals.ProposalPurchaseLineList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-e88370b7f2dc) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| SetDefaultLotForItem | `System.Boolean` | true | true | — | — | Scalar |
| ATAttributes | `NebimV3.Proposals.ProposalATAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-28e295806fc6) |
| AllowValidateEmptyPrice | `System.Boolean` | true | true | — | — | Scalar |
| AverageDueDate | `System.DateTime` | true | true | — | — | Scalar |
| CompanyName | `System.String` | true | true | — | 200 | Scalar |
| ContactID | `System.Guid` | true | true | — | — | Scalar |
| DOVCode | `System.String` | true | true | — | 10 | Scalar |
| Description | `System.String` | true | true | — | — | Scalar |
| DocCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| ExchangeTypeCode | `System.Byte` | true | true | — | — | Scalar |
| ExpiredDate | `System.DateTime` | true | true | — | — | Scalar |
| ExportFileNumber | `System.String` | true | true | — | 30 | Scalar |
| FTAttributes | `NebimV3.Proposals.ProposalFTAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-3dbd5956fabe) |
| GLTypeCode | `System.String` | true | true | — | 20 | Scalar |
| IdentityNum | `System.String` | true | true | — | 20 | Scalar |
| ImportFileNumber | `System.String` | true | true | — | 30 | Scalar |
| InternalDescription | `System.String` | true | true | — | — | Scalar |
| IsCreditSale | `System.Boolean` | true | true | — | — | Scalar |
| IsTaxIncluded | `System.Boolean` | true | true | — | — | Scalar |
| LocalCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| PaymentPlanCode | `System.String` | true | true | — | — | Scalar |
| PaymentTerm | `System.Int16` | true | true | — | — | Scalar |
| ProposalDate | `System.DateTime` | true | true | — | — | Scalar |
| ProposalNumber | `System.String` | true | true | — | 30 | Scalar |
| ProposalTime | `System.TimeSpan` | true | true | — | — | Scalar |
| ShipmentMethodCode | `System.String` | true | true | — | 10 | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| SuppressItemDiscount | `System.Boolean` | true | true | — | — | Scalar |
| TDisRate1 | `System.Double` | true | true | — | — | Scalar |
| TDisRate2 | `System.Double` | true | true | — | — | Scalar |
| TDisRate3 | `System.Double` | true | true | — | — | Scalar |
| TDisRate4 | `System.Double` | true | true | — | — | Scalar |
| TDisRate5 | `System.Double` | true | true | — | — | Scalar |
| TaxExemptionCode | `System.Int16` | true | true | — | — | Scalar |
| TaxNumber | `System.String` | true | true | — | 10 | Scalar |
| TaxOfficeCode | `System.String` | true | true | — | 10 | Scalar |
| TaxTypeCode | `NebimV3.ItemTransactions.TaxTypes` | true | true | — | — | Scalar |
| WarehouseCode | `System.String` | true | true | — | 10 | Scalar |
| WithHoldingTaxTypeCode | `System.String` | true | true | — | 10 | Scalar |
| BillingPostalAddressID | `System.Guid` | true | true | — | — | Scalar |
| ShippingPostalAddressID | `System.Guid` | true | true | — | — | Scalar |
| SubCurrAccID | `System.Guid` | true | true | — | — | Scalar |
| UseRequisitionBase | `System.Boolean` | true | true | — | — | Scalar |
| VendorCode | `System.String` | true | true | — | 30 | Scalar |
| PaymentMethodCode | `System.String` | true | true | — | 20 | Scalar |
| StoppageRate | `System.Double` | true | true | — | — | Scalar |
