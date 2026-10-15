[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-8"></a>

## 8 — InvoiceR / Perakende satış faturası

Perakende satış faturası için Entegratör özel satış modelleri grubundaki model. Somut factory tipi NebimV3.Integrator.Models.RetailInvoiceShipmentBase. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Integrator.Models.RetailInvoiceShipmentBase`. Grup: Entegratör özel satış modelleri. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.InvoiceController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 8,
  "CustomerCode": "{{CustomerCode}}",
  "InvoiceNumber": "{{InvoiceNumber}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "OperationDate": "2026-01-01T00:00:00",
  "InvoiceDate": "2026-01-01T00:00:00",
  "IsReturn": false,
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "OperationTime": "00:00:00",
  "InvoiceTime": "00:00:00",
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
  "ModelType": 8,
  "HeaderID": "{{exampleGuid}}",
  "CustomerCode": "{{CustomerCode}}",
  "InvoiceNumber": "{{InvoiceNumber}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "OperationDate": "2026-01-01T00:00:00",
  "InvoiceDate": "2026-01-01T00:00:00",
  "IsReturn": false,
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "OperationTime": "00:00:00",
  "InvoiceTime": "00:00:00",
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
  "ModelType": 8,
  "InvoiceNumber": "{{InvoiceNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=8` → `{"ModelType":8}`.

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
| Lines | `NebimV3.Invoices.InvoiceLineList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-80440743f5ba) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| SetDefaultLotForItem | `System.Boolean` | true | true | — | — | Scalar |
| ATAttributes | `NebimV3.Invoices.InvoiceATAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-740c5188793c) |
| AddRemainingOrdersOnInventory | `System.Boolean` | true | true | — | — | Scalar |
| AllowValidateEmptyPrice | `System.Boolean` | true | true | — | — | Scalar |
| AverageDueDate | `System.DateTime` | true | true | — | — | Scalar |
| CashRegisterInfo | `NebimV3.Invoices.CashRegisterInfo` | true | true | — | — | İç nesne [tip](../TYPES.md#t-90e82861f934) |
| CombineAllWithSingleWareHouseCode | `System.Boolean` | true | true | — | — | Scalar |
| ContactID | `System.Guid` | true | true | — | — | Scalar |
| DBSBankCode | `System.String` | true | true | — | 10 | Scalar |
| DOVCode | `System.String` | true | true | — | 10 | Scalar |
| DeliveryCompanyBarcode | `System.String` | true | true | — | 30 | Scalar |
| DeliveryCompanyCode | `System.String` | true | true | — | 10 | Scalar |
| Description | `System.String` | true | true | — | — | Scalar |
| DisableEInvoiceValidateFromInbox | `System.Boolean` | true | false | — | — | Scalar |
| DisableLineValidation | `System.Boolean` | true | true | — | — | Scalar |
| DisableSummaryBackup | `System.Boolean` | true | true | — | — | Scalar |
| DisableValidatingItemInventory | `System.Boolean` | true | true | — | — | Scalar |
| DiscountReasonCode | `System.Byte` | true | true | — | — | Scalar |
| DocCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| DocumentTypeCode | `System.Byte` | true | true | — | — | Scalar |
| EArchiveInvoiceConfirmation | `NebimV3.Invoices.EArchiveInvoiceConfirmation` | true | false | — | — | İç nesne [tip](../TYPES.md#t-30411ac2d02d) |
| EArchivePrefixCode | `System.String` | true | true | — | — | Scalar |
| EInvoiceAliasCode | `System.String` | true | true | — | — | Scalar |
| EInvoiceNumber | `System.String` | true | true | — | — | Scalar |
| EInvoiceStatusCode | `NebimV3.Invoices.EInvoiceStatus` | true | true | — | — | Scalar |
| EMailAddress | `System.String` | true | true | — | — | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| ExchangeTypeCode | `System.Byte` | true | true | — | — | Scalar |
| ExpenseTypeCode | `System.Byte` | true | true | — | — | Scalar |
| ExportFileNumber | `System.String` | true | true | — | 30 | Scalar |
| FTAttributes | `NebimV3.Invoices.InvoiceFTAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-5db01423ff6d) |
| FirstUseRemainingTolerance | `System.Boolean` | true | true | — | — | Scalar |
| FiscalPrintedState | `System.Byte` | true | true | — | — | Scalar |
| FormType | `NebimV3.ApplicationCommon.FormTypes` | true | true | — | — | Scalar |
| GLTypeCode | `System.String` | true | true | — | 20 | Scalar |
| GSMNo | `System.String` | true | true | — | — | Scalar |
| GetUnofficialInvoiceString | `System.Boolean` | true | true | — | — | Scalar |
| ImportFileNumber | `System.String` | true | true | — | 30 | Scalar |
| IntegrationDebitLines | `System.Collections.Generic.IEnumerable<NebimV3.Payments.DebitLine>` | true | false | — | — | Scalar |
| InternalDescription | `System.String` | true | true | — | — | Scalar |
| InvoiceDate | `System.DateTime` | true | true | — | — | Scalar |
| InvoiceExchangeDifferencePaidChequeList | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Invoices.InvoiceExchangeDifferencePaidCheque>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-5da09791c9c4) |
| InvoiceHeaderExtension | `NebimV3.Invoices.InvoiceHeaderExtension` | true | true | — | — | İç nesne [tip](../TYPES.md#t-e0ae35b311ec) |
| InvoiceNumber | `System.String` | true | true | — | 30 | Scalar |
| InvoiceSourceInfo | `NebimV3.Invoices.InvoiceSourceInfo` | true | true | — | — | İç nesne [tip](../TYPES.md#t-c97d3c070769) |
| InvoiceTime | `System.TimeSpan` | true | true | — | — | Scalar |
| InvoiceUBLExtensionsList | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Invoices.InvoiceUBLExtensions>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-56b539ca998a) |
| IsConstInvoiceTypeAsInvoice | `System.Boolean` | true | false | — | — | Scalar |
| IsCreditSale | `System.Boolean` | true | true | — | — | Scalar |
| IsOrderBase | `System.Boolean` | true | true | — | — | Scalar |
| IsPickingBase | `System.Boolean` | true | true | — | — | Scalar |
| IsProposalBased | `System.Boolean` | true | true | — | — | Scalar |
| IsReportedSaleBase | `System.Boolean` | true | true | — | — | Scalar |
| IsReturn | `System.Boolean` | true | true | — | — | Scalar |
| IsSalesViaInternet | `System.Boolean` | true | true | — | — | Scalar |
| IsShipmentBase | `System.Boolean` | true | true | — | — | Scalar |
| IsSuspended | `System.Boolean` | true | true | — | — | Scalar |
| IsTaxIncluded | `System.Boolean` | true | true | — | — | Scalar |
| JournalDate | `System.DateTime` | true | true | — | — | Scalar |
| LocalCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| OnlineDBSWebServiceCode | `System.String` | true | true | — | 30 | Scalar |
| OperationDate | `System.DateTime` | true | true | — | — | Scalar |
| OperationTime | `System.TimeSpan` | true | true | — | — | Scalar |
| PaymentTerm | `System.Int16` | true | true | — | — | Scalar |
| PosTerminalID | `System.Int16` | true | true | — | — | Scalar |
| PostalAddress | `NebimV3.ItemTransactions.TransactionPostalAddress` | true | true | — | — | İç nesne [tip](../TYPES.md#t-45eaf6e9e256) |
| RoundsmanCode | `System.String` | true | true | — | 10 | Scalar |
| SalesViaInternetInfo | `NebimV3.Invoices.SalesViaInternetInfo` | true | true | — | — | İç nesne [tip](../TYPES.md#t-cf89a1e677d7) |
| SectionCode | `System.String` | true | true | — | — | Scalar |
| SendInvoiceByEMail | `System.Boolean` | true | true | — | — | Scalar |
| SendInvoiceBySMS | `System.Boolean` | true | true | — | — | Scalar |
| Series | `System.String` | true | true | — | 5 | Scalar |
| SeriesNumber | `System.Decimal` | true | true | — | — | Scalar |
| ShipmentMethodCode | `System.String` | true | true | — | 10 | Scalar |
| ShouldCustomValidateIntegratedTransaction | `System.Boolean` | true | true | — | — | Scalar |
| ShouldPrintEArchiveOnSave | `System.Boolean` | true | true | — | — | Scalar |
| SkipSubCurrAcc | `System.Boolean` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| SuppressItemDiscount | `System.Boolean` | true | true | — | — | Scalar |
| TDisRate1 | `System.Double` | true | true | — | — | Scalar |
| TDisRate2 | `System.Double` | true | true | — | — | Scalar |
| TDisRate3 | `System.Double` | true | true | — | — | Scalar |
| TDisRate4 | `System.Double` | true | true | — | — | Scalar |
| TDisRate5 | `System.Double` | true | true | — | — | Scalar |
| TaxExemptionCode | `System.Int16` | true | true | — | — | Scalar |
| TaxTypeCode | `NebimV3.ItemTransactions.TaxTypes` | true | true | — | — | Scalar |
| TransportModeDetail | `NebimV3.Invoices.InvoiceTransportModeDetail` | true | true | — | — | İç nesne [tip](../TYPES.md#t-133677e62c6f) |
| UnofficialInvoiceString | `System.String` | false | true | — | — | readonly-scalar |
| UseOrderExchangeRate | `System.Boolean` | true | true | — | — | Scalar |
| UseOrderLineDiscount | `System.Boolean` | true | true | — | — | Scalar |
| UseOrderPrice | `System.Boolean` | true | false | — | — | Scalar |
| WarehouseCode | `System.String` | true | true | — | 10 | Scalar |
| WithHoldingTaxTypeCode | `System.String` | true | true | — | 10 | Scalar |
| BillingPostalAddressID | `System.Guid` | true | true | — | — | Scalar |
| DigitalMarketingServiceCode | `System.String` | true | true | — | — | Scalar |
| InstantDiscountEnable | `System.Boolean` | true | false | — | — | Scalar |
| PaymentPlanCode | `System.String` | true | true | — | — | Scalar |
| ShippingPostalAddressID | `System.Guid` | true | true | — | — | Scalar |
| CustomerCode | `System.String` | true | true | — | 30 | Scalar |
| CustomerTypeCode | `NebimV3.ApplicationCommon.CurrAccTypes` | true | true | — | — | Scalar |
| DefaultPreviousProcess | `NebimV3.ApplicationCommon.ProcessFlowCodes` | true | true | — | — | Scalar |
| GuarantorContactID | `System.Guid` | true | true | — | — | Scalar |
| GuarantorContactID2 | `System.Guid` | true | true | — | — | Scalar |
| IncotermCode1 | `System.String` | true | true | — | — | Scalar |
| IncotermCode2 | `System.String` | true | true | — | — | Scalar |
| InvoiceHeaderSalesPersons | `NebimV3.v3Entities.v3EntityList<NebimV3.Invoices.InvoiceHeaderSalesPerson>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-1d0ce06f568b) |
| InvoiceLineLinkedProducts | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Invoices.InvoiceLineLinkedProduct>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-34cd6173cd74) |
| PaymentMethodCode | `System.String` | true | true | — | 20 | Scalar |
| SkipSetCustomerLoyaltyProgramState | `System.Boolean` | true | true | — | — | Scalar |
| SkipUpdateCustomerLoyaltyLevelStatus | `System.Boolean` | true | true | — | — | Scalar |
| TransactionLineLinkedProducts | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| UseEmptyPct | `System.Boolean` | true | true | — | — | Scalar |
