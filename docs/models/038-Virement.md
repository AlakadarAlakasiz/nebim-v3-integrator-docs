[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-38"></a>

## 38 — Virement / Virman

Virman için Ödemeler grubundaki model. Somut factory tipi NebimV3.Payments.Virement. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Payments.Virement`. Grup: Ödemeler. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 38,
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "LocalCurrencyCode": "TRY",
  "DocumentNumber": "{{DocumentNumber}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "CreditDebitHeaderID": "{{exampleGuid}}",
      "DebitDebitHeaderID": "{{exampleGuid}}",
      "DebitReasonCode": "{{DebitReasonCode}}",
      "FTAtt01": "{{FTAtt01}}",
      "FTAtt02": "{{FTAtt02}}"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 38,
  "HeaderID": "{{exampleGuid}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "LocalCurrencyCode": "TRY",
  "DocumentNumber": "{{DocumentNumber}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "CreditDebitHeaderID": "{{exampleGuid}}",
      "DebitDebitHeaderID": "{{exampleGuid}}",
      "DebitReasonCode": "{{DebitReasonCode}}",
      "FTAtt01": "{{FTAtt01}}",
      "FTAtt02": "{{FTAtt02}}"
    }
  ]
}
```

### Okuma / silme / şablon

Yazılabilir anahtar yok; kaynak LoadEntity normal setter yolundan aday belge numarası gösterilir. Model bazında yükleme akışı doğrulanmış değildir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 38,
  "DocumentNumber": "{{DocumentNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=38` → `{"ModelType":38}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| ApplicationCode | `System.String` | true | true | — | — | Scalar |
| ApplicationID | `System.Guid` | true | true | — | — | Scalar |
| AutoGenerateUniqueNumber | `System.Boolean` | true | true | — | — | Scalar |
| BlockCheckOutProcess | `System.Boolean` | true | true | — | — | Scalar |
| CheckByOperationDate | `System.Boolean` | true | false | — | — | Scalar |
| CompanyCode | `System.Decimal` | true | true | — | — | Scalar |
| DisableInsertDefaultAttributes | `System.Boolean` | true | true | — | — | Scalar |
| HeaderID | `System.Guid` | false | true | evet | — | readonly-scalar |
| IsCompleted | `System.Boolean` | true | true | — | — | Scalar |
| IsLocked | `System.Boolean` | true | true | — | — | Scalar |
| IsPrinted | `System.Boolean` | true | true | — | — | Scalar |
| Lines | `NebimV3.Payments.VirementLineList<NebimV3.Payments.VirementLine>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-5a5ec1ecb723) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| ATAttributes | `NebimV3.Payments.VirementATAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-051530e1a8bc) |
| Description | `System.String` | true | true | — | 200 | Scalar |
| DisableJournalIntegration | `System.Boolean` | true | true | — | — | Scalar |
| DocumentDate | `System.DateTime` | true | true | — | — | Scalar |
| DocumentNumber | `System.String` | true | true | — | 30 | Scalar |
| DocumentTime | `System.TimeSpan` | true | true | — | — | Scalar |
| GLTypeCode | `System.String` | true | true | — | 20 | Scalar |
| LineSource | `NebimV3.Payments.VirementLineDataSourceList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-a14104ea9fc4) |
| LocalCurrencyCode | `System.String` | true | true | — | 10 | Scalar |
| StoreCode | `System.String` | true | true | — | 30 | Scalar |
| VirementNumber | `System.String` | true | true | — | — | Scalar |
