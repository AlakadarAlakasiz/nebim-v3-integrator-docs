[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-190"></a>

## 190 — District / İlçe

İlçe için Ortak tanımlar grubundaki model. Somut factory tipi NebimV3.ApplicationCommon.District. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.ApplicationCommon.District`. Grup: Ortak tanımlar. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 190,
  "DistrictCode": "{{DistrictCode}}",
  "CityCode": "{{CityCode}}",
  "DistrictDescription": "{{DistrictDescription}}",
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
  "ModelType": 190,
  "DistrictCode": "{{DistrictCode}}",
  "CityCode": "{{CityCode}}",
  "DistrictDescription": "{{DistrictDescription}}",
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
  "ModelType": 190,
  "DistrictCode": "{{DistrictCode}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=190` → `{"ModelType":190}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| CityCode | `System.String` | true | true | — | 10 | Scalar |
| Descriptions | `NebimV3.ApplicationCommon.DistrictLanguageDescriptionList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f31bc69161d4) |
| DistrictCode | `System.String` | true | true | evet | 30 | Scalar |
| DistrictDescription | `System.String` | true | true | — | 100 | Scalar |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| MapLocation | `NebimV3.v3Entities.v3Element` | true | true | — | — | İç nesne [tip](../TYPES.md#t-e32f51689953) |
| QuarterList | `NebimV3.v3Entities.v3EntityList<NebimV3.ApplicationCommon.Quarter>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-a6b99700ad16) |
