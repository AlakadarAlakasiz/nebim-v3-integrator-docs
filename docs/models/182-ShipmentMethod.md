[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-182"></a>

## 182 — ShipmentMethod / Sevkiyat yöntemi

Sevkiyat yöntemi için Stok işlem tanımları grubundaki model. Somut factory tipi NebimV3.ItemTransactions.ShipmentMethod. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.ItemTransactions.ShipmentMethod`. Grup: Stok işlem tanımları. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.ShipmentController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 182,
  "ShipmentMethodCode": "{{ShipmentMethodCode}}",
  "ShipmentMethodDescription": "{{ShipmentMethodDescription}}",
  "TransportModeCode": "{{TransportModeCode}}",
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
  "ModelType": 182,
  "ShipmentMethodCode": "{{ShipmentMethodCode}}",
  "ShipmentMethodDescription": "{{ShipmentMethodDescription}}",
  "TransportModeCode": "{{TransportModeCode}}",
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
  "ModelType": 182,
  "ShipmentMethodCode": "{{ShipmentMethodCode}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=182` → `{"ModelType":182}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| Descriptions | `NebimV3.ItemTransactions.ShipmentMethodLanguageDescriptionList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f31bc69161d4) |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| ShipmentMethodCode | `System.String` | true | true | evet | 10 | Scalar |
| ShipmentMethodDescription | `System.String` | true | true | — | 100 | Scalar |
| TransportModeCode | `System.String` | true | true | — | — | Scalar |
