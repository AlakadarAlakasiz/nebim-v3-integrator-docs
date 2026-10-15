[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-2"></a>

## 2 — Customer / Müşteri

Müşteri için Cari hesaplar grubundaki model. Somut factory tipi NebimV3.CurrentAccounts.Customer. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.CurrentAccounts.Customer`. Grup: Cari hesaplar. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.CustomerController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 2,
  "CurrAccCode": "{{CurrAccCode}}",
  "FirstName": "ÖRNEK FirstName",
  "LastName": "ÖRNEK LastName",
  "CurrAccDescription": "ÖRNEK CurrAccDescription",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "CurrencyCode": "TRY",
  "Descriptions": [
    {
      "Description": "ÖRNEK Description",
      "DataLanguageCode": "TR",
      "DataLanguageDescription": "{{DataLanguageDescription}}"
    }
  ],
  "PostalAddresses": [
    {
      "PostalAddressID": "{{exampleGuid}}",
      "AddressTypeCode": "{{AddressTypeCode}}",
      "CountryCode": "{{CountryCode}}",
      "StateCode": "{{StateCode}}",
      "CityCode": "{{CityCode}}",
      "DistrictCode": "{{DistrictCode}}",
      "Address": "{{Address}}"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 2,
  "CurrAccCode": "{{CurrAccCode}}",
  "CurrAccTypeCode": 0,
  "FirstName": "ÖRNEK FirstName",
  "LastName": "ÖRNEK LastName",
  "CurrAccDescription": "ÖRNEK CurrAccDescription",
  "OfficeCode": "{{OfficeCode}}",
  "CurrencyCode": "TRY",
  "PostalAddresses": [
    {
      "PostalAddressID": "{{exampleGuid}}",
      "AddressTypeCode": "{{AddressTypeCode}}",
      "CountryCode": "{{CountryCode}}",
      "StateCode": "{{StateCode}}",
      "CityCode": "{{CityCode}}",
      "DistrictCode": "{{DistrictCode}}",
      "Address": "{{Address}}"
    }
  ],
  "Communications": [
    {
      "CommunicationID": "{{exampleGuid}}",
      "CommAddress": "{{CommAddress}}",
      "CommunicationTypeCode": "{{CommunicationTypeCode}}",
      "ContactID": "{{exampleGuid}}",
      "FormNumber": "{{FormNumber}}",
      "SubCurrAccID": "{{exampleGuid}}"
    }
  ]
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 2,
  "CurrAccCode": "{{CurrAccCode}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=2` → `{"ModelType":2}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| AllCommunications | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccCommunication>` | true | false | — | — | Dizi; somut satır [tip](../TYPES.md#t-c757efaab26b) |
| AllContacts | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccContact>` | true | false | — | — | Dizi; somut satır [tip](../TYPES.md#t-1f53ee6347f3) |
| AllPostalAddresses | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccPostalAddress>` | true | false | — | — | Dizi; somut satır [tip](../TYPES.md#t-f1a249f03cbd) |
| Attributes | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| Communications | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccCommunication>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-c757efaab26b) |
| CompanyCode | `System.Decimal` | true | false | — | — | Scalar |
| Contacts | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccContact>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-1f53ee6347f3) |
| CurrAccBankAccNoes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccBankAccNo>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f4bd66b4f46e) |
| CurrAccCode | `System.String` | true | true | evet | 30 | Scalar |
| CurrAccDefault | `NebimV3.CurrentAccounts.CurrAccDefault` | true | true | — | — | İç nesne [tip](../TYPES.md#t-a2ddb012503c) |
| CurrAccDescription | `System.String` | true | true | — | 200 | Scalar |
| CurrAccEInvoiceAliases | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccEInvoiceAlias>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-b2ae5ead7b3e) |
| CurrAccEInvoiceOfficialForms | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccEInvoiceOfficialForm>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-7536829e9d15) |
| CurrAccEShipmentAliases | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccEShipmentAlias>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-00a3c22833b4) |
| CurrAccEShipmentOfficialForms | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccEShipmentOfficialForm>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-3dfc8ebd607d) |
| CurrAccExtendedProperties | `NebimV3.CurrentAccounts.CurrAccExtendedProperties` | true | true | — | — | İç nesne [tip](../TYPES.md#t-ef1983922379) |
| CurrAccInformations | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccInformation>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-52d736d8f68f) |
| CurrAccNotes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccNotes>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-2c6168b5bc2a) |
| CurrAccOnlineBank | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccOnlineBank>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-8e8df4059bfb) |
| CurrAccPersonalDataConfirmationStatus | `NebimV3.CurrentAccounts.CurrAccPersonalDataConfirmationStatus` | true | false | — | — | İç nesne [tip](../TYPES.md#t-b51613fe9868) |
| CurrAccPersonalDataConfirmations | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccPersonalDataConfirmation>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-ce9aca3be14a) |
| CurrAccTypeCode | `System.Byte` | false | true | evet | — | readonly-scalar |
| CurrAccUserWarnings | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccUserWarning>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-56b36829ba91) |
| Descriptions | `NebimV3.CurrentAccounts.CurrAccLanguageDescriptionList` | true | false | — | — | Dizi; somut satır [tip](../TYPES.md#t-f31bc69161d4) |
| DigitalChannelStockConfigurations | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.DigitalChannelStockConfiguration>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f7409baf5b10) |
| GLAccounts | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccGLAccount>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-34537a3b84a6) |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| IsIndividualAcc | `System.Boolean` | true | true | — | — | Scalar |
| MarketPlaceCode | `System.String` | true | true | — | — | Scalar |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| PersonalInfo | `NebimV3.CurrentAccounts.CurrAccPersonalInfo` | true | false | — | — | İç nesne [tip](../TYPES.md#t-906217a5b6a1) |
| PostalAddresses | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccPostalAddress>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f1a249f03cbd) |
| TaxOfficeCode | `System.String` | true | true | — | 10 | Scalar |
| TitleCode | `System.String` | true | true | — | 10 | Scalar |
| UseBankAccOnStore | `System.Boolean` | true | true | — | — | Scalar |
| AccountClosingDate | `System.DateTime` | true | true | — | — | Scalar |
| AccountOpeningDate | `System.DateTime` | true | true | — | — | Scalar |
| AgreementDate | `System.DateTime` | true | true | — | — | Scalar |
| CreditLimit | `System.Decimal` | true | true | — | — | Scalar |
| CurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| CustomerASNNumberIsRequiredForShipments | `System.Boolean` | true | true | — | — | Scalar |
| CustomerDiscountGrCode | `System.String` | true | true | — | 10 | Scalar |
| CustomerPaymentPlanGrCode | `System.String` | true | true | — | 10 | Scalar |
| CustomerPresentCards | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CustomerPresentCard>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-a98975978327) |
| CustomerPresentCardsList | `NebimV3.v3Entities.v3ElementItemList` | true | false | — | — | Dizi; somut satır çözülemedi |
| DataLanguageCode | `System.String` | true | true | — | 10 | Scalar |
| EInvoiceConfirmationRuleCode | `System.String` | true | true | — | — | Scalar |
| EInvoiceConfirmationRuleID | `System.Guid` | true | true | — | — | Scalar |
| EInvoiceStartDate | `System.DateTime` | true | true | — | — | Scalar |
| EShipmentStartDate | `System.DateTime` | true | true | — | — | Scalar |
| IdentityNum | `System.String` | true | true | — | 20 | Scalar |
| IsSendAdvertMail | `System.Nullable<System.Boolean>` | true | true | — | — | Scalar |
| IsSendAdvertSMS | `System.Nullable<System.Boolean>` | true | true | — | — | Scalar |
| IsSubjectToEInvoice | `System.Boolean` | true | true | — | — | Scalar |
| IsSubjectToEShipment | `System.Boolean` | true | true | — | — | Scalar |
| IsVIP | `System.Nullable<System.Boolean>` | true | true | — | — | Scalar |
| Patronym | `System.String` | true | true | — | 60 | Scalar |
| PaymentTerm | `System.Int16` | true | true | — | — | Scalar |
| PromotionGroupCode | `System.String` | true | true | — | 10 | Scalar |
| RetailSalePriceGroupCode | `System.String` | true | true | — | 10 | Scalar |
| Salespersons | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CustomerSalesperson>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-62857ffffdf1) |
| WholesalePriceGroupCode | `System.String` | true | true | — | 10 | Scalar |
| AllowOnlySelectedCurrency | `System.Boolean` | true | true | — | — | Scalar |
| AvailableForeignCurrencyTransList | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| BarcodeTypeCode | `System.String` | true | true | — | 20 | Scalar |
| CurrAccLotGrCode | `System.String` | true | true | — | 10 | Scalar |
| CurrAccPersonalInfo | `NebimV3.v3Entities.v3Element` | true | true | — | — | İç nesne [tip](../TYPES.md#t-e32f51689953) |
| CurrAccReconciliationContacts | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| CurrAccUBLExtensionsList | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| CurrAccUTSInformations | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccUTSInformation>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-aa366e234b05) |
| CustomerCreditLimits | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CustomerCreditLimit>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-2a9491737df0) |
| CustomerDBSAccounts | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CustomerDBSAccount>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-e9bfe1fd5076) |
| CustomerDescription | `System.String` | true | false | — | 200 | Scalar |
| CustomerMarkupGrCode | `System.String` | true | true | — | 10 | Scalar |
| CustomerOnlinePayment | `NebimV3.CurrentAccounts.CustomerOnlinePayment` | true | true | — | — | İç nesne [tip](../TYPES.md#t-ae829ae91ad8) |
| CustomerOnlinePaymentContacts | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CustomerOnlinePaymentContact>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-6f628eb5536b) |
| CustomerReconciliationContacts | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccReconciliationContact>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f3b1b71f54dd) |
| CustomerTypeCode | `System.Byte` | true | true | — | — | Scalar |
| CustomerVendorAccount | `NebimV3.CurrentAccounts.CustomerVendorAccount` | true | false | — | — | İç nesne [tip](../TYPES.md#t-dfdd6ea095a3) |
| CustomerWarehouses | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| DisableSubCurrAccWarning | `System.Boolean` | true | false | — | — | Scalar |
| DueDateFormulaCode | `System.String` | true | true | — | — | Scalar |
| ExchangeTypeCode | `System.Byte` | true | true | — | — | Scalar |
| FirstName | `System.String` | true | true | — | 60 | Scalar |
| IsArrangeCommercialInvoice | `System.Boolean` | true | true | — | — | Scalar |
| LastName | `System.String` | true | true | — | 60 | Scalar |
| MersisNum | `System.String` | true | true | — | 20 | Scalar |
| SalesChannelCode | `System.String` | true | true | — | 5 | Scalar |
| StoreHierarchyID | `System.Int32` | true | true | — | — | Scalar |
| SubCustomers | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.SubCustomer>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-a7a94452b95f) |
| TaxNumber | `System.String` | true | true | — | 20 | Scalar |
| UseDBSIntegration | `System.Boolean` | true | true | — | — | Scalar |
| UseManufacturing | `System.Boolean` | true | true | — | — | Scalar |
| UseSerialNumberTracking | `System.Boolean` | true | true | — | — | Scalar |
