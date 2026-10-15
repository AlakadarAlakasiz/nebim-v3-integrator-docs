[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-118"></a>

## 118 — SalesPerson / Satış temsilcisi

Satış temsilcisi için Cari hesaplar grubundaki model. Somut factory tipi NebimV3.CurrentAccounts.Salesperson. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.CurrentAccounts.Salesperson`. Grup: Cari hesaplar. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 118,
  "SalespersonCode": "{{SalespersonCode}}",
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
  "ModelType": 118,
  "SalespersonCode": "{{SalespersonCode}}",
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
  "ModelType": 118,
  "SalespersonCode": "{{SalespersonCode}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=118` → `{"ModelType":118}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| DailySalesIncentiveRate | `System.Single` | true | true | — | — | Scalar |
| Email | `System.String` | true | true | — | 100 | Scalar |
| EmployeeCode | `System.String` | true | true | — | 30 | Scalar |
| ExtraSalesIncentiveRate1 | `System.Single` | true | true | — | — | Scalar |
| ExtraSalesIncentiveRate2 | `System.Single` | true | true | — | — | Scalar |
| ExtraSalesIncentiveRate3 | `System.Single` | true | true | — | — | Scalar |
| FirstName | `System.String` | true | true | — | 20 | Scalar |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| IsSalespersonTeamLeader | `System.Boolean` | true | true | — | — | Scalar |
| IsWorkOnRetail | `System.Boolean` | true | true | — | — | Scalar |
| IsWorkOnWholeSale | `System.Boolean` | true | true | — | — | Scalar |
| LastName | `System.String` | true | true | — | 20 | Scalar |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| SalespersonCode | `System.String` | true | true | evet | 10 | Scalar |
| SalespersonTeamCode | `System.String` | true | true | — | 10 | Scalar |
| SalespersonTypeCode | `System.String` | true | true | — | 10 | Scalar |
| SignOff | `System.Boolean` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| WeekendSalesIncentiveRate | `System.Single` | true | true | — | — | Scalar |
