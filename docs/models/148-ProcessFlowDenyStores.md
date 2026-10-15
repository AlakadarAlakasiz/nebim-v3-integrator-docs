[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-148"></a>

## 148 — ProcessFlowDenyStores / Mağaza süreç engelleri

Mağaza süreç engelleri için Cari hesaplar grubundaki model. Somut factory tipi NebimV3.CurrentAccounts.ProcessFlowDenyStores. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.CurrentAccounts.ProcessFlowDenyStores`. Grup: Cari hesaplar. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 148,
  "CompanyCode": 1,
  "StoreCode": "{{StoreCode}}",
  "ProcessFlowCode": 0,
  "SubCurrAccID": "{{exampleGuid}}",
  "ProcessFlowDenyReasonCode": "{{ProcessFlowDenyReasonCode}}"
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 148,
  "CompanyCode": 1,
  "StoreCode": "{{StoreCode}}",
  "ProcessFlowCode": 0,
  "SubCurrAccID": "{{exampleGuid}}",
  "ProcessFlowDenyReasonCode": "{{ProcessFlowDenyReasonCode}}"
}
```

### Okuma / silme / şablon

Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.

`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`

```json
{
  "ModelType": 148,
  "CompanyCode": 1,
  "ProcessFlowCode": 0,
  "SubCurrAccID": "{{exampleGuid}}",
  "StoreCode": "{{StoreCode}}"
}
```

Delete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.

`GET {{baseUrl}}/IntegratorService/NewModel?modelType=148` → `{"ModelType":148}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| AllowReturnTransactions | `System.Boolean` | true | true | — | — | Scalar |
| CompanyCode | `System.Decimal` | true | true | evet | — | Scalar |
| ProcessFlowCode | `System.Byte` | true | true | evet | — | Scalar |
| ProcessFlowDenyReasonCode | `System.String` | true | true | — | 10 | Scalar |
| SubCurrAccID | `System.Guid` | true | true | evet | — | Scalar |
| StoreCode | `System.String` | true | true | evet | 30 | Scalar |
