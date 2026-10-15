[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-1"></a>

## 1 — Login / Nebim kullanıcısıyla giriş

Nebim kullanıcısını doğrular ve token oluşturur. Validate=true ile giriş doğrulanmalıdır; session/auto-login davranışı kuruluma bağlıdır.

Somut kök: `Özel / dinamik işlem`. Grup: Giriş ve oturum. Örnek kanıtı: `source-operation-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Connect`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 1,
  "DatabaseName": "{{DatabaseName}}",
  "UserGroupCode": "{{UserGroupCode}}",
  "UserName": "{{UserName}}",
  "Password": "{{Password}}",
  "Validate": true
}
```

### Örnek response

Giriş başarı biçimi; token yer tutucudur.

```json
{
  "Status": "Connection Created Successfully",
  "StatusCode": 200,
  "Token": "{{token}}"
}
```

### Okuma / silme / şablon

Özel işlem için genel GetModel/Delete gövdesi uydurulmaz.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=1` → `{"ModelType":1}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

Sabit entity alan listesi yok; yukarıdaki dinamik işlem sözleşmesini kullanın.

Özel işlemde dinamik gövde esas alınır. Model163 tablosu yalnız doğrulanan baz header alanlarını,113 tablosu seçilen CustomerAttribute örneğini gösterir; selector ve özel nested gövdeler ayrıca ele alınır.
