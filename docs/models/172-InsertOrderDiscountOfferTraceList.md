[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-172"></a>

## 172 — InsertOrderDiscountOfferTraceList / Toplu sipariş indirim izi ekleme

Toplu sipariş indirim izi ekleme için Siparişler grubundaki model. Somut factory tipi NebimV3.Orders.InsertOrderDiscountOfferListModel. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Orders.InsertOrderDiscountOfferListModel`. Grup: Siparişler. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 172,
  "Lines": [
    {
      "CustomerDiscountPointID": "{{exampleGuid}}",
      "DiscountAmount": 0,
      "DiscountOfferCode": "{{DiscountOfferCode}}",
      "DiscountPointTypeCode": "{{DiscountPointTypeCode}}",
      "DiscountRate": 0,
      "DiscountVoucherTypeCode": "{{DiscountVoucherTypeCode}}"
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 172,
  "Lines": [
    {
      "CustomerDiscountPointID": "{{exampleGuid}}",
      "DiscountAmount": 0,
      "DiscountOfferCode": "{{DiscountOfferCode}}",
      "DiscountPointTypeCode": "{{DiscountPointTypeCode}}",
      "DiscountRate": 0,
      "DiscountVoucherTypeCode": "{{DiscountVoucherTypeCode}}"
    }
  ]
}
```

### Okuma / silme / şablon

GetModel için güvenilir yazılabilir anahtar adayı çıkarılamadı; uydurma HeaderID/Code gönderilmez.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=172` → `{"ModelType":172}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| Lines | `NebimV3.v3Entities.v3EntityList<NebimV3.Orders.OrderDiscountOffer>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-0434ecc11970) |
