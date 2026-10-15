[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-156"></a>

## 156 — RetailReturnPayment / Perakende iade ödemesi

Perakende iade ödemesi. Payments burada boş şema yeridir; ödeme türüne göre somut satır alanları ayrıca gerekir.

Somut kök: `Özel / dinamik işlem`. Grup: Özel işlemler. Örnek kanıtı: `source-operation-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 156,
  "CustomerTypeCode": 4,
  "CustomerCode": "{{CustomerCode}}",
  "PaymentHeaderID": "{{exampleGuid}}",
  "POSTerminalID": 0,
  "Payments": []
}
```

### Örnek response

Kaynakta kök istek geri döner; değerler temsili. İşlemin başarılı olduğu kanıtı değildir.

```json
{
  "ModelType": 156,
  "CustomerTypeCode": 4,
  "CustomerCode": "{{CustomerCode}}",
  "PaymentHeaderID": "{{exampleGuid}}",
  "POSTerminalID": 0,
  "Payments": []
}
```

### Okuma / silme / şablon

Özel işlem için genel GetModel/Delete gövdesi uydurulmaz.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=156` → `{"ModelType":156}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

Sabit entity alan listesi yok; yukarıdaki dinamik işlem sözleşmesini kullanın.

Özel işlemde dinamik gövde esas alınır. Model163 tablosu yalnız doğrulanan baz header alanlarını,113 tablosu seçilen CustomerAttribute örneğini gösterir; selector ve özel nested gövdeler ayrıca ele alınır.
