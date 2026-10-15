[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-163"></a>

## 163 — AdjustCostInvoice / Fatura maliyet düzeltmesi

Fatura maliyet düzeltmesi; yöntem4 artırımı,8 azaltımı okur. Örnek yalnız kanıtlanmış özel alan parçasıdır; tam header modeli çözülmemiştir.

Somut kök: `Özel / dinamik işlem`. Grup: Özel işlemler. Örnek kanıtı: `source-operation-template`.

Kısıtlı controller kabul envanteri: `NebimV3.Integrator.AdjustCostController`. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.

### Örnek request

`POST {{baseUrl}}/AdjustCostService/Post/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 163,
  "ProcessCode": "{{ProcessCode}}",
  "AdjustCostMethodCode": 4,
  "AdjustCostInvoices": [
    {
      "InvoiceNumber": "{{InvoiceNumber}}",
      "CostLines": [
        {
          "LineID": "{{exampleGuid}}",
          "IncreaseAmount": 1,
          "ReduceAmount": 0
        }
      ]
    }
  ]
}
```

### Örnek response

Kaynakta AdjustCostHeaderInvoice, AdjustCostHeaderTransactionBase tipinden türemiştir; controller ModelType163 değerini korur. Yalnız kanıtlanmış baz header alanlarının temsili alt kümesi gösterilir. AdjustCostInvoices ve nested sonuçların tam şeması çözümlenmiş değildir; bu bir canlı başarı yakalaması değildir.

```json
{
  "ModelType": 163,
  "AdjustCostHeaderID": "{{exampleGuid}}",
  "AdjustCostNumber": "{{AdjustCostNumber}}",
  "AdjustCostMethodCode": 4,
  "Amount": 1,
  "ProcessCode": "{{ProcessCode}}"
}
```

### Okuma / silme / şablon

Özel işlem için genel GetModel/Delete gövdesi uydurulmaz.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=163` → `{"ModelType":163}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |
|---|---|---|---|---|---:|---|
| AdjustAllEPInvoiceLine | `System.Boolean` | true | true | — | — | Scalar |
| AdjustCostHeaderID | `System.Guid` | true | true | evet | — | Scalar |
| AdjustCostMethodCode | `System.Byte` | true | true | — | — | Scalar |
| AdjustCostNumber | `System.String` | true | true | — | — | Scalar |
| Amount | `System.Decimal` | true | true | — | — | Scalar |
| BankHeaderID | `System.Guid` | true | true | — | — | Scalar |
| BankTransNumber | `System.String` | true | true | — | — | Scalar |
| CompanyCode | `System.Decimal` | true | true | — | — | Scalar |
| DisableLockOperation | `System.Boolean` | true | true | — | — | Scalar |
| DocCurrencyCode | `System.String` | true | true | — | — | Scalar |
| ExchangeRate | `System.Double` | true | true | — | — | Scalar |
| ExpenseSlipHeaderID | `System.Guid` | true | true | — | — | Scalar |
| ExportFileNumber | `System.String` | true | true | — | — | Scalar |
| ImportFileNumber | `System.String` | true | true | — | — | Scalar |
| InvoiceHeaderID | `System.Guid` | true | true | — | — | Scalar |
| InvoiceNumber | `System.String` | true | true | — | — | Scalar |
| IsCompleted | `System.Boolean` | true | true | — | — | Scalar |
| IsLocked | `System.Boolean` | true | true | — | — | Scalar |
| LocalCurrencyCode | `System.String` | true | true | — | — | Scalar |
| OfficeCode | `System.String` | true | true | — | — | Scalar |
| OperationDate | `System.DateTime` | true | true | — | — | Scalar |
| OperationTime | `System.TimeSpan` | true | true | — | — | Scalar |
| Rate | `System.Single` | true | true | — | — | Scalar |
| RefNumber | `System.String` | true | true | — | — | Scalar |
| StoreCode | `System.String` | true | true | — | — | Scalar |
| AdjustCostTransactions | `NebimV3.v3Entities.v3ElementItemList` | true | true | — | — | Dizi; somut satır çözülemedi |
| InnerProcessCode | `System.String` | true | true | — | — | Scalar |
| ProcessCode | `System.String` | true | true | — | — | Scalar |

Özel işlemde dinamik gövde esas alınır. Model163 tablosu yalnız doğrulanan baz header alanlarını,113 tablosu seçilen CustomerAttribute örneğini gösterir; selector ve özel nested gövdeler ayrıca ele alınır.
