[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-215"></a>

## 215 — GLAcc / Muhasebe hesabı

Muhasebe hesabı için Muhasebe grubundaki model. Somut factory tipi NebimV3.GL.GLAcc. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.GL.GLAcc`. Grup: Muhasebe. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 215,
  "CompanyCode": 1,
  "GLAccCode": "{{GLAccCode}}",
  "CostCenterCode": "{{CostCenterCode}}",
  "GLAccDescription": "{{GLAccDescription}}",
  "GLAccMainCode": "{{GLAccMainCode}}",
  "GLAccSubCode1": "{{GLAccSubCode1}}",
  "Descriptions": [
    {
      "Description": "ÖRNEK Description",
      "DataLanguageCode": "TR",
      "DataLanguageDescription": "{{DataLanguageDescription}}"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 215,
  "CompanyCode": 1,
  "GLAccCode": "{{GLAccCode}}",
  "CostCenterCode": "{{CostCenterCode}}",
  "GLAccDescription": "{{GLAccDescription}}",
  "GLAccMainCode": "{{GLAccMainCode}}",
  "GLAccSubCode1": "{{GLAccSubCode1}}",
  "Descriptions": [
    {
      "Description": "ÖRNEK Description",
      "DataLanguageCode": "TR"
    }
  ]
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 215,
  "CompanyCode": 1,
  "GLAccCode": "{{GLAccCode}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=215` → `{"ModelType":215}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| AllowForeignCurrencyTrans | `System.Boolean` | true | true | — | — | Scalar |
| Attributes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.GL.AttributeGLAcc>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-40895134903f) |
| AvailableForeignCurrencyTransList | `NebimV3.v3Entities.v3ElementItemList<NebimV3.GL.GLAccAvailableForeignCurrencyTrans>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-467d532c3261) |
| CompanyCode | `System.Decimal` | true | true | evet | — | Scalar |
| CostCenterCode | `System.String` | true | true | — | 20 | Scalar |
| Descriptions | `NebimV3.GL.GLAccLanguageDescriptionList` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-f31bc69161d4) |
| ForceCostCenter | `System.Boolean` | true | true | — | — | Scalar |
| ForceGLType | `System.Boolean` | true | true | — | — | Scalar |
| ForceQty | `System.Boolean` | true | true | — | — | Scalar |
| GLAccAvailableJournalTypeSubs | `NebimV3.v3Entities.v3ElementItemList<NebimV3.GL.GLAccAvailableJournalTypeSub>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-3498492f6245) |
| GLAccCode | `System.String` | true | true | evet | 30 | Scalar |
| GLAccDescription | `System.String` | true | true | — | 200 | Scalar |
| GLAccMainCode | `System.String` | true | true | — | 10 | Scalar |
| GLAccNotes | `NebimV3.v3Entities.v3ElementItemList<NebimV3.GL.GLAccNotes>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-3c3b25484f2c) |
| GLAccOnlineBank | `NebimV3.v3Entities.v3ElementItemList<NebimV3.GL.GLAccOnlineBank>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-df91a9010892) |
| GLAccSubCode1 | `System.String` | true | true | — | — | Scalar |
| GLAccSubCode2 | `System.String` | true | true | — | — | Scalar |
| GLAccSubCode3 | `System.String` | true | true | — | — | Scalar |
| GLAccUserWarnings | `NebimV3.v3Entities.v3ElementItemList<NebimV3.GL.GLAccUserWarning>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-3d2d18e86075) |
| GLTypeCode | `System.String` | true | true | — | 20 | Scalar |
| IdentityNum | `System.String` | true | true | — | 20 | Scalar |
| InflationAdjustmentDiffGLAccCode | `System.String` | true | true | — | 30 | Scalar |
| InflationAdjustmentGLAccCode | `System.String` | true | true | — | 30 | Scalar |
| IsBlocked | `System.Boolean` | true | true | — | — | Scalar |
| IsIndividualAcc | `System.Boolean` | true | true | — | — | Scalar |
| IsNonMonetaryItem | `System.Boolean` | true | true | — | — | Scalar |
| IsStampDutyAcc | `System.Boolean` | true | true | — | — | Scalar |
| ReverseBalanceGLAccCode | `System.String` | true | true | — | 30 | Scalar |
| TaxNumber | `System.String` | true | true | — | 20 | Scalar |
| TaxOfficeCode | `System.String` | true | true | — | 10 | Scalar |
| TaxPaymentAccTypeCode | `System.Byte` | true | true | — | — | Scalar |
| TaxPaymentTypeCode | `System.Byte` | true | true | — | — | Scalar |
