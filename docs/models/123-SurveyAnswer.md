[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-123"></a>

## 123 — SurveyAnswer / Anket yanıtı

Anket yanıtı için Anketler grubundaki model. Somut factory tipi NebimV3.Surveys.SurveyAnswer. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Surveys.SurveyAnswer`. Grup: Anketler. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.SurveyController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 123,
  "SurveyAnswerHeaderID": "{{exampleGuid}}",
  "CurrAccCode": "{{CurrAccCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "ApplicationCode": "{{ApplicationCode}}",
  "ApplicationID": "{{exampleGuid}}",
  "ContactID": "{{exampleGuid}}",
  "Lines": [
    {
      "SurveyAnswerLineID": "{{exampleGuid}}",
      "Description": "ÖRNEK Description",
      "AnswerDate": "2026-01-01T00:00:00",
      "AnswerNumeric": 0,
      "AnswerText": "{{AnswerText}}",
      "DescriptionForNo": "{{DescriptionForNo}}"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 123,
  "SurveyAnswerHeaderID": "{{exampleGuid}}",
  "CurrAccCode": "{{CurrAccCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "ApplicationCode": "{{ApplicationCode}}",
  "ApplicationID": "{{exampleGuid}}",
  "ContactID": "{{exampleGuid}}",
  "Lines": [
    {
      "SurveyAnswerLineID": "{{exampleGuid}}",
      "Description": "ÖRNEK Description",
      "AnswerDate": "2026-01-01T00:00:00",
      "AnswerNumeric": 0,
      "AnswerText": "{{AnswerText}}",
      "DescriptionForNo": "{{DescriptionForNo}}"
    }
  ]
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 123,
  "SurveyAnswerHeaderID": "{{exampleGuid}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=123` → `{"ModelType":123}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| ApplicationCode | `System.String` | true | true | — | — | Scalar |
| ApplicationID | `System.Guid` | true | true | — | — | Scalar |
| ContactID | `System.Guid` | true | true | — | — | Scalar |
| CurrAccCode | `System.String` | true | true | — | 30 | Scalar |
| CurrAccTypeCode | `System.Byte` | true | true | — | — | Scalar |
| DocumentDate | `System.DateTime` | true | true | — | — | Scalar |
| DocumentTime | `System.TimeSpan` | true | true | — | — | Scalar |
| IsCompleted | `System.Boolean` | true | true | — | — | Scalar |
| IsLocked | `System.Boolean` | true | true | — | — | Scalar |
| Lines | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Surveys.SurveyAnswerLine>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-3998360e5f72) |
| SurveyAnswerHeaderID | `System.Guid` | true | true | evet | — | Scalar |
| SurveyCode | `System.String` | true | true | — | 10 | Scalar |
