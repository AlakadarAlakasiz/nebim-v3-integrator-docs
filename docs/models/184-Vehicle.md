[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-184"></a>

## 184 — Vehicle / Araç

Araç için Ortak tanımlar grubundaki model. Somut factory tipi NebimV3.ApplicationCommon.Vehicle. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.ApplicationCommon.Vehicle`. Grup: Ortak tanımlar. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.ShipmentController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 184,
  "VehicleCode": "{{VehicleCode}}",
  "Description": "ÖRNEK Description",
  "Brand": "{{Brand}}",
  "LicensePlate": "{{LicensePlate}}",
  "MaxVolume": 0,
  "MaxWeight": 0
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 184,
  "VehicleCode": "{{VehicleCode}}",
  "Description": "ÖRNEK Description",
  "Brand": "{{Brand}}",
  "LicensePlate": "{{LicensePlate}}",
  "MaxVolume": 0,
  "MaxWeight": 0
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 184,
  "VehicleCode": "{{VehicleCode}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=184` → `{"ModelType":184}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| Brand | `System.String` | true | true | — | 30 | Scalar |
| Description | `System.String` | true | true | — | 100 | Scalar |
| Drivers | `NebimV3.v3Entities.v3ElementItemList<NebimV3.ApplicationCommon.VehicleDrivers>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-847b663ae9e8) |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| LicensePlate | `System.String` | true | true | — | 20 | Scalar |
| MaxVolume | `System.Double` | true | true | — | — | Scalar |
| MaxWeight | `System.Double` | true | true | — | — | Scalar |
| Model | `System.String` | true | true | — | 30 | Scalar |
| VehicleCode | `System.String` | true | true | evet | 10 | Scalar |
| VehicleTypeCode | `System.String` | true | true | — | 10 | Scalar |
