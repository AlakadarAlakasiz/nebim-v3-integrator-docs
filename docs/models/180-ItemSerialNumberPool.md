[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-180"></a>

## 180 — ItemSerialNumberPool / Ürün seri numarası havuzu

Ürün seri numarası havuzu için Ürün ve tanımlar grubundaki model. Somut factory tipi NebimV3.Items.ItemSerialNumberPool. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Items.ItemSerialNumberPool`. Grup: Ürün ve tanımlar. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 180,
  "SerialNumber": "{{SerialNumber}}",
  "ItemCode": "{{ItemCode}}",
  "ItemTypeCode": 1,
  "ColorCode": "{{ColorCode}}",
  "ItemDim1Code": "{{ItemDim1Code}}",
  "ItemDim2Code": "{{ItemDim2Code}}",
  "ItemDim3Code": "{{ItemDim3Code}}"
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 180,
  "SerialNumber": "{{SerialNumber}}",
  "ItemCode": "{{ItemCode}}",
  "ItemTypeCode": 1,
  "ColorCode": "{{ColorCode}}",
  "ItemDim1Code": "{{ItemDim1Code}}",
  "ItemDim2Code": "{{ItemDim2Code}}",
  "ItemDim3Code": "{{ItemDim3Code}}"
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 180,
  "SerialNumber": "{{SerialNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=180` → `{"ModelType":180}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| ColorCode | `System.String` | true | true | — | 10 | Scalar |
| ItemCode | `System.String` | true | true | — | 30 | Scalar |
| ItemDim1Code | `System.String` | true | true | — | 10 | Scalar |
| ItemDim2Code | `System.String` | true | true | — | 10 | Scalar |
| ItemDim3Code | `System.String` | true | true | — | 10 | Scalar |
| ItemTypeCode | `System.Byte` | true | true | — | — | Scalar |
| SerialNumber | `System.String` | true | true | evet | — | Scalar |
