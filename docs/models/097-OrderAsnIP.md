[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-97"></a>

## 97 — OrderAsnIP / İthalat alış sipariş ASN bildirimi

İthalat alış sipariş ASN bildirimi için Sevkiyat ve irsaliyeler grubundaki model. Somut factory tipi NebimV3.Shipments.ImportPurchaseAsn. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Shipments.ImportPurchaseAsn`. Grup: Sevkiyat ve irsaliyeler. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.ShipmentController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 97,
  "VendorCode": "{{VendorCode}}",
  "InvoiceNumber": "{{InvoiceNumber}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "IsReturn": false,
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
      "Qty2": 0
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 97,
  "HeaderID": "{{exampleGuid}}",
  "VendorCode": "{{VendorCode}}",
  "InvoiceNumber": "{{InvoiceNumber}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "IsReturn": false,
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
  "ModelType": 97,
  "InvoiceNumber": "{{InvoiceNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=97` → `{"ModelType":97}`.

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
| Lines | `NebimV3.Shipments.OrderAsnPurchaseLineList<NebimV3.Shipments.ImportPurchaseAsnLine>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-81b8887e97f2) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| SetDefaultLotForItem | `System.Boolean` | true | true | — | — | Scalar |
| ActualDateOfArrival | `System.DateTime` | true | true | — | — | Scalar |
| BillOfLadingNumber | `System.String` | true | true | — | 30 | Scalar |
| ContactID | `System.Guid` | true | true | — | — | Scalar |
| ContainerNumber | `System.String` | true | true | — | 30 | Scalar |
| ContainerTypeCode | `System.String` | true | true | — | 10 | Scalar |
| DateOfLading | `System.DateTime` | true | true | — | — | Scalar |
| DateOfNationalization | `System.DateTime` | true | true | — | — | Scalar |
| DeliveryCompanyCode | `System.String` | true | true | — | 10 | Scalar |
| DepartureCountryCode | `System.String` | true | true | — | 10 | Scalar |
| Description | `System.String` | true | true | — | 200 | Scalar |
| DischargePortCode | `System.String` | true | true | — | 30 | Scalar |
| EstimatedDateOfArrival | `System.DateTime` | true | true | — | — | Scalar |
| GrossWeight | `System.Double` | true | true | — | — | Scalar |
| ImportFileNumber | `System.String` | true | true | — | 30 | Scalar |
| InvoiceNumber | `System.String` | true | true | — | 30 | Scalar |
| IsReturn | `System.Boolean` | true | true | — | — | Scalar |
| LadingPortCode | `System.String` | true | true | — | 30 | Scalar |
| LettersOfCreditNumber | `System.String` | true | true | — | 30 | Scalar |
| NameOfShip | `System.String` | true | true | — | 30 | Scalar |
| NetWeight | `System.Double` | true | true | — | — | Scalar |
| OrderAsnDate | `System.DateTime` | true | true | — | — | Scalar |
| OrderAsnNumber | `System.String` | true | true | — | 30 | Scalar |
| OrderAsnTime | `System.TimeSpan` | true | true | — | — | Scalar |
| PortOfDischarge | `System.String` | true | true | — | 30 | Scalar |
| PortOfLading | `System.String` | true | true | — | 30 | Scalar |
| ShipmentMethodCode | `System.String` | true | true | — | 10 | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| SubCurrAccID | `System.Guid` | true | true | — | — | Scalar |
| TotalCBM | `System.Double` | true | true | — | — | Scalar |
| TotalCHW | `System.Double` | true | true | — | — | Scalar |
| TotalPackage | `System.Int32` | true | true | — | — | Scalar |
| WarehouseCode | `System.String` | true | true | — | 10 | Scalar |
| VendorCode | `System.String` | true | true | — | 30 | Scalar |
| IncotermCode1 | `System.String` | true | true | — | 5 | Scalar |
| IncotermCode2 | `System.String` | true | true | — | 5 | Scalar |
