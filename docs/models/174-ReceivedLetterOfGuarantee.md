[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-174"></a>

## 174 — ReceivedLetterOfGuarantee / Alınan teminat mektubu

Alınan teminat mektubu için Çek, senet ve teminatlar grubundaki model. Somut factory tipi NebimV3.Cheques.ReceivedLetterOfGuarantee. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Cheques.ReceivedLetterOfGuarantee`. Grup: Çek, senet ve teminatlar. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 174,
  "LetterOfGuaranteeCode": "{{LetterOfGuaranteeCode}}",
  "CurrAccCode": "{{CurrAccCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "CurrencyCode": "TRY",
  "DocumentDate": "2026-01-01T00:00:00",
  "Amount": 1,
  "DueDate": "2026-01-01T00:00:00",
  "DocumentNumber": "{{DocumentNumber}}"
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 174,
  "LetterOfGuaranteeCode": "{{LetterOfGuaranteeCode}}",
  "CurrAccCode": "{{CurrAccCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "CurrencyCode": "TRY",
  "DocumentDate": "2026-01-01T00:00:00",
  "Amount": 1,
  "DueDate": "2026-01-01T00:00:00",
  "DocumentNumber": "{{DocumentNumber}}"
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 174,
  "LetterOfGuaranteeCode": "{{LetterOfGuaranteeCode}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=174` → `{"ModelType":174}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| Amount | `System.Decimal` | true | true | — | — | Scalar |
| BankBranchCode | `System.String` | true | true | — | 20 | Scalar |
| BankCode | `System.String` | true | true | — | 10 | Scalar |
| ClosingDate | `System.DateTime` | true | true | — | — | Scalar |
| CompanyCode | `System.Decimal` | true | true | — | — | Scalar |
| CostCenterCode | `System.String` | true | true | — | 20 | Scalar |
| CreditGLAccCode | `System.String` | true | true | — | 30 | Scalar |
| CurrAccCode | `System.String` | true | true | — | 30 | Scalar |
| CurrAccTypeCode | `System.Byte` | true | true | — | — | Scalar |
| CurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| DebitGLAccCode | `System.String` | true | true | — | 30 | Scalar |
| Description | `System.String` | true | true | — | 200 | Scalar |
| DocumentDate | `System.DateTime` | true | true | — | — | Scalar |
| DocumentNumber | `System.String` | true | true | — | 30 | Scalar |
| DueDate | `System.DateTime` | true | true | — | — | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| ExportFileNumber | `System.String` | true | true | — | — | Scalar |
| ImportFileNumber | `System.String` | true | true | — | — | Scalar |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| IsClosed | `System.Boolean` | true | true | — | — | Scalar |
| LetterOfGuaranteeCode | `System.String` | true | true | evet | 30 | Scalar |
| LetterTypeCode | `System.String` | true | true | — | 10 | Scalar |
| OfficeCode | `System.String` | true | true | — | 5 | Scalar |
| SubCurrAccID | `System.Guid` | true | true | — | — | Scalar |
| AttributeList | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| Attributes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Cheques.LetterOfGuaranteeReceivedAttribute>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-76be05a63b0c) |
