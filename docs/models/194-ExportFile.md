[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-194"></a>

## 194 — ExportFile / İhracat dosyası

İhracat dosyası için İthalat/ihracat grubundaki model. Somut factory tipi NebimV3.ImportExport.ExportFile. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.ImportExport.ExportFile`. Grup: İthalat/ihracat. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 194,
  "ExportFileNumber": "{{ExportFileNumber}}",
  "CurrAccCode": "{{CurrAccCode}}",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "ClosingDate": "2026-01-01T00:00:00",
  "CurrAccTypeCode": 0,
  "Descriptions": [
    {
      "Description": "ÖRNEK Description",
      "DataLanguageCode": "TR",
      "DataLanguageDescription": "{{DataLanguageDescription}}"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 194,
  "ExportFileNumber": "{{ExportFileNumber}}",
  "CurrAccCode": "{{CurrAccCode}}",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "ClosingDate": "2026-01-01T00:00:00",
  "CurrAccTypeCode": 0,
  "Descriptions": [
    {
      "Description": "ÖRNEK Description",
      "DataLanguageCode": "TR"
    }
  ]
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 194,
  "ExportFileNumber": "{{ExportFileNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=194` → `{"ModelType":194}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| AttributeList | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| Attributes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.ImportExport.AttributeExportFile>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-e21798d9c305) |
| ClosingDate | `System.DateTime` | true | true | — | — | Scalar |
| CompanyCode | `System.Decimal` | true | true | — | — | Scalar |
| CurrAccCode | `System.String` | true | true | — | 30 | Scalar |
| CurrAccTypeCode | `System.Byte` | true | true | — | — | Scalar |
| CustomsCompanyCode | `System.String` | true | true | — | 10 | Scalar |
| CustomsOfficesCode | `System.String` | true | true | — | 10 | Scalar |
| Descriptions | `NebimV3.ImportExport.ExportFileLanguageDescriptionList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f31bc69161d4) |
| ExportFileDescription | `System.String` | true | true | — | 100 | Scalar |
| ExportFileIndirectExpenses | `NebimV3.v3Entities.v3ElementItemList<NebimV3.ImportExport.ExportFileIndirectExpense>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-a3cecf58ea2e) |
| ExportFileInsurances | `NebimV3.v3Entities.v3ElementItemList<NebimV3.ImportExport.ExportFileInsurance>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-783d96da452e) |
| ExportFileNumber | `System.String` | true | true | evet | 30 | Scalar |
| ExportFileShippingInfos | `NebimV3.v3Entities.v3ElementItemList<NebimV3.ImportExport.ExportFileShippingInfo>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-50d880a2ef9c) |
| ExportFileStatusHistorys | `NebimV3.v3Entities.v3ElementItemList<NebimV3.ImportExport.ExportFileStatusHistory>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-0eb4f8dd091c) |
| ExtraNumber1 | `System.String` | true | true | — | 30 | Scalar |
| ExtraNumber2 | `System.String` | true | true | — | 30 | Scalar |
| IncotermCode1 | `System.String` | true | true | — | 5 | Scalar |
| IncotermCode2 | `System.String` | true | true | — | 5 | Scalar |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| IsClosed | `System.Boolean` | true | true | — | — | Scalar |
| LettersOfCreditNumber | `System.String` | true | true | — | 30 | Scalar |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| PaymentMeansCode | `System.String` | true | true | — | — | Scalar |
| PaymentMethodCode | `System.String` | true | true | — | 20 | Scalar |
| StartDate | `System.DateTime` | true | true | — | — | Scalar |
