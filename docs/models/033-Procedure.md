[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)

<a id="model-33"></a>

## 33 — Procedure / İzinli prosedür çalıştırma

Saklı prosedür çalıştırır. Özgün servis ProcName ve Parameters alanlarını kullanır; prosedürün salt okunur olduğu varsayılmaz.

Somut kök: `Özel / dinamik işlem`. Grup: Özel işlemler. Örnek kanıtı: `source-operation-template`.

### Örnek request

`POST {{baseUrl}}/IntegratorService/RunProc/{{token}}`

Kaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.

```json
{
  "ModelType": 33,
  "ProcName": "{{ProcName}}",
  "Parameters": [
    {
      "Name": "@Kod",
      "Value": "{{ParameterValue}}"
    }
  ]
}
```

### Örnek response

Şematik sonuç dizisi; ORNEK_KOLON gerçek/sabit kolon değildir. Prosedür/rapor kolonları kullanılır.

```json
[
  {
    "ORNEK_KOLON": "DEGER"
  }
]
```

RunProcReturnSingle aynı gövdeyle ilk satır nesnesi veya null döndürür. Prosedür kolonları ve yan etkileri tanıma bağlıdır; read-only olduğu varsayılmaz.

### Okuma / silme / şablon

Özel işlem için genel GetModel/Delete gövdesi uydurulmaz.


`GET {{baseUrl}}/IntegratorService/NewModel?modelType=33` → `{"ModelType":33}`.

### Modelde hata değerlendirmesi

Giriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](../HTTP-AND-ERRORS.md#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.

### Giriş / çıkış alanları

true: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.

Sabit entity alan listesi yok; yukarıdaki dinamik işlem sözleşmesini kullanın.

Özel işlemde dinamik gövde esas alınır. Model163 tablosu yalnız doğrulanan baz header alanlarını,113 tablosu seçilen CustomerAttribute örneğini gösterir; selector ve özel nested gövdeler ayrıca ele alınır.
