[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-131"></a>

## 131 — ChequeTrans / Çek hareketi

Çek hareketi için Çek, senet ve teminatlar grubundaki model. Somut factory tipi NebimV3.Cheques.ChequeTrans. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Cheques.ChequeTrans`. Grup: Çek, senet ve teminatlar. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 131,
  "CurrAccCode": "{{CurrAccCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "BankAccountCode": "{{BankAccountCode}}",
  "CashAccountCode": "{{CashAccountCode}}",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "DocumentNumber": "{{DocumentNumber}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "DocCurrencyCode": "TRY",
      "Amount": 1,
      "BankBranchCode": "{{BankBranchCode}}",
      "BankCode": "{{BankCode}}",
      "ChequeAtt01": "{{ChequeAtt01}}"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 131,
  "HeaderID": "{{exampleGuid}}",
  "CurrAccCode": "{{CurrAccCode}}",
  "Description": "ÖRNEK Description",
  "CompanyCode": 1,
  "OfficeCode": "{{OfficeCode}}",
  "StoreCode": "{{StoreCode}}",
  "DocumentDate": "2026-01-01T00:00:00",
  "BankAccountCode": "{{BankAccountCode}}",
  "CashAccountCode": "{{CashAccountCode}}",
  "DocCurrencyCode": "TRY",
  "LocalCurrencyCode": "TRY",
  "DocumentNumber": "{{DocumentNumber}}",
  "Lines": [
    {
      "LineID": "{{exampleGuid}}",
      "DocCurrencyCode": "TRY",
      "Amount": 1,
      "BankBranchCode": "{{BankBranchCode}}",
      "BankCode": "{{BankCode}}",
      "ChequeAtt01": "{{ChequeAtt01}}"
    }
  ]
}
```

### Okuma / silme / şablon

Yazılabilir anahtar yok; kaynak LoadEntity normal setter yolundan aday belge numarası gösterilir. Model bazında yükleme akışı doğrulanmış değildir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 131,
  "DocumentNumber": "{{DocumentNumber}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=131` → `{"ModelType":131}`.

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
| Lines | `NebimV3.Cheques.ChequeLineList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-da4bd13a47a4) |
| OfficeCode | `System.String` | true | true | — | 20 | Scalar |
| ATAttributes | `NebimV3.Cheques.ChequeATAttributeList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-a1c0ae75f721) |
| BankAccountCode | `System.String` | true | true | — | — | Scalar |
| CashAccountCode | `System.String` | true | true | — | — | Scalar |
| ChequeTransNumber | `System.String` | true | true | — | — | Scalar |
| ChequeTransTypeCode | `NebimV3.Cheques.ChequeTransTypes` | true | true | — | — | Scalar |
| ContactID | `System.Guid` | true | true | — | — | Scalar |
| CurrAccCode | `System.String` | true | true | — | — | Scalar |
| CurrAccTypeCode | `System.Byte` | true | true | — | — | Scalar |
| DefATAttributes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.Cheques.ChequeDefATAttribute>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-0dac4b32cbe1) |
| DeleteChequesOnDelete | `System.Boolean` | true | true | — | — | Scalar |
| Description | `System.String` | true | true | — | — | Scalar |
| DocCurrencyCode | `System.String` | true | true | — | — | Scalar |
| DocumentDate | `System.DateTime` | true | true | — | — | Scalar |
| DocumentNumber | `System.String` | true | true | — | — | Scalar |
| DocumentTime | `System.TimeSpan` | true | true | — | — | Scalar |
| EmptyChequesCurrAccOnDelete | `System.Boolean` | true | true | — | — | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| ExchangeTypeCode | `System.Byte` | true | true | — | — | Scalar |
| GLTypeCode | `System.String` | true | true | — | — | Scalar |
| JournalDate | `System.DateTime` | true | true | — | — | Scalar |
| LocalCurrencyCode | `System.String` | true | true | — | — | Scalar |
| PosTerminalID | `System.Int16` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | — | Scalar |
| SubCurrAccID | `System.Guid` | true | true | — | — | Scalar |
