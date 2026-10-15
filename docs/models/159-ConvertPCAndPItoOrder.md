[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-159"></a>

## 159 — ConvertPCAndPItoOrder / Potansiyel müşteri teklifini siparişe dönüştürme

Teklifi modelin belirttiği sipariş türüne dönüştürür. Başarı istek nesnesidir; oluşan sipariş kimliği bu yanıta eklenmez.

Somut kök: `Özel / dinamik işlem`. Grup: Özel işlemler. Örnek kanıtı: `source-operation-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.ProposalController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/ProposalService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 159,
  "ProposalNumber": "{{ProposalNumber}}",
  "OrderDate": "2026-01-01",
  "OrderTime": "00:00:00",
  "OfficeCode": "{{OfficeCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "CreateReservation": false,
  "ReApplyDiscountOffers": false,
  "PriceOption": 0
}
```

### Örnek response

Kaynakta kök istek geri döner; değerler temsili. İşlemin başarılı olduğu kanıtı değildir.

```json
{
  "ModelType": 159,
  "ProposalNumber": "{{ProposalNumber}}",
  "OrderDate": "2026-01-01",
  "OrderTime": "00:00:00",
  "OfficeCode": "{{OfficeCode}}",
  "WarehouseCode": "{{WarehouseCode}}",
  "CreateReservation": false,
  "ReApplyDiscountOffers": false,
  "PriceOption": 0
}
```

### Okuma / silme / şablon

Özel işlem için genel GetModel/Delete gövdesi uydurulmaz.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=159` → `{"ModelType":159}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

Sabit entity alan listesi yok; yukarıdaki dinamik işlem sözleşmesini kullanın.

Özel işlemde dinamik gövde esas alınır. Model163 tablosu yalnız doğrulanan baz header alanlarını,113 tablosu seçilen CustomerAttribute örneğini gösterir; selector ve özel nested gövdeler ayrıca ele alınır.
