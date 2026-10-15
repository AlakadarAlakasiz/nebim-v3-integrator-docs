[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-219"></a>

## 219 — SecondmentPlan / Geçici görevlendirme planı

Geçici görevlendirme planı için Personel işlemleri grubundaki model. Somut factory tipi NebimV3.Payroll.WorkPlaceSecondment. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Payroll.WorkPlaceSecondment`. Grup: Personel işlemleri. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.EmployeeController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 219,
  "CurrAccCode": "{{CurrAccCode}}",
  "StartDate": "2026-01-01T00:00:00",
  "WorkPlaceCode": "{{WorkPlaceCode}}",
  "EmployeeCode": "{{EmployeeCode}}",
  "CancelDate": "2026-01-01T00:00:00",
  "EndDate": "2026-01-01T00:00:00"
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 219,
  "CurrAccCode": "{{CurrAccCode}}",
  "StartDate": "2026-01-01T00:00:00",
  "WorkPlaceCode": "{{WorkPlaceCode}}",
  "EmployeeCode": "{{EmployeeCode}}",
  "CancelDate": "2026-01-01T00:00:00",
  "EndDate": "2026-01-01T00:00:00"
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 219,
  "CurrAccCode": "{{CurrAccCode}}",
  "StartDate": "2026-01-01T00:00:00",
  "WorkPlaceCode": "{{WorkPlaceCode}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=219` → `{"ModelType":219}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| CancelDate | `System.DateTime` | true | true | — | — | Scalar |
| Canceled | `System.Boolean` | true | true | — | — | Scalar |
| CurrAccCode | `System.String` | true | true | evet | — | Scalar |
| EmployeeCode | `System.String` | true | true | — | — | Scalar |
| EndDate | `System.DateTime` | true | true | — | — | Scalar |
| EndTime | `System.TimeSpan` | true | true | — | — | Scalar |
| IsCompleted | `System.Boolean` | true | true | — | — | Scalar |
| StartDate | `System.DateTime` | true | true | evet | — | Scalar |
| StartTime | `System.TimeSpan` | true | true | — | — | Scalar |
| WorkPlaceCode | `System.String` | true | true | evet | 10 | Scalar |
