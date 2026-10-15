[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-208"></a>

## 208 — OnlineInstallmentPayment / Çevrimiçi taksit ödemesi

Taksit ödemesini ve varsa Invoice nesnesini işler. Alt Payment/Invoice için tam ilgili model gerekir; örnek dış sarmalı gösterir.

Somut kök: `Özel / dinamik işlem`. Grup: Özel işlemler. Örnek kanıtı: `source-operation-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 208,
  "Payment": {
    "ModelType": 45,
    "DebitLines": [],
    "Payments": []
  }
}
```

### Örnek response

Kaynak, kök isteğe Payment.PaymentHeaderID ekler. Invoice verilirse Invoice.InvoiceHeaderID de eklenir; alt gövdeler örnekte tamamlanmış değildir.

```json
{
  "ModelType": 208,
  "Payment": {
    "ModelType": 45,
    "DebitLines": [],
    "Payments": [],
    "PaymentHeaderID": "{{exampleGuid}}"
  }
}
```

### Okuma / silme / şablon

Özel işlem için genel GetModel/Delete gövdesi uydurulmaz.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=208` → `{"ModelType":208}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

Sabit entity alan listesi yok; yukarıdaki dinamik işlem sözleşmesini kullanın.

Özel işlemde dinamik gövde esas alınır. Model163 tablosu yalnız doğrulanan baz header alanlarını,113 tablosu seçilen CustomerAttribute örneğini gösterir; selector ve özel nested gövdeler ayrıca ele alınır.
