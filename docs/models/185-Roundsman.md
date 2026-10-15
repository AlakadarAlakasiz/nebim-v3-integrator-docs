[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-185"></a>

## 185 — Roundsman / Dağıtım görevlisi

Dağıtım görevlisi için Stok işlem tanımları grubundaki model. Somut factory tipi NebimV3.ItemTransactions.Roundsman. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.ItemTransactions.Roundsman`. Grup: Stok işlem tanımları. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.ShipmentController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 185,
  "RoundsmanCode": "{{RoundsmanCode}}",
  "EmployeeCode": "{{EmployeeCode}}",
  "FirstName": "ÖRNEK FirstName",
  "LastName": "ÖRNEK LastName",
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}"
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 185,
  "RoundsmanCode": "{{RoundsmanCode}}",
  "EmployeeCode": "{{EmployeeCode}}",
  "FirstName": "ÖRNEK FirstName",
  "LastName": "ÖRNEK LastName",
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}"
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 185,
  "RoundsmanCode": "{{RoundsmanCode}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=185` → `{"ModelType":185}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| EmployeeCode | `System.String` | true | true | — | 30 | Scalar |
| FirstName | `System.String` | true | true | — | 20 | Scalar |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| LastName | `System.String` | true | true | — | 20 | Scalar |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| RoundsmanCode | `System.String` | true | true | evet | 10 | Scalar |
| RoundsmanResponsibilityAreas | `NebimV3.v3Entities.v3ElementItemList<NebimV3.ItemTransactions.RoundsmanResponsibilityArea>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-81231f4ce1ac) |
| SignOff | `System.Boolean` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| VehiclePlateNum | `System.String` | true | true | — | 30 | Scalar |
