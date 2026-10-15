[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-113"></a>

## 113 — Attribute / Dinamik özellik tanımı

ObjectName ve AttributeTypeCode ile dinamik attribute entity oluşturur. Örnekte katalogda bulunan CustomerAttribute seçilir; tip kodu kurulumda doğrulanmalıdır.

Somut kök: `Özel / dinamik işlem`. Grup: Özel işlemler. Örnek kanıtı: `source-operation-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.AttributeController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 113,
  "ObjectName": "Customer",
  "AttributeTypeCode": 1,
  "AttributeCode": "{{AttributeCode}}",
  "AttributeDescription": "ÖRNEK ÖZELLİK"
}
```

### Örnek response

CustomerAttribute için metadata temsili; ObjectName başka ise sözleşme değişir.

```json
{
  "ModelType": 113,
  "AttributeCode": "{{AttributeCode}}",
  "Description": "ÖRNEK Description",
  "AttributeDescription": "{{AttributeDescription}}",
  "Descriptions": [
    {
      "Description": "ÖRNEK Description",
      "DataLanguageCode": "TR"
    }
  ]
}
```

### Okuma / silme / şablon

Özel işlem için genel GetModel/Delete gövdesi uydurulmaz.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=113` → `{"ModelType":113}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| AttributeCode | `System.String` | true | true | evet | 20 | Scalar |
| AttributeDescription | `System.String` | true | true | — | 100 | Scalar |
| Description | `System.String` | true | true | — | 1000 | Scalar |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| Descriptions | `NebimV3.Attributes.CurrAccAttributeLanguageDescriptionList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f31bc69161d4) |

Özel işlemde dinamik gövde esas alınır. Model163 tablosu yalnız doğrulanan baz header alanlarını,113 tablosu seçilen CustomerAttribute örneğini gösterir; selector ve özel nested gövdeler ayrıca ele alınır.
