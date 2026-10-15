[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-181"></a>

## 181 — EmployeeDebit / Personel zimmeti

Personel zimmeti için Personel işlemleri grubundaki model. Somut factory tipi NebimV3.Payroll.EmployeeDebit. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Payroll.EmployeeDebit`. Grup: Personel işlemleri. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.EmployeeDebitController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 181,
  "EmployeeDebitID": "{{exampleGuid}}",
  "EmployeeCode": "{{EmployeeCode}}",
  "Description": "ÖRNEK Description",
  "DocumentDate": "2026-01-01T00:00:00",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "Debit": 0,
  "DueDate": "2026-01-01T00:00:00",
  "DocumentNumber": "{{DocumentNumber}}"
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 181,
  "EmployeeDebitID": "{{exampleGuid}}",
  "EmployeeCode": "{{EmployeeCode}}",
  "Description": "ÖRNEK Description",
  "DocumentDate": "2026-01-01T00:00:00",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "Debit": 0,
  "DueDate": "2026-01-01T00:00:00",
  "DocumentNumber": "{{DocumentNumber}}"
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 181,
  "EmployeeDebitID": "{{exampleGuid}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=181` → `{"ModelType":181}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| ApplicationCode | `System.String` | true | true | — | — | Scalar |
| ApplicationID | `System.Guid` | true | true | — | — | Scalar |
| Debit | `System.Decimal` | true | true | — | — | Scalar |
| DeductionCode | `System.String` | true | true | — | 30 | Scalar |
| Description | `System.String` | true | true | — | — | Scalar |
| DocCurrencyCode | `System.String` | true | true | — | — | Scalar |
| DocumentDate | `System.DateTime` | true | true | — | — | Scalar |
| DocumentNumber | `System.String` | true | true | — | 30 | Scalar |
| DueDate | `System.DateTime` | true | true | — | — | Scalar |
| EmployeeCode | `System.String` | true | true | — | 30 | Scalar |
| EmployeeDebitID | `System.Guid` | true | true | evet | — | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| IsLocked | `System.Boolean` | true | true | — | — | Scalar |
| IsPaid | `System.Boolean` | true | true | — | — | Scalar |
| IsPostingJournal | `System.Boolean` | true | true | — | — | Scalar |
| JournalDate | `System.DateTime` | true | true | — | — | Scalar |
| LocalCurrencyCode | `System.String` | true | true | — | — | Scalar |
