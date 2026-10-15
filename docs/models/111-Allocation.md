[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-111"></a>

## 111 — Allocation / Mağaza dağıtımı

Mağaza dağıtımı için Mağaza dağıtımı grubundaki model. Somut factory tipi NebimV3.StoreAllocations.AllocationModelForIntegrator. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır.

Somut kök: `NebimV3.StoreAllocations.AllocationModelForIntegrator`. Grup: Mağaza dağıtımı. Örnek kanıtı: `metadata-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.AllocationController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/IntegratorService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 111,
  "Description": "ÖRNEK Description",
  "WarehouseCode": "{{WarehouseCode}}",
  "OperationDate": "2026-01-01T00:00:00",
  "ATAtt01": "{{ATAtt01}}",
  "ATAtt02": "{{ATAtt02}}",
  "ATAtt03": "{{ATAtt03}}"
}
```

### Örnek response

Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

```json
{
  "ModelType": 111,
  "Description": "ÖRNEK Description",
  "WarehouseCode": "{{WarehouseCode}}",
  "OperationDate": "2026-01-01T00:00:00",
  "ATAtt01": "{{ATAtt01}}",
  "ATAtt02": "{{ATAtt02}}",
  "ATAtt03": "{{ATAtt03}}"
}
```

### Okuma / silme / şablon

GetModel için güvenilir yazılabilir anahtar adayı çıkarılamadı; uydurma HeaderID/Code gönderilmez.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=111` → `{"ModelType":111}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| ATAtt01 | `System.String` | true | true | — | — | Scalar |
| ATAtt02 | `System.String` | true | true | — | — | Scalar |
| ATAtt03 | `System.String` | true | true | — | — | Scalar |
| ATAtt04 | `System.String` | true | true | — | — | Scalar |
| ATAtt05 | `System.String` | true | true | — | — | Scalar |
| AllocationChannels | `NebimV3.v3Entities.v3ElementItemList<NebimV3.StoreAllocations.AllocationChannelItemModelFI>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-4e3b9d235d00) |
| AllocationProductQtys | `NebimV3.v3Entities.v3ElementItemList<NebimV3.StoreAllocations.AllocationProductQtyModelFI>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-9288699bbebb) |
| AllocationProducts | `NebimV3.v3Entities.v3ElementItemList<NebimV3.StoreAllocations.AllocationProductModelFI>` | true | true | — | — | Dizi; somut satır [tip](../TYPES.md#t-645425ddda0d) |
| AllocationRuleCode | `System.String` | true | true | — | — | Scalar |
| Description | `System.String` | true | true | — | — | Scalar |
| ITAtt01 | `System.String` | true | true | — | — | Scalar |
| ITAtt02 | `System.String` | true | true | — | — | Scalar |
| ITAtt03 | `System.String` | true | true | — | — | Scalar |
| ITAtt04 | `System.String` | true | true | — | — | Scalar |
| ITAtt05 | `System.String` | true | true | — | — | Scalar |
| ITAtt06 | `System.String` | true | true | — | — | Scalar |
| ITAtt07 | `System.String` | true | true | — | — | Scalar |
| ITAtt08 | `System.String` | true | true | — | — | Scalar |
| ITAtt09 | `System.String` | true | true | — | — | Scalar |
| ITAtt10 | `System.String` | true | true | — | — | Scalar |
| OperationDate | `System.DateTime` | true | true | — | — | Scalar |
| WarehouseCode | `System.String` | true | true | — | — | Scalar |
