[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-17"></a>

## 17 — OrderSS / Hizmet satışı siparişi

Hizmet satışı siparişi için Siparişler grubundaki model. Somut factory tipi NebimV3.Orders.ServiceSale. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Orders.ServiceSale`. Grup: Siparişler. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.OrderController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 17,
  "CustomerCode": "{{CustomerCode}}",
  "OrderNumber": "{{OrderNumber}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "OrderDate": "2026-01-01T00:00:00",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "OrderTime": "00:00:00",
  "DocumentNumber": "{{DocumentNumber}}",
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
  "ModelType": 17,
  "HeaderID": "{{exampleGuid}}",
  "CustomerCode": "{{CustomerCode}}",
  "OrderNumber": "{{OrderNumber}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "OrderDate": "2026-01-01T00:00:00",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "OrderTime": "00:00:00",
  "DocumentNumber": "{{DocumentNumber}}",
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
  "ModelType": 17,
  "OrderNumber": "{{OrderNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=17` → `{"ModelType":17}`.

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
| Lines | `NebimV3.Orders.OrderSaleLineList<NebimV3.Orders.ServiceSaleLine>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f325f558e072) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| SetDefaultLotForItem | `System.Boolean` | true | true | — | — | Scalar |
| ATAttributes | `NebimV3.Orders.OrderATAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-a874ebf77d11) |
| AllowValidateEmptyPrice | `System.Boolean` | true | true | — | — | Scalar |
| CashRegisterInfos | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Orders.OrderCashRegisterInfo>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f79d4a79b9dc) |
| ContactID | `System.Guid` | true | true | — | — | Scalar |
| CreditableConfirmedDate | `System.DateTime` | true | true | — | — | Scalar |
| CreditableConfirmedUser | `System.String` | true | true | — | 20 | Scalar |
| DeliveryCompanyCode | `System.String` | true | true | — | 10 | Scalar |
| Description | `System.String` | true | true | — | — | Scalar |
| DiscountReasonCode | `System.Byte` | true | true | — | — | Scalar |
| DocumentNumber | `System.String` | true | true | — | 30 | Scalar |
| ExportFileNumber | `System.String` | true | true | — | 30 | Scalar |
| FTAttributes | `NebimV3.Orders.OrderFTAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-661625dc9d97) |
| GLTypeCode | `System.String` | true | true | — | 20 | Scalar |
| ImportFileNumber | `System.String` | true | true | — | 30 | Scalar |
| InternalDescription | `System.String` | true | true | — | — | Scalar |
| IsCreditSale | `System.Boolean` | true | true | — | — | Scalar |
| IsCreditableConfirmed | `System.Boolean` | true | true | — | — | Scalar |
| IsInstantForOpenOrder | `System.Boolean` | true | true | — | — | Scalar |
| IsProposalBased | `System.Boolean` | true | true | — | — | Scalar |
| IsSalesViaInternet | `System.Boolean` | true | true | — | — | Scalar |
| IsSuspended | `System.Boolean` | true | true | — | — | Scalar |
| ItemBalanceProcessFlowCode | `NebimV3.ApplicationCommon.ProcessFlowCodes` | true | true | — | — | Scalar |
| OrderDate | `System.DateTime` | true | true | — | — | Scalar |
| OrderHeaderExtension | `NebimV3.Orders.OrderHeaderExtension` | true | true | — | — | İç nesne [tip](../TYPES.md#t-8bf8fc7661c4) |
| OrderNumber | `System.String` | true | true | — | 30 | Scalar |
| OrderTime | `System.TimeSpan` | true | true | — | — | Scalar |
| OrdersViaInternetInfo | `NebimV3.Orders.OrdersViaInternetInfo` | true | true | — | — | İç nesne [tip](../TYPES.md#t-14dae919b6d6) |
| POSTerminalID | `System.Int16` | true | true | — | — | Scalar |
| PostalAddress | `NebimV3.ItemTransactions.TransactionPostalAddress` | true | true | — | — | İç nesne [tip](../TYPES.md#t-45eaf6e9e256) |
| RoundsmanCode | `System.String` | true | true | — | 10 | Scalar |
| ShipmentMethodCode | `System.String` | true | true | — | 10 | Scalar |
| ShouldCustomValidateIntegratedTransaction | `System.Boolean` | true | true | — | — | Scalar |
| ShouldSaveITAttributes | `System.Boolean` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| SurplusOrderQtyToleranceRate | `System.Double` | true | true | — | — | Scalar |
| UserLocked | `System.Boolean` | true | true | — | — | Scalar |
| WarehouseCode | `System.String` | true | true | — | 10 | Scalar |
| AverageDueDate | `System.DateTime` | true | true | — | — | Scalar |
| DOVCode | `System.String` | true | true | — | 10 | Scalar |
| DocCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| ExchangeTypeCode | `System.Byte` | true | true | — | — | Scalar |
| InsertRecordPaymentPlan | `System.Boolean` | true | false | — | — | Scalar |
| IsTaxIncluded | `System.Boolean` | true | true | — | — | Scalar |
| LocalCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| PaymentPlanCode | `System.String` | true | true | — | — | Scalar |
| PaymentTerm | `System.Int16` | true | true | — | — | Scalar |
| SuppressItemDiscount | `System.Boolean` | true | true | — | — | Scalar |
| TDisRate1 | `System.Double` | true | true | — | — | Scalar |
| TDisRate2 | `System.Double` | true | true | — | — | Scalar |
| TDisRate3 | `System.Double` | true | true | — | — | Scalar |
| TDisRate4 | `System.Double` | true | true | — | — | Scalar |
| TDisRate5 | `System.Double` | true | true | — | — | Scalar |
| TaxExemptionCode | `System.Int16` | true | true | — | — | Scalar |
| TaxTypeCode | `NebimV3.ItemTransactions.TaxTypes` | true | true | — | — | Scalar |
| WithHoldingTaxTypeCode | `System.String` | true | true | — | 10 | Scalar |
| BillingPostalAddressID | `System.Guid` | true | true | — | — | Scalar |
| ShippingPostalAddressID | `System.Guid` | true | true | — | — | Scalar |
| CustomerCode | `System.String` | true | true | — | 30 | Scalar |
| SubCurrAccID | `System.Guid` | true | true | — | — | Scalar |
