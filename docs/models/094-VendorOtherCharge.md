[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-94"></a>

## 94 — VendorOtherCharge / Tedarikçi ek masrafı

Tedarikçi ek masrafı için Ödemeler grubundaki model. Somut factory tipi NebimV3.Payments.VendorOtherCharge. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Payments.VendorOtherCharge`. Grup: Ödemeler. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.DebitController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 94,
  "CurrAccCode": "{{CurrAccCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "IsReturn": false,
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "DocumentNumber": "{{DocumentNumber}}",
  "RefNumber": "{{RefNumber}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "Description": "ÖRNEK Description",
      "DocCurrencyCode": "TRY",
      "DueDate": "2026-01-01T00:00:00",
      "DocumentNumber": "{{DocumentNumber}}",
      "CreditAmount": 0
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 94,
  "HeaderID": "{{exampleGuid}}",
  "CurrAccCode": "{{CurrAccCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "IsReturn": false,
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "DocumentNumber": "{{DocumentNumber}}",
  "RefNumber": "{{RefNumber}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "Description": "ÖRNEK Description",
      "DocCurrencyCode": "TRY",
      "DueDate": "2026-01-01T00:00:00",
      "DocumentNumber": "{{DocumentNumber}}",
      "CreditAmount": 0
    }
  ]
}
```

### Okuma / silme / şablon

Yazılabilir anahtar yok; kaynak LoadEntity normal setter yolundan aday belge numarası gösterilir. Model bazında yükleme akışı doğrulanmış değildir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 94,
  "DocumentNumber": "{{DocumentNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=94` → `{"ModelType":94}`.

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
| Lines | `NebimV3.Payments.DebitLineList<NebimV3.Payments.DebitLine>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-e554601ab444) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| ATAttributes | `NebimV3.Payments.DebitATAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-1544f74bd248) |
| BaseApplicationCode | `System.String` | true | true | — | — | Scalar |
| BaseApplicationID | `System.Guid` | true | true | — | — | Scalar |
| ContactID | `System.Guid` | true | true | — | — | Scalar |
| CurrAccCode | `System.String` | true | true | — | 30 | Scalar |
| CurrAccTypeCode | `System.Byte` | true | true | — | — | Scalar |
| DebitNumber | `System.String` | true | true | — | — | Scalar |
| DebitTypeCode | `NebimV3.Payments.DebitTypes` | true | true | — | — | Scalar |
| Description | `System.String` | true | true | — | 200 | Scalar |
| DocCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| DocumentDate | `System.DateTime` | true | true | — | — | Scalar |
| DocumentNumber | `System.String` | true | true | — | 30 | Scalar |
| DocumentTime | `System.TimeSpan` | true | true | — | — | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| ExportFileNumber | `System.String` | true | true | — | — | Scalar |
| GLTypeCode | `System.String` | true | true | — | 20 | Scalar |
| ImportFileNumber | `System.String` | true | true | — | — | Scalar |
| InvoiceDescription | `System.String` | true | true | — | — | Scalar |
| InvoiceInternalDescription | `System.String` | true | true | — | — | Scalar |
| IsDiffCurrencyEachLine | `System.Boolean` | true | true | — | — | Scalar |
| IsForeignCurrencyTransaction | `System.Boolean` | true | true | — | — | Scalar |
| IsReturn | `System.Boolean` | true | true | — | — | Scalar |
| LocalCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| RefNumber | `System.String` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| SubCurrAccID | `System.Guid` | true | true | — | — | Scalar |
