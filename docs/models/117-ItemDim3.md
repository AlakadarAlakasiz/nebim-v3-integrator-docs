[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-117"></a>

## 117 — ItemDim3 / Üçüncü ürün boyutu

Üçüncü ürün boyutu için Ürün ve tanımlar grubundaki model. Somut factory tipi NebimV3.Items.ItemDim3. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Items.ItemDim3`. Grup: Ürün ve tanımlar. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 117,
  "ItemDim3Code": "{{ItemDim3Code}}",
  "ItemDimType1": "{{ItemDimType1}}",
  "ItemDimType10": "{{ItemDimType10}}",
  "ItemDimType2": "{{ItemDimType2}}",
  "ItemDimType3": "{{ItemDimType3}}",
  "ItemDimType4": "{{ItemDimType4}}"
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 117,
  "ItemDim3Code": "{{ItemDim3Code}}",
  "ItemDimType1": "{{ItemDimType1}}",
  "ItemDimType10": "{{ItemDimType10}}",
  "ItemDimType2": "{{ItemDimType2}}",
  "ItemDimType3": "{{ItemDimType3}}",
  "ItemDimType4": "{{ItemDimType4}}"
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 117,
  "ItemDim3Code": "{{ItemDim3Code}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=117` → `{"ModelType":117}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| DimEques | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Items.ItemDim3Equ>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-5ca58f317d8e) |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| ItemDim3Code | `System.String` | true | true | evet | 10 | Scalar |
| ItemDimType1 | `System.String` | true | true | — | 20 | Scalar |
| ItemDimType10 | `System.String` | true | true | — | 20 | Scalar |
| ItemDimType2 | `System.String` | true | true | — | 20 | Scalar |
| ItemDimType3 | `System.String` | true | true | — | 20 | Scalar |
| ItemDimType4 | `System.String` | true | true | — | 20 | Scalar |
| ItemDimType5 | `System.String` | true | true | — | 20 | Scalar |
| ItemDimType6 | `System.String` | true | true | — | 20 | Scalar |
| ItemDimType7 | `System.String` | true | true | — | 20 | Scalar |
| ItemDimType8 | `System.String` | true | true | — | 20 | Scalar |
| ItemDimType9 | `System.String` | true | true | — | 20 | Scalar |
| SortOrder | `System.Int16` | true | true | — | — | Scalar |
