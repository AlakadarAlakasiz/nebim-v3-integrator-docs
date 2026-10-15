[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-70"></a>

## 70 — LinkProduct / Ürün bağlama

Ürün bağlama/bağlantı kaldırma işlemi. ITAttributes içindeki ITAttNN alanları kurulumdaki özellik tiplerinden gelir; örnekte uydurulmaz.

Somut kök: `Özel / dinamik işlem`. Grup: Özel işlemler. Örnek kanıtı: `source-operation-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.InnerController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/InnerService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 70,
  "OperationDate": "2026-01-01",
  "OperationTime": "00:00:00",
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "InWarehouseCode": "{{InWarehouseCode}}",
  "OutWarehouseCode": "{{OutWarehouseCode}}",
  "ProductCode": "{{ProductCode}}",
  "Qty1": 1,
  "ITAttributes": {}
}
```

### Örnek response

Kaynakta kök istek geri döner; değerler temsili. İşlemin başarılı olduğu kanıtı değildir.

```json
{
  "ModelType": 70,
  "OperationDate": "2026-01-01",
  "OperationTime": "00:00:00",
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "InWarehouseCode": "{{InWarehouseCode}}",
  "OutWarehouseCode": "{{OutWarehouseCode}}",
  "ProductCode": "{{ProductCode}}",
  "Qty1": 1,
  "ITAttributes": {}
}
```

### Okuma / silme / şablon

Özel işlem için genel GetModel/Delete gövdesi uydurulmaz.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=70` → `{"ModelType":70}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

Sabit entity alan listesi yok; yukarıdaki dinamik işlem sözleşmesini kullanın.

Özel işlemde dinamik gövde esas alınır. Model163 tablosu yalnız doğrulanan baz header alanlarını,113 tablosu seçilen CustomerAttribute örneğini gösterir; selector ve özel nested gövdeler ayrıca ele alınır.
