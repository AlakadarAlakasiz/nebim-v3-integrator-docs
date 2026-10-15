# Özgün Nebim V3 Entegratör API dokümantasyonu

**25.4.1.0** sürümündeki özgün IIS Entegratör backend’i için238 model, request/response şablonları, alan sözlüğü ve hata rehberi. Bağımsız, resmi olmayan teknik referanstır.

## İçerik

- [238 modelin Markdown rehberi](docs/ALL-MODELS.md)
- [Aranabilir çevrimdışı HTML rehber](docs/index.html) — dosyayı indirdikten sonra tarayıcıda açın; GitHub HTML’yi doğrudan uygulama olarak çalıştırmaz.
- [2.325 tipin alan/enum sözlüğü](docs/TYPES.md)
- [Postman koleksiyonu](docs/Nebim-V3-238-model.postman_collection.json) ve [ortamı](docs/Nebim-V3.postman_environment.json)
- [Model örnekleri](docs/examples), [doğrulama raporu](docs/validation.json)

Kodlar1–238 eksiksiz kapsanır;0/None sentinel’dır. Standart entity modelleriyle giriş, sorgu/prosedür, iptal, onay ve dönüştürme gibi özel işlemler ayrılır. Örnekler kaynak/metadata şablonudur; bütün iş kurallarını sağlayan canlı başarı yakalaması değildir. Model163 başarı örneği yalnız doğrulanan baz header alanlarıyla sınırlıdır; dinamik/çözülemeyen alt şemalar açıkça belirtilir.

## Postman

1. Koleksiyon ve ortam dosyalarını Import edin; ortamı seçin.
2. baseUrl’yi **özgün Nebim Entegratör** adresinize ayarlayın. Sanal IIS uygulama dizinini koruyun.
3. DatabaseName, UserGroupCode, UserName ve Password değerlerini kendi ortamınızda doldurun.
4. Model1 Connect isteğini gönderin. Başarıdaki token seçili ortama aktarılır.
5. Göndermeden önce örnek kodları, tarihleri ve GUID’leri gerçek iş değerleriyle değiştirin. Modelin kaynak iş kuralları, lisans ve yetkileri ayrıca geçerlidir.

Post/Delete, iptal, ödeme, onay ve dönüştürme modelleri veri değiştirebilir. Dokümanı üretmek servis/SQL isteği göndermez. Gerçek parola, token, şirket sunucu IP’si, müşteri gövdesi, DLL, lisans/passport veya Web.config bu depoda bulunmaz.

## Yeniden üretme

Python3 ve Node.js ile, depo kökünde:

```text
python tools/build_docs.py
node tools/verify_docs.mjs
```

Girdi data/source-contracts.json içindeki sürümlü özgün sözleşme snapshot’ıdır; başka bir projeye veya yerel Nebim kurulumuna bağımlılık yoktur. Üretim çevrimdışıdır. Kaynak hash’leri ve doğrulama sınırları JSON raporunda bulunur. ZIP artifacts/ altında üretilir ve Git’e eklenmez.

Nebim ve Nebim V3 adları ilgili hak sahiplerine aittir. Bu depo API kullanım bilgisini belgeler; ürünün kendisini veya resmi destek garantisini dağıtmaz.
