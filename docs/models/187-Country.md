[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-187"></a>

## 187 — Country / Ülke

Ülke için Ortak tanımlar grubundaki model. Somut factory tipi NebimV3.ApplicationCommon.Country. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.ApplicationCommon.Country`. Grup: Ortak tanımlar. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 187,
  "CountryCode": "{{CountryCode}}",
  "CurrencyCode": "TRY",
  "CountryDescription": "{{CountryDescription}}",
  "CountryISOCode": "{{CountryISOCode}}",
  "TaxDecCode": "{{TaxDecCode}}",
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
  "ModelType": 187,
  "CountryCode": "{{CountryCode}}",
  "CurrencyCode": "TRY",
  "CountryDescription": "{{CountryDescription}}",
  "CountryISOCode": "{{CountryISOCode}}",
  "TaxDecCode": "{{TaxDecCode}}",
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
  "ModelType": 187,
  "CountryCode": "{{CountryCode}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=187` → `{"ModelType":187}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| ApplyPCTOnSelectedPaymentTypes | `System.Boolean` | true | true | — | — | Scalar |
| CountryCode | `System.String` | true | true | evet | 10 | Scalar |
| CountryDescription | `System.String` | true | true | — | 100 | Scalar |
| CountryISOCode | `System.String` | true | true | — | 10 | Scalar |
| CurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| Descriptions | `NebimV3.ApplicationCommon.CountryLanguageDescriptionList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f31bc69161d4) |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| IsItemDim1Required | `System.Boolean` | true | true | — | — | Scalar |
| IsItemDim2Required | `System.Boolean` | true | true | — | — | Scalar |
| IsItemDim3Required | `System.Boolean` | true | true | — | — | Scalar |
| IsVatRequired | `System.Boolean` | true | true | — | — | Scalar |
| PCTApplicablePaymentTypes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.ApplicationCommon.CountryPCTApplicablePaymentTypes>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-ee899efced80) |
| TaxDecCode | `System.String` | true | true | — | 10 | Scalar |
| UseItemDim1Equ | `System.Boolean` | true | true | — | — | Scalar |
| UseItemDim2Equ | `System.Boolean` | true | true | — | — | Scalar |
| UseItemDim3Equ | `System.Boolean` | true | true | — | — | Scalar |
| UseVat | `System.Boolean` | true | true | — | — | Scalar |
