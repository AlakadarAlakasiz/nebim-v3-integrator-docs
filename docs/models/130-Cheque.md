[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-130"></a>

## 130 — Cheque / Alınan çek

Alınan çek için Çek, senet ve teminatlar grubundaki model. Somut factory tipi NebimV3.Cheques.ChequeReceived. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Cheques.ChequeReceived`. Grup: Çek, senet ve teminatlar. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 130,
  "BankBranchCode": "{{BankBranchCode}}",
  "BankCode": "{{BankCode}}",
  "ChequeCode": "{{ChequeCode}}",
  "ChequeTypeCode": 0,
  "CurrAccCode": "{{CurrAccCode}}",
  "CompanyCode": 1,
  "CurrencyCode": "TRY",
  "CityCode": "{{CityCode}}",
  "DistrictCode": "{{DistrictCode}}",
  "Amount": 1,
  "DueDate": "2026-01-01T00:00:00",
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
  "ModelType": 130,
  "BankBranchCode": "{{BankBranchCode}}",
  "BankCode": "{{BankCode}}",
  "ChequeCode": "{{ChequeCode}}",
  "ChequeTypeCode": 0,
  "CurrAccCode": "{{CurrAccCode}}",
  "CompanyCode": 1,
  "CurrencyCode": "TRY",
  "CityCode": "{{CityCode}}",
  "DistrictCode": "{{DistrictCode}}",
  "Amount": 1,
  "DueDate": "2026-01-01T00:00:00",
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
  "ModelType": 130,
  "BankBranchCode": "{{BankBranchCode}}",
  "BankCode": "{{BankCode}}",
  "ChequeCode": "{{ChequeCode}}",
  "ChequeTypeCode": 0
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=130` → `{"ModelType":130}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| Amount | `System.Decimal` | true | true | — | — | Scalar |
| BankAccNo | `System.String` | true | true | — | 30 | Scalar |
| BankBranchCode | `System.String` | true | true | evet | 20 | Scalar |
| BankCode | `System.String` | true | true | evet | 10 | Scalar |
| ChequeCode | `System.String` | true | true | evet | 30 | Scalar |
| ChequeDescription | `System.String` | true | true | — | 100 | Scalar |
| ChequeTypeCode | `System.Byte` | true | true | evet | — | Scalar |
| CityCode | `System.String` | true | true | — | 10 | Scalar |
| ClosingDate | `System.DateTime` | true | true | — | — | Scalar |
| CompanyCode | `System.Decimal` | true | true | — | — | Scalar |
| CurrAccCode | `System.String` | true | true | — | 30 | Scalar |
| CurrAccTypeCode | `System.Byte` | true | true | — | — | Scalar |
| CurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| Descriptions | `NebimV3.Cheques.ChequeLanguageDescriptionList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f31bc69161d4) |
| DistrictCode | `System.String` | true | true | — | 30 | Scalar |
| Drawer | `System.String` | true | true | — | 100 | Scalar |
| DueDate | `System.DateTime` | true | true | — | — | Scalar |
| ExtraNumber1 | `System.String` | true | true | — | 30 | Scalar |
| ExtraNumber2 | `System.String` | true | true | — | 30 | Scalar |
| IBAN | `System.String` | true | true | — | 40 | Scalar |
| IdentityNum | `System.String` | true | true | — | 20 | Scalar |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| IsClosed | `System.Boolean` | true | true | — | — | Scalar |
| IsEndorsed | `System.Boolean` | true | true | — | — | Scalar |
| IsIndividualAcc | `System.Boolean` | true | true | — | — | Scalar |
| OrganizedDate | `System.DateTime` | true | true | — | — | Scalar |
| TaxNumber | `System.String` | true | true | — | 20 | Scalar |
| TaxOfficeCode | `System.String` | true | true | — | 10 | Scalar |
| AttributeList | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| Attributes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Cheques.ChequeReceivedAttribute>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-354987818407) |
