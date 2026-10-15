[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-224"></a>

## 224 — JobInterview / İş görüşmesi

İş görüşmesi için İnsan kaynakları grubundaki model. Somut factory tipi NebimV3.HR.JobInterview. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.HR.JobInterview`. Grup: İnsan kaynakları. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 224,
  "JobInterviewID": "{{exampleGuid}}",
  "EmployeeCode": "{{EmployeeCode}}",
  "InterViewTime": "00:00:00",
  "InterviewDate": "2026-01-01T00:00:00",
  "InterviewPlace": "{{InterviewPlace}}",
  "JobCandidateCode": "{{JobCandidateCode}}"
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 224,
  "JobInterviewID": "{{exampleGuid}}",
  "EmployeeCode": "{{EmployeeCode}}",
  "InterViewTime": "00:00:00",
  "InterviewDate": "2026-01-01T00:00:00",
  "InterviewPlace": "{{InterviewPlace}}",
  "JobCandidateCode": "{{JobCandidateCode}}"
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 224,
  "JobInterviewID": "{{exampleGuid}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=224` → `{"ModelType":224}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| EmployeeCode | `System.String` | true | true | — | — | Scalar |
| InterViewTime | `System.TimeSpan` | true | true | — | — | Scalar |
| InterviewDate | `System.DateTime` | true | true | — | — | Scalar |
| InterviewPlace | `System.String` | true | true | — | 200 | Scalar |
| IsClosed | `System.Boolean` | true | true | — | — | Scalar |
| JobCandidateCode | `System.String` | true | true | — | — | Scalar |
| JobInterViewResultCode | `System.String` | true | true | — | 10 | Scalar |
| JobInterviewID | `System.Guid` | true | true | evet | — | Scalar |
| JobInterviewNotes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.HR.JobInterviewNotes>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-3f5cfa85f202) |
| JobPositionCode | `System.String` | true | true | — | 10 | Scalar |
| Notes | `System.String` | true | true | — | — | Scalar |
