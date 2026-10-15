"""Build original Nebim V3 documentation offline from the bundled contract snapshot."""
from pathlib import Path
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import zipfile
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'docs'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def dump(v):return json.dumps(v,ensure_ascii=False,indent=2)
def write(name,text):
    p=OUT/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
registry=read(ROOT/'data/source-contracts.json')
catalog=registry
types=registry['types']
models=[m for m in registry['models'] if m['code']!=0]
assert [m['code'] for m in models]==list(range(1,239))
source_models={m['code']:m for m in registry['models']}
routes={r['path'] for r in registry['routes']}
variables={'baseUrl':'http://localhost:3019','token':'','DatabaseName':'','UserGroupCode':'','UserName':'','Password':'','exampleGuid':'00000000-0000-0000-0000-000000000001'}
FAMILIES = dict(Authentication='Giriş ve oturum', CurrentAccounts='Cari hesaplar', Items='Ürün ve tanımlar', Orders='Siparişler',
    Invoices='Faturalar', Integrator='Entegratör özel satış modelleri', SpecialOperations='Özel işlemler', ProductSupport='Ürün destek süreçleri',
    GL='Muhasebe', Payments='Ödemeler', Reservations='Rezervasyonlar', UIWindowsForm='Taksit ödeme işlemleri', Price='Fiyat listeleri',
    DiscountOffers='İndirim ve kampanya', Shipments='Sevkiyat ve irsaliyeler', ExpenseSlips='Gider ve borç/alacak belgeleri', Banks='Banka işlemleri',
    Cashs='Kasa işlemleri', DispOrders='Sevk emirleri', Proposals='Teklifler', Cheques='Çek, senet ve teminatlar', InnerTransactions='İç stok işlemleri',
    StoreAllocations='Mağaza dağıtımı', StoreTransferPlans='Mağaza transfer planları', Surveys='Anketler', Cost='Maliyet işlemleri',
    Payroll='Personel işlemleri', ItemTransactions='Stok işlem tanımları', ApplicationCommon='Ortak tanımlar', ImportExport='İthalat/ihracat',
    Requisitions='Talepler', FixedAssets='Sabit kıymetler', HR='İnsan kaynakları')

LABELS = {
1:'Nebim kullanıcısıyla giriş',2:'Müşteri',3:'Perakende müşteri',4:'Ürün',28:'Malzeme',29:'Sabit kıymet',30:'Destek talebi',31:'Personel',
32:'Kayıtlı rapor/sorgu çalıştırma',33:'İzinli prosedür çalıştırma',34:'Sipariş iptali',35:'Muhasebe fişi',36:'Destek ürününü mağazaya transfer',
37:'Destek ürününü depolar arasında transfer',38:'Virman',39:'Perakende sipariş indirimi',40:'Fatura indirimi',41:'Kur farkı faturası',
42:'Destek ürününü müşteriye çıkış',43:'Ürün rezervasyonu',44:'Ertelenmiş fatura',45:'Taksit ödeme kapatma',46:'Fiyat listesi',47:'İndirim puanı',
48:'İade faturası indirimi',49:'İade siparişi indirimi',59:'Mağazalar arası transfer',68:'Hediye kartı',69:'Tedarikçi',70:'Ürün bağlama',
71:'Ürün bağlantısını kaldırma',72:'Gider pusulası',73:'Mağaza ziyaretçileri',74:'Merkez banka hesabına nakit gönderme',76:'Fatura indirim izi',
77:'Perakende hediye kartı faturası',91:'Kredi kartı ödemesi',92:'Müşteri ek masrafı',93:'Perakende müşteri ek masrafı',94:'Tedarikçi ek masrafı',
98:'Banka havalesi / EFT',99:'Kasa giriş/çıkışı',100:'Borç dekontu',101:'Alacak dekontu',109:'Depolar arası transfer',110:'Müşteri deposu transferi',
111:'Mağaza dağıtımı',112:'Transfer planı',113:'Dinamik özellik tanımı',114:'Renk tanımı',115:'Birinci ürün boyutu',116:'İkinci ürün boyutu',
117:'Üçüncü ürün boyutu',118:'Satış temsilcisi',119:'Depo sayımı',120:'Müşteri deposu sayımı',121:'Mağaza siparişi',122:'Banka fon havalesi / EFT',
123:'Anket yanıtı',124:'Diğer tüketim',125:'Diğer üretim',126:'İndirim çeki',127:'Bildirilen konsinye satış',128:'Bildirilen distribütör satışı',
129:'Potansiyel müşteri',130:'Alınan çek',131:'Çek hareketi',142:'Sayım denkleştirme',143:'Müşteri deposu sayım denkleştirme',144:'Stok düzeltme',
145:'Alacak senedi',146:'Borç senedi',147:'Senet hareketi',148:'Mağaza süreç engelleri',149:'Banka hesap hareketleri',150:'Mağaza',
151:'Gümrükten mal transferi',152:'Potansiyel müşteriye toptan satış teklifi',153:'Personel kasa işlemleri',154:'Personel banka işlemleri',
155:'Personel gider alış faturası',156:'Perakende iade ödemesi',157:'Teklif onaylama / onay kaldırma',158:'Teklifi toptan satış siparişine dönüştürme',
159:'Potansiyel müşteri teklifini siparişe dönüştürme',160:'Banka ödeme talimatı',161:'Gider tahakkuku',162:'İç işlem maliyet düzeltmesi',
163:'Fatura maliyet düzeltmesi',164:'Müşteri süreç engelleri',165:'Toptan sipariş indirimi',166:'Sipariş indirim izi',
167:'Lojistik firmasına müşteri iade bildirimi',168:'Lojistik firmasına ürün talebi bildirimi',169:'Lojistik firmasına tedarikçi iade bildirimi',
170:'Siparişe bağlı ertelenmiş fatura',171:'Toplu fatura indirim izi ekleme',172:'Toplu sipariş indirim izi ekleme',173:'Taksitli fatura indirimi',
174:'Alınan teminat mektubu',179:'Lojistik firmasına perakende müşteri iade bildirimi',180:'Ürün seri numarası havuzu',181:'Personel zimmeti',
182:'Sevkiyat yöntemi',183:'Sürücü',184:'Araç',185:'Dağıtım görevlisi',186:'Tedarikçi fiyat listesi',187:'Ülke',188:'Bölge / eyalet',189:'Şehir',
190:'İlçe',191:'Mahalle',192:'Sokak',193:'Departman makbuzu',194:'İhracat dosyası',195:'Gider satış faturası',196:'Başka ürüne stok transferi',
197:'Anlık toptan satış rezervasyonu',198:'Teklifi toplu alış siparişine dönüştürme',199:'Teklifi gider alış siparişine dönüştürme',
200:'Teklifi ithalat alış siparişine dönüştürme',201:'Teklifi ihracat satış siparişine dönüştürme',202:'Araca yükleme',203:'Araçtan indirme',
204:'Anlık perakende rezervasyonu',205:'Kısmi taksit ödemesi kapatma',206:'Destek ürününü tedarikçiye çıkış',207:'Planet Payment toptan faturası',
208:'Çevrimiçi taksit ödemesi',209:'Toptan hediye kartı faturası',210:'Satın alma talebi',211:'Stoksuz gelen e-İrsaliye',212:'Stoklu gelen e-İrsaliye',
213:'Stoksuz giden e-İrsaliye',214:'Stoklu giden e-İrsaliye',215:'Muhasebe hesabı',216:'Kredi kartıyla gider alış faturası',
217:'Global Blue toptan faturası',218:'Global Blue Web toptan faturası',219:'Geçici görevlendirme planı',220:'Açık siparişe anlık toptan rezervasyon',
221:'Toplu indirim çeki oluşturma',222:'Teslimat tutarı hesaplama',223:'İş adayı',224:'İş görüşmesi',225:'Sabit kıymet alış faturası',
226:'Sabit kıymet satış faturası',227:'Lot tanımı',228:'Mikro ihracat perakende siparişi',229:'Banka iç transferi',230:'Mikro ihracat perakende faturası',
231:'Anlık mağaza transfer rezervasyonu',232:'Anlık konsinye rezervasyonu',233:'Anlık distribütör rezervasyonu',234:'Anlık ihracat rezervasyonu',
235:'Destek talebi onaylama / onay kaldırma',236:'Müşteri listesi',237:'Toptan satış araç yükleme',238:'Sipariş ASN onaylama / onay kaldırma'}
SUFFIX = {'WS':'Toptan satış','R':'Perakende satış','BP':'Toplu alış','CP':'Konsinye alış','CS':'Konsinye satış','DS':'Distribütör satışı',
          'EP':'Gider alış','ES':'İhracat satış','IP':'İthalat alış','RI':'Taksitli perakende satış','SS':'Hizmet satışı','ST':'Mağaza transferi',
          'RFS':'Mağazadan talep','RSD':'Sonradan teslim perakende satış'}
PREFIX = {'Order':'siparişi','Invoice':'faturası','Shipment':'irsaliyesi','Reservation':'rezervasyonu','DispatchOrder':'sevk emri',
          'Picking':'toplama emri','Proposal':'teklifi','OrderAsn':'sipariş ASN bildirimi','InstantShipment':'anlık irsaliyesi',
          'InstantShipmenWithRemainings':'kalanlarla anlık irsaliyesi','InstantOrderShipment':'siparişten anlık irsaliyesi'}
for model in models:
    if model['code'] in LABELS:
        continue
    for prefix in sorted(PREFIX, key=len, reverse=True):
        if model['name'].startswith(prefix) and model['name'][len(prefix):] in SUFFIX:
            LABELS[model['code']] = SUFFIX[model['name'][len(prefix):]] + ' ' + PREFIX[prefix]
            break
    assert model['code'] in LABELS, model['name']

def type_anchor(name):
    return 't-' + hashlib.sha256(name.encode()).hexdigest()[:12]

def innertype(name):
    if name.endswith('[]'):
        return name[:-2]
    if '<' in name:
        inner = name[name.index('<')+1:name.rindex('>')]
        return None if ',' in inner else inner
    t = types.get(name, {})
    return t.get('element')

def scalar(field):
    name, typ = field['name'], field['type']
    if 'Nullable<' in typ:
        typ = innertype(typ)
    if typ == 'System.Boolean': return False
    if typ in ('System.DateTime', 'System.DateTimeOffset'): return '2026-01-01T00:00:00'
    if typ == 'System.TimeSpan': return '00:00:00'
    if typ == 'System.Guid': return '{{exampleGuid}}'
    if typ in ('System.Byte','System.SByte','System.Int16','System.Int32','System.Int64','System.UInt16','System.UInt32','System.UInt64','System.Decimal','System.Double','System.Single'):
        return 1 if name in ('Qty1','Quantity','CompanyCode','ItemTypeCode','Price','Amount') else 0
    if types.get(typ, {}).get('enum'):
        return next((v['value'] for v in types[typ]['values'] if isinstance(v.get('value'),(int,float))), 0)
    if typ == 'System.String':
        if name in ('CurrencyCode','DocCurrencyCode','LocalCurrencyCode'): return 'TRY'
        if name in ('DataLanguageCode','LangCode'): return 'TR'
        if name in ('FirstName','LastName','Description','ItemDescription','CurrAccDescription','LineDescription'):
            return 'ÖRNEK ' + name
        variables.setdefault(name, '')
        return '{{' + name + '}}'
    return None

PRIORITY = ['ModelType','CurrAccCode','CustomerCode','VendorCode','EmployeeCode','CustomerCode','ItemCode','OrderNumber','InvoiceNumber','ShipmentNumber','Code','AttributeCode','Description',
 'FirstName','LastName','CurrAccDescription','ItemDescription','CompanyCode','OfficeCode','StoreCode','WarehouseCode','CurrencyCode',
 'OperationDate','OrderDate','InvoiceDate','DocumentDate','IsReturn','ItemTypeCode','ColorCode','ItemDim1Code','Qty1','Price',
 'PaymentType','BasePriceCode','LangCode','AddressTypeCode','CountryCode','StateCode','CityCode','DistrictCode','Address',
 'BankCurrAccCode','BankAccountCode','BankTransNumber','CashAccountCode','DocCurrencyCode','LocalCurrencyCode',
 'Debit','Credit','Amount','Rate','DueDate','PaymentDate','OperationTime','OrderTime','InvoiceTime','Qty2','ItemDim2Code','ItemDim3Code',
 'ProductTypeCode','ItemDimTypeCode','UnitOfMeasureCode1','ItemTaxGrCode','ProposalNumber','ReservationNumber','PriceListNumber',
 'VendorPriceListNumber','GLAccCode','DocumentNumber','ShipmentMethodCode','RefNumber']

def sample_type(name, direction='input', depth=0, seen=(), brief=True):
    t = types.get(name)
    if not t or name in seen or depth > 2: return {}
    fields = [f for f in t.get('fields',{}).values() if f.get(direction)]
    fs = {f['name']:f for f in fields}
    scalar_fields = [f for f in fields if f.get('kind') not in ('nested-collection','nested-element','foreign-object','excluded')]
    priority = ['ItemTypeCode','ItemCode','ColorCode','ItemDim1Code','ItemDim2Code','ItemDim3Code','Qty1','Qty2','Price','Amount','CurrencyCode']+PRIORITY if 'ItemCode' in fs and ('Qty1' in fs or 'Price' in fs) else PRIORITY
    order = sorted(scalar_fields, key=lambda f: (0 if f.get('key') else 1, priority.index(f['name']) if f['name'] in priority else len(priority), f['name']))
    if brief:
        important=[f for f in order if f.get('key') or f['name'] in priority]
        fallback=[f for f in order if f not in important and f['type']!='System.Boolean']
        order=(important+fallback[:max(0,6-len(important))])[:(24 if depth==0 else 12)]
    out = {}
    for field in order:
        v = scalar(field)
        if v is not None: out[field['name']] = v
    if depth < 2:
        names = ['Lines','Descriptions','PostalAddresses','Communications','Contacts','CostLines','Parameters']
        chosen = [fs[n] for n in names if n in fs and fs[n].get('kind') in ('nested-collection','nested-element')][:2]
        for field in chosen:
            target = innertype(field['type']) if field['kind']=='nested-collection' else field['type']
            if target in types:
                value = sample_type(target,direction,depth+1,seen+(name,),brief)
                out[field['name']] = [value] if field['kind']=='nested-collection' else value
    return out

def envelope(status,message):
    return {'ModelType':0,'ExceptionMessage':message,'StackTrace':'','ErrorSource':'NebimV3IntegratorService','StatusCode':status}

ERRORS=[
 {'id':'auth','title':'Giriş bilgileri doğrulanamadı','status':400,'message':'IncorrectUserNameOrPasswordException','meaning':'Kullanıcı grubu, Nebim kullanıcısı/parolası veya veritabanı erişimi doğrulanamadı. HTTP durumuyla birlikte gövdedeki StatusCode kontrol edilir.','action':'Nebim hesabını ve DatabaseName bilgisini doğrulayın; SQL hesabı/parolasını kullanıcı girişiyle karıştırmayın.'},
 {'id':'token','title':'Geçersiz / süresi dolmuş oturum','status':'Değişken','message':'session is invalid or expired','meaning':'URL tokenı geçersiz, kaldırılmış veya oturum süresi dolmuş olabilir. invalid token mesajı da görülebilir.','action':'Connect ile oturum oluşturun; tokenı URL segmentinde gönderin. Belirsiz bir yazmayı otomatik tekrar göndermeyin.'},
 {'id':'model','title':'Model / alan / iş kuralı reddi','status':400,'message':'TEMSiLi_IS_KURALI_HATASI','meaning':'Yanlış ModelType, controller/model uyuşmazlığı, alan türü, eksik anahtar, bloke kod veya iş doğrulaması isteği reddedebilir. Mesaj temsili olup bütün modellerin gerçek hata metni değildir.','action':'Modelin somut tipini, endpointini ve kurulumdaki referans kodlarını kontrol edin.'},
 {'id':'missing','title':'Kayıt bulunamadı','status':400,'message':'RecordNotFoundException','meaning':'İstenen iş anahtarıyla kayıt yüklenemedi. Yerelleştirilmiş metinde tablo ve anahtar bulunabilir; metin burada temsili gösterilir.','action':'Doğru yazılabilir anahtar veya modelin belge numarası yoluyla okuyun; her modele aynı HeaderID/Code alanını göndermeyin.'},
 {'id':'relation','title':'SQL ilişki / kayıt doğrulama hatası','status':400,'message':'TEMSiLi_ILISKI_HATASI','meaning':'Olmayan referans, ilişki kısıtı veya iş doğrulaması kaydı engelleyebilir. Birden çok hata && ile birleşebilir; Message/Detail JSON metni içerebilir.','action':'İlgili tanım kodlarını ve iş anahtarlarını kontrol edin. JSON Detail içindeki && nedeniyle yalnız metin bölmeyle kesin hata sayısı çıkarmayın.'},
 {'id':'json','title':'Gövde / binder sorunu','status':'Değişken','message':'TEMSiLi_JSON_BINDER_HATASI','meaning':'Özgün binder geçersiz JSON’u boş modele çevirebilir; görünen eksik ModelType hatasının asıl nedeni bozuk gövde olabilir.','action':'Doğrudan JSON ve UTF-8 application/json kullanın. GET/PUT binder davranışını standart POST gibi varsaymayın.'},
 {'id':'queue','title':'Kuyruk anahtarı çakışması','status':409,'message':'TEMSiLi_IDEMPOTENT_KEY_CAKISMASI','meaning':'Idempotent-Key daha önce request/response kuyruğunda bulunmuş olabilir. Yanıt düz metin olabilir; ilk başarı otomatik tekrar döndürülmez.','action':'Queue/Read veya iş anahtarıyla ilk işlemi kontrol edin; farklı anahtarla körlemesine tekrar yazmayın.'},
 {'id':'async','title':'Asenkron istek kabulü','status':202,'message':'request accepted','meaning':'Call-Type:Async ve kuyruk anahtarıyla kabul yanıtı, iş kaydının tamamlandığını kanıtlamaz. Worker akışı bu sözleşme incelemesinde sertifikalanmamıştır.','action':'Kuyruk sonucunu izleyin;202 yanıtını kayıt başarı yanıtı olarak işlemeyin.'},
 {'id':'queue-missing','title':'Kuyruk kaydı bulunamadı','status':404,'message':'TEMSiLi_KUYRUK_KAYDI_YOK','meaning':'Queue/Read için request/response dosyası bulunamamış olabilir. Bu evrensel entity GetModel hata kodu değildir.','action':'Doğru kuyruk anahtarını ve işlem durumunu kontrol edin.'}
]
SPECIAL = {}
def special(code,path,body,description,response='echo'):
    SPECIAL[code] = {'path':path,'body':dict(ModelType=code,**body),'description':description,'responseKind':response}

special(1,'/IntegratorService/Connect',{'DatabaseName':'{{DatabaseName}}','UserGroupCode':'{{UserGroupCode}}','UserName':'{{UserName}}','Password':'{{Password}}','Validate':True},'Nebim kullanıcısını doğrular ve token oluşturur. Validate=true ile giriş doğrulanmalıdır; session/auto-login davranışı kuruluma bağlıdır.','login')
special(32,'/IntegratorService/RunQuery/{token}',{'ReportName':'V3Integrator','QueryName':'{{QueryName}}','Criteria':'','Skip':0,'Take':100},'Kayıtlı rapor/sorgu çalıştırır; keyfi SQL gövdesi değildir. Sonuç kolonları rapora bağlıdır.','rows')
special(33,'/IntegratorService/RunProc/{token}',{'ProcName':'{{ProcName}}','Parameters':[{'Name':'@Kod','Value':'{{ParameterValue}}'}]},'Saklı prosedür çalıştırır. Özgün servis ProcName ve Parameters alanlarını kullanır; prosedürün salt okunur olduğu varsayılmaz.','rows')
special(34,'/IntegratorService/Post/{token}',{'OrderNumber':'{{OrderNumber}}','CancelDate':'2026-01-01','Lines':[{'LineID':'{{exampleGuid}}','Qty1':1,'Qty2':0,'OrderCancelReasonCode':'{{OrderCancelReasonCode}}','LineDescription':'ÖRNEK İPTAL'}],'Description':'ÖRNEK İPTAL'},'OrderNumber veya OrderHeaderID ile sipariş seçer; iptal satırlarını işler. Başarı kök istek nesnesidir.')
for code in (70,71):
    special(code,'/InnerService/Post/{token}',{'OperationDate':'2026-01-01','OperationTime':'00:00:00','OfficeCode':'{{OfficeCode}}','StoreCode':'{{StoreCode}}','InWarehouseCode':'{{InWarehouseCode}}','OutWarehouseCode':'{{OutWarehouseCode}}','ProductCode':'{{ProductCode}}','Qty1':1,'ITAttributes':{}},'Ürün bağlama/bağlantı kaldırma işlemi. ITAttributes içindeki ITAttNN alanları kurulumdaki özellik tiplerinden gelir; örnekte uydurulmaz.')
special(113,'/IntegratorService/Post/{token}',{'ObjectName':'Customer','AttributeTypeCode':1,'AttributeCode':'{{AttributeCode}}','AttributeDescription':'ÖRNEK ÖZELLİK'},'ObjectName ve AttributeTypeCode ile dinamik attribute entity oluşturur. Örnekte katalogda bulunan CustomerAttribute seçilir; tip kodu kurulumda doğrulanmalıdır.','attribute')
special(156,'/IntegratorService/Post/{token}',{'CustomerTypeCode':4,'CustomerCode':'{{CustomerCode}}','PaymentHeaderID':'{{exampleGuid}}','POSTerminalID':0,'Payments':[]},'Perakende iade ödemesi. Payments burada boş şema yeridir; ödeme türüne göre somut satır alanları ayrıca gerekir.')
for code,key,path in [(157,'ProposalHeaderID','Proposal'),(235,'SupportRequestHeaderID','ProductSupport'),(238,'OrderAsnHeaderID','Shipment')]:
    special(code,f'/{path}Service/Post/{{token}}',{'IsConfirmed':True,'HeaderIDs':[{key:'{{exampleGuid}}'}]},'IsConfirmed ile onayı açar/kaldırır. HeaderIDs boş olamaz; sonuç kök istek nesnesidir.')
for code in (158,159,198,199,200,201):
    special(code,'/ProposalService/Post/{token}',{'ProposalNumber':'{{ProposalNumber}}','OrderDate':'2026-01-01','OrderTime':'00:00:00','OfficeCode':'{{OfficeCode}}','WarehouseCode':'{{WarehouseCode}}','CreateReservation':False,'ReApplyDiscountOffers':False,'PriceOption':0},'Teklifi modelin belirttiği sipariş türüne dönüştürür. Başarı istek nesnesidir; oluşan sipariş kimliği bu yanıta eklenmez.')
special(163,'/AdjustCostService/Post/{token}',{'ProcessCode':'{{ProcessCode}}','AdjustCostMethodCode':4,'AdjustCostInvoices':[{'InvoiceNumber':'{{InvoiceNumber}}','CostLines':[{'LineID':'{{exampleGuid}}','IncreaseAmount':1,'ReduceAmount':0}]}]},'Fatura maliyet düzeltmesi; yöntem4 artırımı,8 azaltımı okur. Örnek yalnız kanıtlanmış özel alan parçasıdır; tam header modeli çözülmemiştir.','unknown-cost')
special(208,'/IntegratorService/Post/{token}',{'Payment':{'ModelType':45,'DebitLines':[],'Payments':[]}},'Taksit ödemesini ve varsa Invoice nesnesini işler. Alt Payment/Invoice için tam ilgili model gerekir; örnek dış sarmalı gösterir.','online')
special(222,'/IntegratorService/Post/{token}',{'CustomerAddress':{'CityName':'{{CityName}}','DistrictName':'{{DistrictName}}'},'FindDeliveryLocationSpName':'{{FindDeliveryLocationSpName}}','CalculateDeliveryAmountSpName':'{{CalculateDeliveryAmountSpName}}','Amount':1},'Adres ve kurulum prosedürleriyle teslimat tutarı hesaplar. Sonuç kolonları prosedüre bağlıdır.','delivery')

def fields_for(model):
    typ = 'NebimV3.Attributes.CustomerAttribute' if model['code']==113 else 'NebimV3.Cost.AdjustCostHeaderTransactionBase' if model['code']==163 else model['rootType']
    return types.get(typ,{}).get('fields',{})

def key_request(model):
    fields = fields_for(model)
    keys = [f for f in fields.values() if f.get('key') and f.get('input') and f['kind'] not in ('nested-element','nested-collection')]
    note = 'Yazılabilir metadata anahtarları; iş kuralı/varlık doğrulaması ayrıca gerekir.'
    if not keys:
        for n in ['OrderNumber','InvoiceNumber','ShipmentNumber','ProposalNumber','ReservationNumber','DispOrderNumber','PickingNumber','PriceListNumber','VendorPriceListNumber','DocumentNumber']:
            if n in fields and fields[n].get('input'):
                keys = [fields[n]]
                note = 'Yazılabilir anahtar yok; kaynak LoadEntity normal setter yolundan aday belge numarası gösterilir. Model bazında yükleme akışı doğrulanmış değildir.'
                break
    if not keys:
        return None, 'GetModel için güvenilir yazılabilir anahtar adayı çıkarılamadı; uydurma HeaderID/Code gönderilmez.'
    return dict(ModelType=model['code'],**{f['name']:scalar(f) for f in keys}),note

def md_table(fields):
    if not fields: return 'Sabit entity alan listesi yok; yukarıdaki dinamik işlem sözleşmesini kullanın.\n'
    lines = ['| Alan | CLR / JSON türü | Giriş | Çıkış | Anahtar | En fazla karakter | Not |','|---|---|---|---|---|---:|---|']
    for f in fields.values():
        typ=f['type'];target=innertype(typ) if f['kind']=='nested-collection' else typ
        href=f'[tip](TYPES.md#{type_anchor(target)})' if target in types else ''
        kind={'nested-collection':'Dizi; '+('somut satır '+href if href else 'somut satır çözülemedi'),'nested-element':'İç nesne '+(href or 'somut tip çözülemedi'),'foreign-object':'Yabancı nesne; düz kod alanıyla karıştırmayın','writable-scalar':'Scalar','read-only-scalar':'Salt okunur'}.get(f['kind'],f['kind'])
        if f.get('input') not in (True,False): kind+='; giriş koşullu'
        lines.append('| '+ ' | '.join([f['name'], '`'+typ.replace('|','\\|')+'`',str(f['input']).lower(),str(f['output']).lower(),'evet' if f.get('key') else '—',str(f.get('maxLength') or '—'),kind])+' |')
    return '\n'.join(lines)+'\n'

def response_example(model, request):
    special_model = SPECIAL.get(model['code'])
    if special_model:
        kind=special_model['responseKind']
        if kind=='echo': return request.copy(), 'Kaynakta kök istek geri döner; değerler temsili. İşlemin başarılı olduğu kanıtı değildir.'
        if kind=='login': return {'Status':'Connection Created Successfully','StatusCode':200,'Token':'{{token}}'}, 'Giriş başarı biçimi; token yer tutucudur.'
        if kind=='rows': return [{'ORNEK_KOLON':'DEGER'}], 'Şematik sonuç dizisi; ORNEK_KOLON gerçek/sabit kolon değildir. Prosedür/rapor kolonları kullanılır.'
        if kind=='online':
            result=json.loads(json.dumps(request));result['Payment']['PaymentHeaderID']='{{exampleGuid}}'
            return result,'Kaynak, kök isteğe Payment.PaymentHeaderID ekler. Invoice verilirse Invoice.InvoiceHeaderID de eklenir; alt gövdeler örnekte tamamlanmış değildir.'
        if kind=='delivery': return {'ModelType':222,'Result':[{'ORNEK_KOLON':'DEGER'}]}, 'Result kolonları kurulum prosedüründen gelir; ORNEK_KOLON yalnız gösterimdir.'
        if kind=='unknown-cost':
            # Static class export proves inheritance; recovered controller Post
            # explicitly keeps the request ModelType on the serialized result.
            names=['AdjustCostHeaderID','AdjustCostNumber','AdjustCostMethodCode','Amount','ProcessCode']
            fs=types['NebimV3.Cost.AdjustCostHeaderTransactionBase']['fields']
            value=dict(ModelType=163,**{n:scalar(fs[n]) for n in names})
            value['AdjustCostMethodCode']=request['AdjustCostMethodCode']
            return value, 'Kaynakta AdjustCostHeaderInvoice, AdjustCostHeaderTransactionBase tipinden türemiştir; controller ModelType163 değerini korur. Yalnız kanıtlanmış baz header alanlarının temsili alt kümesi gösterilir. AdjustCostInvoices ve nested sonuçların tam şeması çözümlenmiş değildir; bu bir canlı başarı yakalaması değildir.'
        if kind=='attribute': return dict(ModelType=113,**sample_type('NebimV3.Attributes.CustomerAttribute','output')), 'CustomerAttribute için metadata temsili; ObjectName başka ise sözleşme değişir.'
    return dict(ModelType=model['code'],**sample_type(model['rootType'],'output')), 'Metadata’dan türetilmiş temsili yanıt; canlı yakalama değildir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.'

def serialize_json(value):
    return '```json\n'+dump(value)+'\n```\n'

data=[]
for model in models:
    code=model['code'];s=SPECIAL.get(code)
    path=s['path'] if s else '/IntegratorService/Post/{token}'
    assert path in routes,(code,path)
    request=s['body'] if s else dict(ModelType=code,**sample_type(model['rootType']))
    for v in re.findall(r'\{\{(\w+)\}\}',dump(request)):variables.setdefault(v,'')
    response,response_note=response_example(model,request)
    key,key_note=key_request(model) if not s else (None,'Özel işlem için genel GetModel/Delete gövdesi uydurulmaz.')
    description=s['description'] if s else f"{LABELS[code]} için {FAMILIES.get(model['family'],model['family'])} grubundaki model. Somut factory tipi {model['rootType']}. Referans kodları, yetki/lisans ve iş kuralları kuruluma bağlıdır."
    item={'code':code,'name':model['name'],'title':LABELS[code],'family':FAMILIES.get(model['family'],model['family']),
      'rootType':model['rootType'],'alternativeTypes':model['alternativeTypes'],'lineTypes':model['lineTypes'],
      'description':description,'path':path,'method':'POST','request':request,'response':response,'responseNote':response_note,
      'getRequest':key,'keyNote':key_note,'fieldType':'NebimV3.Attributes.CustomerAttribute' if code==113 else 'NebimV3.Cost.AdjustCostHeaderTransactionBase' if code==163 else model['rootType'],
      'factoryDisposition':model['factoryDisposition'],'sourceOperation':model['operation'],'restrictedControllers':model['restrictedControllers'],
      'special':bool(s),'exampleEvidence':'source-operation-template' if s else 'metadata-template'}
    data.append(item)
    write(f'examples/{code:03d}-{model["name"]}.request.json',dump(request)+'\n')
    write(f'examples/{code:03d}-{model["name"]}.response.json',dump(response)+'\n')

header="""# Özgün Nebim V3 Entegratör — 238 model API rehberi

Referans sürüm **25.4.1.0**. Kodlar **1–238** eksiksiz kapsanır. **0 / None** işlem modeli olmayan sentinel’dır.

Bu paket yalnız özgün IIS üzerinde çalışan Nebim V3 Entegratör HTTP sözleşmesini belgeler. Bağımsız, resmi olmayan teknik referanstır. Örnekler kaynak/metadata şablonudur;238 başarılı canlı işlem yakalaması veya bütün iş kurallarını karşılayan istek garantisi değildir. Gövdeler önemli alanların alt kümesini gösterir; tam alan envanteri model tabloları ve TYPES.md içindedir. Bilinmeyen zorunluluklar, varsayılanlar, dinamik tipler ve prosedür kolonları uydurulmaz.

## Kullanım

- [Aranabilir çevrimdışı rehber](index.html), [tip sözlüğü](TYPES.md), [sözleşme verisi](contracts.json).
- [Postman koleksiyonu](Nebim-V3-238-model.postman_collection.json) ve [ortam dosyası](Nebim-V3.postman_environment.json) birlikte içe aktarılır.
- baseUrl özgün Entegratör adresidir; sanal IIS uygulama dizini varsa korunur. Varsayılan localhost:3019 yalnız örnektir.
- DatabaseName, UserGroupCode, UserName, Password ortamda doldurulur. Connect tokenını test betiği seçili ortama aktarır. Gerçek parola/token/sunucu IP’si veya müşteri verisi pakete gömülmez.
- Sayısal0/1, örnek tarihler ve GUID’ler varsayılan/iş kuralı iddiası değildir. Yer tutucuları geçerli tanım kodları ve gerçek işlem kimlikleriyle değiştirin.
- Post oluşturma/güncelleme; Delete, iptal, onay, dönüştürme ve ödeme işlemleri veri değiştirebilir. Paket hazırlanırken servis/SQL işlemi yapılmadı.

## Giriş ve HTTP

POST /IntegratorService/Connect doğrudan JSON alır. ModelType1, DatabaseName, UserGroupCode, UserName, Password, Validate:true kullanılır. DatabaseServer kuruluma göre eklenebilir. Nebim hesabı ile SQL hesabı farklıdır. Validate false/eksik ise özgün ayar ve auto-login akışına göre doğrulama ertelenebilir; token varlığını tek başına başarılı kimlik doğrulama saymayın.

Content-Type: application/json; charset=utf-8. {"model":...} zarfı veya /api/ öneki yoktur. URL tokenı JWT/Bearer değildir. Cookie/session kurulumları farklılaşabilir. GET/PUT binder davranışı POST ile aynı değildir; gövdeli örnekler POST kullanır.

Başarı evrensel data zarfına sahip değildir: entity, dizi, JSON string, null veya özel işlem nesnesi olabilir. Hata bazı yollarda HTTP200 ile gelebilir; ExceptionMessage, Exception ve gövdedeki StatusCode birlikte denetlenir. Generic null scalar yanıt alanı atlanabilir; yokluk, null,0,false eşit sayılmamalıdır. Enum/model sayısal, decimal JSON sayı, GUID metindir. ISO tarih istekleri ve özgün /Date(milisaniye)/ yanıtları ayrı ele alınır.

GetModel yazılabilir iş anahtarlarıyla Load çağırır; yazılabilir anahtar yoksa normal setter yolunu kullanır. Her modele aynı HeaderID/Code atanmaz. NewModel yalnız {"ModelType":N} döndürür; tam şablon değildir. Koleksiyondan bir satırı çıkarmak silme talebi değildir; kaynak generic IsDeleted akışı ve modelin silme kuralları geçerlidir. POST canlı nesne ile GetModel yeniden yüklenen nesne farklı olabilir.

## Hatalar

Özgün global hata zarfının örnek biçimi:

```json
{"ModelType":0,"ExceptionMessage":"HATA_METNI","StackTrace":"","ErrorSource":"NebimV3IntegratorService","StatusCode":400}
```

StackTrace Base64 UTF-8 olabilir; InnerException iç içe gelebilir. Hassas SQL, parola, token ve müşteri gövdelerini loga taşımayın. Aşağıdaki sınıflar bütün lisans/iş doğrulama hatalarının eksiksiz kataloğu değildir. Temsili mesajlar gerçek yerelleştirilmiş hata metni olarak sunulmaz. HTTP durumu, gövdedeki StatusCode ve endpoint ayrımı korunur.

| Hata | Örnek durum | Açıklama | İstemci davranışı |
|---|---|---|---|
"""
for e in ERRORS:header+=f"| {e['title']} | {e['status']} | {e['meaning']} | {e['action']} |\n"
header+='\n## Model dizini\n\n| Kod | Model | Tanıtım |\n|---:|---|---|\n'
for m in data:header+=f"| {m['code']} | [{m['name']}](#model-{m['code']}) | {m['title']} |\n"
sections=[]
for m in data:
    text=f'\n<a id="model-{m["code"]}"></a>\n\n## {m["code"]} — {m["name"]} / {m["title"]}\n\n{m["description"]}\n\n'
    text+=f"Somut kök: `{m['rootType'] or 'Özel / dinamik işlem'}`. Grup: {m['family']}. Örnek kanıtı: `{m['exampleEvidence']}`.\n\n"
    if m['lineTypes'] or m['alternativeTypes'][1:]:text+='Alternatif kök / somut satır tipleri: '+', '.join('`'+n+'`' for n in m['alternativeTypes'][1:]+m['lineTypes'])+'. Factory daha özel satır seçebilir; bütün varyantların eksiksizliği sertifikalanmamıştır.\n\n'
    if m['restrictedControllers']:text+='Kısıtlı controller kabul envanteri: '+', '.join('`'+n+'`' for n in m['restrictedControllers'])+'. Kabul listesi, tüm action/CRUD işlemlerinin başarı garantisi değildir.\n\n'
    text+=f"### Örnek request\n\n`POST {{{{baseUrl}}}}{m['path'].replace('{token}','{{token}}')}`\n\nKaynak/metadata şablonu; kurulumdaki zorunlu kodlar ayrıca doldurulur.\n\n"+serialize_json(m['request'])
    text+='\n### Örnek response\n\n'+m['responseNote']+'\n\n'+serialize_json(m['response'])
    if m['code']==33:text+='\nRunProcReturnSingle aynı gövdeyle ilk satır nesnesi veya null döndürür. Prosedür kolonları ve yan etkileri tanıma bağlıdır; read-only olduğu varsayılmaz.\n'
    text+='\n### Okuma / silme / şablon\n\n'+m['keyNote']+'\n\n'
    if m['getRequest'] is not None:
        text+='`POST {{baseUrl}}/IntegratorService/GetModel/{{token}}`\n\n'+serialize_json(m['getRequest'])
        text+='\nDelete aynı iş anahtarıyla /IntegratorService/Delete/{token} üzerinden modelin kaynak silme kurallarını uygular. Lisans/yetki, kilitli/korunan kayıtlar ve FK davranışı ayrıca geçerlidir; generic cascade varsayılmaz.\n'
    text+=f'\n`GET {{{{baseUrl}}}}/IntegratorService/NewModel?modelType={m["code"]}` → `{{"ModelType":{m["code"]}}}`.\n'
    text+='\n### Modelde hata değerlendirmesi\n\nGiriş/oturum, model ve alan türü, kayıt bulunamaması, referans/iş doğrulaması ve lisans/yetki koşulları ortak [Hatalar](#hatalar) bölümünde açıklanır. Bunlar bu modelde canlı denenmiş bütün hata metinleri değildir. Yanıttaki ModelType0 istek ModelType değerini0 yapmanız gerektiğini göstermez. Timeout/kuyruk belirsizliğinde önce ilk işlemi sorgulayın; otomatik tekrar yazmayın.\n'
    text+='\n### Giriş / çıkış alanları\n\ntrue: sözleşmede var; false: yok; diğer: koşullu. Anahtar metadata bilgisidir; salt okunur scalar ile getter-only koleksiyon ayrıdır. Uzunluk bilinmiyorsa sınırsızlık, alan listesi zorunluluk/varsayılan iddiası değildir.\n\n'+md_table(fields_for(registry['models'][m['code']]))
    if m['special']:text+='\nÖzel işlemde dinamik gövde esas alınır. Model163 tablosu yalnız doğrulanan baz header alanlarını,113 tablosu seçilen CustomerAttribute örneğini gösterir; selector ve özel nested gövdeler ayrıca ele alınır.\n'
    page=text.replace('](TYPES.md#','](../TYPES.md#').replace('](#hatalar)','](../HTTP-AND-ERRORS.md#hatalar)')
    write(f'models/{m["code"]:03d}-{m["name"]}.md','[Model dizinine dön](../MODELS.md) · [HTTP ve hatalar](../HTTP-AND-ERRORS.md)\n'+page)
    sections.append(text)
write('HTTP-AND-ERRORS.md',header.split('## Model dizini')[0])
index='# Özgün Nebim V3 Entegratör — model dizini\n\n[HTTP, giriş ve hata rehberi](HTTP-AND-ERRORS.md) · [Tam çevrimdışı Markdown](ALL-MODELS.md) · [Aranabilir HTML](index.html)\n\n238 modelin her biri ayrı sayfadadır. Örnekler kaynak/metadata şablonudur; canlı başarı garantisi değildir.\n\n| Kod | Model | Tanıtım |\n|---:|---|---|\n'
for m in data:index+=f'| {m["code"]} | [{m["name"]}](models/{m["code"]:03d}-{m["name"]}.md) | {m["title"]} |\n'
write('MODELS.md',index)
write('ALL-MODELS.md',header+'\n'.join(sections)+'\n## 0 — None\n\nİşlem modeli olmayan sentinel; hata yanıtındaki ModelType0 ile karıştırılmamalıdır.\n')
type_lines=['# Alt nesne ve tip sözlüğü','',f'{len(types)} metadata tipi. Koleksiyon container özellikleri JSON dizi satırı değildir; örnek gövdeler somut element tipini kullanır. Enum değerleri yalnız metadata’dır; alan/kurulum geçerliliği ayrıca kontrol edilir.','']
for name,t in sorted(types.items()):
    type_lines += [f'<a id="{type_anchor(name)}"></a>','',f'## {name}','',f"Baz tip: `{t.get('base') or '—'}`. Entity:{t.get('isEntity')}; element:{t.get('isElement')}; collection:{t.get('isCollection')}.",'']
    if t.get('enum'):
        type_lines+=['| Enum | Değer |','|---|---|']+[f"| {v['name']} | {v['value']} |" for v in t.get('values',[])]+['']
    elif t.get('isCollection'):
        element=t.get('element'); type_lines+=[f"JSON taşıma biçimi: array. Somut eleman: [{element}](#{type_anchor(element)})" if element in types else f"Somut eleman çözülemedi: `{element}`; satır alanları uydurulmaz.",'']
    else: type_lines += [md_table(t.get('fields',{})),'']
write('TYPES.md','\n'.join(type_lines))

def postman_item(name,path,body=None,response=None,note='',status=200,method='POST'):
    raw='{{baseUrl}}'+path.replace('{token}','{{token}}')
    req={'method':method,'header':[{'key':'Content-Type','value':'application/json; charset=utf-8'}],
         'url':raw,'description':note}
    if body is not None: req['body']={'mode':'raw','raw':dump(body),'options':{'raw':{'language':'json'}}}
    item={'name':name,'request':req,'response':[]}
    if response is not None:
        item['response'].append({'name':'ŞABLON — canlı yakalama değildir','originalRequest':req,'status':'OK' if status==200 else 'Not Implemented',
            'code':status,'header':[{'key':'Content-Type','value':'application/json; charset=utf-8'}],'body':dump(response),'_postman_previewlanguage':'json'})
    return item

folders=[]
for m in data:
    items=[postman_item('POST — kaynak/metadata örneği',m['path'],m['request'],m['response'],m['description']+'\n'+m['responseNote'])]
    if m['code']==1:items[0]['event']=[{'listen':'test','script':{'type':'text/javascript','exec':[
        'let body; try { body = pm.response.json(); } catch (_) { body = null; }',
        'if (body && body.Token && !body.ExceptionMessage && body.StatusCode === 200) { pm.environment.set("token", body.Token); }',
        'pm.test("Giriş başarı yanıtı", function () { pm.expect(body && body.StatusCode).to.eql(200); });']}}]
    if m['getRequest'] is not None:
        items.append(postman_item('GetModel — anahtar örneği','/IntegratorService/GetModel/{token}',m['getRequest'],None,m['keyNote']))
        items.append(postman_item('Delete — kaynak silme kuralları','/IntegratorService/Delete/{token}',m['getRequest'],None,'Veri değiştirebilir. Modelin lisans/yetki ve kaynak silme kuralları ayrıca geçerlidir.'))
    items.append(postman_item('NewModel — yalnız ModelType',f'/IntegratorService/NewModel?modelType={m["code"]}',None,{'ModelType':m['code']},'Tam DTO değildir.',method='GET'))
    if m['code']==33:items.append(postman_item('RunProcReturnSingle','/IntegratorService/RunProcReturnSingle/{token}',m['request'],None,'İlk satır nesnesi veya null.'))
    folders.append({'name':f"{m['code']:03d} {m['name']} — {m['title']}",'description':m['description'],'item':items})
collection={'info':{'name':'Özgün Nebim V3 Entegratör25.4.1.0 —238 model','schema':'https://schema.getpostman.com/json/collection/v2.1.0/collection.json',
 'description':'Yalnız özgün Nebim V3 Entegratör. Kaynak/metadata şablonları; canlı başarı garantisi değildir. Önce ALL-MODELS.md okuyun.'},
 'variable':[{'key':'baseUrl','value':variables['baseUrl'],'type':'string'}],'item':folders}
environment={'name':'Özgün Nebim V3 — doldurulacak ortam','values':[{'key':k,'value':v,'enabled':True,'type':'secret' if k in ('Password','token') else 'default'} for k,v in variables.items()],'_postman_variable_scope':'environment'}
write('Nebim-V3-238-model.postman_collection.json',dump(collection)+'\n')
write('Nebim-V3.postman_environment.json',dump(environment)+'\n')
document={'referenceVersion':registry['referenceVersion'],'modelCount':238,'typeCount':len(types),'models':data,'types':types,'errors':ERRORS,
 'generatedDate':dt.datetime.now(dt.timezone.utc).date().isoformat(),'liveRequestsSent':False,
 'sources':registry['provenance']+[{'name':'Bundled original-service contract snapshot','sha256':sha(ROOT/'data/source-contracts.json')}],
 'limitations':['Metadata examples are not live success captures','Model163 success shows only proven base header fields','Dynamic/procedure columns and unclassified nested types remain explicit gaps']}
write('contracts.json',dump(document)+'\n')
template=(ROOT/'tools/templates/reference.html').read_text(encoding='utf-8')
write('index.html',template.replace('__DATA__',json.dumps(document,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c').replace('&','\\u0026')))
assert len(folders)==238 and [m['code'] for m in data]==list(range(1,239))
assert len(list((OUT/'examples').glob('*.request.json')))==238
assert len(list((OUT/'examples').glob('*.response.json')))==238
assert len(list((OUT/'models').glob('*.md')))==238
for p in OUT.rglob('*.json'):read(p)
for p in [OUT/'ALL-MODELS.md',OUT/'TYPES.md',OUT/'index.html']:
    assert '\ufffd' not in p.read_text(encoding='utf-8'),p
validation={'passed':True,'models':238,'types':len(types),'postmanModelFolders':238,'postmanRequests':sum(len(f['item']) for f in folders),
 'requestExampleFiles':238,'responseExampleFiles':238,'individualModelPages':238,'partialSuccessSchemas':[163],
 'scope':'Original-service documentation only; offline coverage/JSON/source-route checks, not live execution','sqlOrHttpRequestsSent':False,'sources':document['sources']}
write('validation.json',dump(validation)+'\n')
node=shutil.which('node') or ('C:/Program Files/nodejs/node.exe' if Path('C:/Program Files/nodejs/node.exe').exists() else None)
if node:subprocess.run([node,str(ROOT/'tools/verify_docs.mjs')],cwd=ROOT,check=True)
archives=ROOT/'artifacts';archives.mkdir(exist_ok=True)
with zipfile.ZipFile(archives/'nebim-v3-integrator-docs.zip','w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(OUT.rglob('*')):
        if p.is_file():z.write(p,Path('docs')/p.relative_to(OUT))
    z.write(ROOT/'README.md','README.md')
print(dump(validation))
