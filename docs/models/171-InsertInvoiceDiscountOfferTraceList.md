[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-171"></a>

## 171 — InsertInvoiceDiscountOfferTraceList / Toplu fatura indirim izi ekleme

Toplu fatura indirim izi ekleme için Faturalar grubundaki model. Somut factory tipi NebimV3.Invoices.InsertInvoiceDiscountOfferListModel. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.Invoices.InsertInvoiceDiscountOfferListModel`. Grup: Faturalar. Örnek kanıtı: `metadata-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 171,
  "Lines": [
    {
      "CustomerDiscountPointID": "{{exampleGuid}}",
      "DigitalMarketingServiceCode": "{{DigitalMarketingServiceCode}}",
      "DiscountAmount": 0,
      "DiscountOfferCode": "{{DiscountOfferCode}}",
      "DiscountPointTypeCode": "{{DiscountPointTypeCode}}",
      "DiscountRate": 0
    }
  ]
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 171,
  "Lines": [
    {
      "CustomerDiscountPointID": "{{exampleGuid}}",
      "DigitalMarketingServiceCode": "{{DigitalMarketingServiceCode}}",
      "DiscountAmount": 0,
      "DiscountOfferCode": "{{DiscountOfferCode}}",
      "DiscountPointTypeCode": "{{DiscountPointTypeCode}}",
      "DiscountRate": 0
    }
  ]
}
```

### Okuma / silme / şablon

GetModel için güvenilir yazılabilir anahtar adayı çıkarılamadı; uydurma HeaderID/Code gönderilmez.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=171` → `{"ModelType":171}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| Lines | `NebimV3.v3Entities.v3EntityList<NebimV3.Invoices.InvoiceDiscountOffer>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-96055679f96e) |
