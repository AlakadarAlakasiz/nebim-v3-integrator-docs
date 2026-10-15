[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-45"></a>

## 45 — CloseInstallmentPayment / Taksit ödeme kapatma

Taksit ödeme kapatma için Taksit ödeme işlemleri grubundaki model. Somut factory tipi NebimV3.UIWindowsForm.CloseInstallmentPaymentModel. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.UIWindowsForm.CloseInstallmentPaymentModel`. Grup: Taksit ödeme işlemleri. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 45,
  "CustomerCode": "{{CustomerCode}}",
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "OperationDate": "2026-01-01T00:00:00",
  "DocumentNumber": "{{DocumentNumber}}",
  "CustomerTypeCode": 0
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 45,
  "CustomerCode": "{{CustomerCode}}",
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "OperationDate": "2026-01-01T00:00:00",
  "DocumentNumber": "{{DocumentNumber}}",
  "CustomerTypeCode": 0
}
```

### Okuma / silme / şablon

Yazılabilir anahtar yok; kaynak LoadEntity normal setter yolundan aday belge numarası gösterilir. Model bazında yükleme akışı doğrulanmış değildir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 45,
  "DocumentNumber": "{{DocumentNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=45` → `{"ModelType":45}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| CustomerCode | `System.String` | true | true | — | — | Scalar |
| CustomerTypeCode | `NebimV3.ApplicationCommon.CurrAccTypes` | true | true | — | — | Scalar |
| DebitIDs | `System.Collections.Generic.IEnumerable<System.Guid>` | true | false | — | — | Scalar |
| DocumentNumber | `System.String` | true | true | — | — | Scalar |
| EarlyPaymentDiscount | `System.Double` | true | true | — | — | Scalar |
| ForceLateCharge | `System.Boolean` | true | true | — | — | Scalar |
| ForcePrePaidDiscount | `System.Boolean` | true | true | — | — | Scalar |
| MonthlyLateChargeRate | `System.Double` | true | true | — | — | Scalar |
| OfficeCode | `System.String` | true | true | — | — | Scalar |
| OperationDate | `System.DateTime` | true | true | — | — | Scalar |
| PaymentDataSource | `NebimV3.UIWindowsForm.PaymentDataSource` | true | false | — | — | Scalar |
| PosTerminalID | `System.Int16` | true | true | — | — | Scalar |
| SeriesCode | `System.String` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | — | Scalar |
