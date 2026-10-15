[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-31"></a>

## 31 — Employee / Personel

Personel için Cari hesaplar grubundaki model. Somut factory tipi NebimV3.CurrentAccounts.Employee. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.CurrentAccounts.Employee`. Grup: Cari hesaplar. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.EmployeeController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 31,
  "CurrAccCode": "{{CurrAccCode}}",
  "FirstName": "ÖRNEK FirstName",
  "LastName": "ÖRNEK LastName",
  "CurrAccDescription": "ÖRNEK CurrAccDescription",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
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
  "ModelType": 31,
  "CurrAccCode": "{{CurrAccCode}}",
  "CurrAccTypeCode": 0,
  "FirstName": "ÖRNEK FirstName",
  "LastName": "ÖRNEK LastName",
  "CurrAccDescription": "ÖRNEK CurrAccDescription",
  "OfficeCode": "{{OfficeCode}}",
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
  "ModelType": 31,
  "CurrAccCode": "{{CurrAccCode}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=31` → `{"ModelType":31}`.

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
| Contacts | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.EmployeeContact>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-3cc2ddbe4013) |
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
| PersonalInfo | `NebimV3.CurrentAccounts.CurrAccPersonalInfo` | true | true | — | — | İç nesne [tip](../TYPES.md#t-906217a5b6a1) |
| PostalAddresses | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CurrAccPostalAddress>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f1a249f03cbd) |
| TaxOfficeCode | `System.String` | true | true | — | — | Scalar |
| TitleCode | `System.String` | true | true | — | 10 | Scalar |
| UseBankAccOnStore | `System.Boolean` | true | true | — | — | Scalar |
| CreditLimit | `System.Decimal` | true | true | — | — | Scalar |
| DataLanguageCode | `System.String` | true | true | — | 10 | Scalar |
| Educations | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.EmployeeEducation>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-fcabc4a9f5eb) |
| EmployeeDocuments | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.EmployeeDocument>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-4f4eeae3020e) |
| FirstName | `System.String` | true | true | — | 60 | Scalar |
| ForeignLanguages | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.EmployeeForeignLanguage>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-2bd7278f4a04) |
| IdentityNum | `System.String` | true | true | — | 20 | Scalar |
| LastName | `System.String` | true | true | — | 60 | Scalar |
| PrevJobs | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.EmployeePrevJob>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-73937ace265c) |
| Records | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.EmployeeRecord>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-0d16a2c12140) |
| RetailSalePriceGroupCode | `System.String` | true | true | — | 10 | Scalar |
| Softwares | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.EmployeeSoftware>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-0128604b9cbd) |
| WholesalePriceGroupCode | `System.String` | true | true | — | 10 | Scalar |
| BankAccNo | `System.String` | true | true | — | 20 | Scalar |
| BankBranchCode | `System.String` | true | true | — | 20 | Scalar |
| BankCode | `System.String` | true | true | — | 10 | Scalar |
| CanDeleteSGKEmployeeJobStartDeclaration | `System.Boolean` | true | true | — | — | Scalar |
| CostCenterCode | `System.String` | true | true | — | 20 | Scalar |
| CustomerDiscountGrCode | `System.String` | true | true | — | 10 | Scalar |
| CustomerPaymentPlanGrCode | `System.String` | true | true | — | 10 | Scalar |
| CustomerPresentCards | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.CustomerPresentCard>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-a98975978327) |
| CustomerPresentCardsList | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| EmployeeDescription | `System.String` | true | true | — | 200 | Scalar |
| EmployeeLeaveDays | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.EmployeeLeaveDay>` | true | false | — | — | Dizi; somut satır [tip](../TYPES.md#t-ad5301d936fe) |
| EmployeeLeaveHours | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.EmployeeLeaveHour>` | true | false | — | — | Dizi; somut satır [tip](../TYPES.md#t-43501fbfd638) |
| EmployeeLeaveRequestHours | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.EmployeeLeaveRequestHour>` | true | false | — | — | Dizi; somut satır [tip](../TYPES.md#t-00b4af045b02) |
| EmployeeLeaveRequests | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.EmployeeLeaveRequest>` | true | false | — | — | Dizi; somut satır [tip](../TYPES.md#t-26648165f0ec) |
| ExchangeTypeCode | `System.Byte` | true | true | — | — | Scalar |
| IBAN | `System.String` | true | true | — | 40 | Scalar |
| IsCurrAccConfirmed | `System.Nullable<System.Boolean>` | true | true | — | — | Scalar |
| IsSendAdvertMail | `System.Nullable<System.Boolean>` | true | true | — | — | Scalar |
| IsSendAdvertSMS | `System.Nullable<System.Boolean>` | true | true | — | — | Scalar |
| JobTrainings | `NebimV3.v3Entities.v3ElementItemList<NebimV3.CurrentAccounts.EmployeeJobTraining>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-fa4e27533f18) |
| PensionBankAccNo | `System.String` | true | true | — | 20 | Scalar |
| PensionBankBranchCode | `System.String` | true | true | — | 20 | Scalar |
| PensionBankCode | `System.String` | true | true | — | 10 | Scalar |
| PensionIBAN | `System.String` | true | true | — | 40 | Scalar |
| PromotionGroupCode | `System.String` | true | true | — | 10 | Scalar |
| SWIFTCode | `System.String` | true | true | — | 20 | Scalar |
| ShoppingLimit | `NebimV3.CurrentAccounts.EmployeeShoppingLimit` | true | true | — | — | İç nesne [tip](../TYPES.md#t-6d23b84a4109) |
