[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-74"></a>

## 74 — SendCashMainOfficeBankAccount / Merkez banka hesabına nakit gönderme

Merkez banka hesabına nakit gönderme için Banka işlemleri grubundaki model. Somut factory tipi NebimV3.Banks.SendCashMainOfficeBankAccountModel. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Banks.SendCashMainOfficeBankAccountModel`. Grup: Banka işlemleri. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.BankController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 74,
  "Description": "ÖRNEK Description",
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "BankAccountCode": "{{BankAccountCode}}",
  "BankTransNumber": "{{BankTransNumber}}",
  "CashAccountCode": "{{CashAccountCode}}",
  "Amount": 1,
  "DocumentNumber": "{{DocumentNumber}}"
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 74,
  "Description": "ÖRNEK Description",
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "BankAccountCode": "{{BankAccountCode}}",
  "BankTransNumber": "{{BankTransNumber}}",
  "CashAccountCode": "{{CashAccountCode}}",
  "Amount": 1,
  "DocumentNumber": "{{DocumentNumber}}"
}
```

### Okuma / silme / şablon

Yazılabilir anahtar yok; kaynak LoadEntity normal setter yolundan aday belge numarası gösterilir. Model bazında yükleme akışı doğrulanmış değildir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 74,
  "DocumentNumber": "{{DocumentNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=74` → `{"ModelType":74}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| ATAttribute | `NebimV3.Banks.BankATAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-501d3f0d1a5c) |
| AllowDifferentOfficeBankForStoreUser | `System.Boolean` | true | true | — | — | Scalar |
| Amount | `System.Decimal` | true | true | — | — | Scalar |
| BankAccountCode | `System.String` | true | true | — | — | Scalar |
| BankTransNumber | `System.String` | true | true | — | — | Scalar |
| CashAccountCode | `System.String` | true | true | — | — | Scalar |
| Description | `System.String` | true | true | — | — | Scalar |
| DocumentCurrencyCode | `System.String` | true | true | — | — | Scalar |
| DocumentDate | `System.DateTime` | true | true | — | — | Scalar |
| DocumentNumber | `System.String` | true | true | — | — | Scalar |
| DocumentTime | `System.TimeSpan` | true | true | — | — | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| GLTypeCode | `System.String` | true | true | — | — | Scalar |
| OfficeCode | `System.String` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | — | Scalar |
| TransferCharges | `System.Decimal` | true | true | — | — | Scalar |
