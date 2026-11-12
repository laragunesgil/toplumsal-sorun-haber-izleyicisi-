# YZ ile çalışma günlüğü

Bu günlükte başlangıç mesajı sayılmadan, bu proje için gerçekten gönderilmiş yedi takip promptu yer alır. Kararlar, kullanıcının seçtiği seçeneklere dayanır. Kod ve test sonuçları gerçek Python çalıştırmalarından alınmıştır.

## Prompt 1 — Uygulama tasarımı

### Gönderilen prompt

~~~text
GEP1316 ödevim için Sosyoloji bölümüne uygun bir Python komut satırı uygulaması tasarlıyorum: Toplumsal Sorun Haber İzleyicisi. Program, kamuya açık haber başlıklarını toplumsal sorun kategorilerine göre kaydedecek ve özet rapor oluşturacak.

Henüz kod yazma. Başlangıç seviyesinde biri için programın hangi bilgileri alacağını ve raporda neleri göstereceğini öner. Kişisel veri kaydetmeden çalışsın ve haberleri internetten otomatik toplamasın. Tasarımın sonunda iki basit analiz seçeneği sun: A) yalnızca kategori sayılarını gösterme, B) kategori sayılarını kaynaklara göre de gösterme. Her seçeneğin ne işe yaradığını ve hangisinin bu ödev için daha kolay olacağını kısaca açıkla. Sonunda seçim yapmam için A/B diye sor.
~~~

### YZ yanıtı ve karar

YZ; haber başlığı, kaynak, yayın tarihi ve hazır kategoriler alınmasını; CSV’ye kayıt ve kategori özeti üretilmesini önerdi. A seçeneği yalnızca kategori sayılarını, B seçeneği kaynaklara göre de sayımları göstermeyi içeriyordu. Kullanıcı A’yı seçti.

### Onaylanan gerekçe

“Kategori sayılarını seçtim çünkü uygulaması ve anlaşılması daha kolay. Bu özet, hangi toplumsal sorunların haberlerde daha sık yer aldığını görmeme yardımcı olur. Ayrıca temel gereksinimleri karşılarken girdi kontrolü ve dosyaya kayıt gibi konulara odaklanmamı sağlar.”

### Uygulanan karar

Rapor kategori sayılarını gösterir; kaynaklara göre karşılaştırma yapmaz. Uygulama kamuya açık başlıkları elle alır ve internetten veri çekmez.

## Prompt 2 — Girdi doğrulama ve planlanan testler

### Gönderilen prompt

~~~text
GEP1316 projemiz için tasarımımız şu: Toplumsal Sorun Haber İzleyicisi; kullanıcıdan haber başlığı, kaynak adı, yayın tarihi ve hazır listeden toplumsal sorun kategorisi alacak. Kayıtları CSV dosyasına ekleyecek ve raporda yalnızca her kategorideki haber sayısını gösterecek. Kişisel veri toplamayacak ve internetten otomatik haber çekmeyecek.

Henüz kod yazma. Bu dört bilgi için başlangıç seviyesinde anlaşılır doğrulama kuralları öner. Başlığın veya kaynak adının boş bırakılması, geçersiz tarih (örneğin 2026-02-30) ve listede olmayan kategori gibi hatalarda programın çökmeden ne yapması gerektiğini açıkla. En az iki hatalı veya uç durum içeren beş planlı test senaryosu yaz; her biri için girdi ve beklenen sonucu belirt. Sonunda yayın tarihi için iki seçenek sun: A) Geçerli takvim tarihine ek olarak gelecekteki tarihleri reddetmek, B) Her geçerli takvim tarihine izin vermek. Hangisinin bu proje için daha uygun olduğunu kısaca öner ve A/B seçmemi iste.
~~~

### YZ yanıtı ve karar

YZ boş başlık ve kaynak, takvimde olmayan tarih ve geçersiz kategori için uyarı ve yeniden giriş kuralı önerdi. Beş planlanan senaryo sundu. Kullanıcı B’yi seçti: geçerli takvim tarihleri kabul edilecek, gelecek tarihleri ayrıca bugünün tarihiyle karşılaştırılmayacak.

### Onaylanan gerekçe

“B seçeneğini tercih ettim çünkü tarih kontrolünü basit tutuyor. Program geçersiz takvim tarihlerini reddedecek, ancak girilen tarihi bugünün tarihiyle karşılaştırmayacak. Böylece tarih doğrulama kuralını anlamak ve uygulamak daha kolay olacak.”

### Uygulanan karar

Kod tarihi `YYYY-AA-GG` biçiminde ve gerçek bir takvim tarihi olarak doğrular; `2099-12-31` gibi geçerli gelecek tarihlerini kabul eder.

## Prompt 3 — Boş kategorilerin raporda gösterilmesi

### Gönderilen prompt

~~~text
Toplumsal Sorun Haber İzleyicisi raporunda yalnızca kategori sayılarını göstereceğiz. Kategorilerimiz Barınma, Göç, Gençlik, Eğitim ve Çalışma hayatı olacak.

Henüz kod yazma. İki rapor biçimini karşılaştır: A) Kayıt bulunan kategorilerin hepsini göster; haber olmayan kategorilerin yanında da 0 yaz. B) Yalnızca en az bir haberi olan kategorileri göster. Hiç haber kaydı yoksa her iki seçenekte de kullanıcıya anlaşılır bir mesaj gösterilmesini öner. Bu proje için hangisinin daha kullanışlı olduğunu kısaca açıkla ve A/B seçmemi iste.
~~~

### YZ yanıtı ve karar

YZ, A’nın tüm kategorileri görünür tuttuğunu; B’nin ise daha kısa rapor ürettiğini açıkladı. Hiç kayıt yoksa açık bir bilgi mesajı önerdi. Kullanıcı A’yı seçti.

### Onaylanan gerekçe

“Tüm kategorileri, sayı sıfır olsa bile göstermeyi seçtim. Böylece hangi toplumsal sorunların haber kayıtlarında yer aldığını ve hangilerinin hiç kaydedilmediğini tek raporda görebilirim.”

### Uygulanan karar

Rapor beş kategorinin tümünü gösterir; kayıt olmayanların yanında 0 yazar. CSV boşsa “Henüz haber kaydı yok.” mesajı gösterilir.

## Prompt 4 — Yinelenen kayıtlar

### Gönderilen prompt

~~~text
Toplumsal Sorun Haber İzleyicisi haber başlığı, kaynak, yayın tarihi ve kategori bilgilerini CSV dosyasına kaydedecek. Henüz kod yazma.

Aynı başlık, kaynak, tarih ve kategoriyle bir kayıt daha eklenmek istenirse iki seçeneği karşılaştır: A) Program bunun aynı kayıt olduğunu fark edip uyarı versin ve ikinci kez kaydetmesin. B) Program her girdiyi kaydetsin; tekrarları kullanıcı takip etsin. Her seçeneğin kategori sayılarını etkisini açıkla. Bu başlangıç seviyesi proje için hangisini önerdiğini söyle ve A/B seçmemi iste.
~~~

### YZ yanıtı ve karar

YZ, tekrarları kabul etmenin kategori sayımlarını şişirebileceğini; tekrar kontrolünün CSV’yi okuyup mevcut kayıtlarla karşılaştırmayı gerektirdiğini açıkladı. Kullanıcı A’yı seçti.

### Onaylanan gerekçe

“A seçeneğini tercih ettim çünkü aynı haberin iki kez kaydedilmesi kategori sayılarını olduğundan fazla gösterebilir. Tekrarlanan kaydı engellemek, raporun daha güvenilir olmasına yardımcı olur.”

### Uygulanan karar

Uygulama başlık, kaynak, tarih ve kategori karşılaştırması yapar; aynı kayıt tekrar eklenmek istenirse uyarı verir ve CSV’ye ikinci satırı yazmaz.

## Prompt 5 — Uygulama kodu ve gerçek testler

### Gönderilen prompt

~~~text
Artık Toplumsal Sorun Haber İzleyicisi için uygulama.py dosyasını yaz. Şu kararlarımızı uygula:

- Python standart kütüphanesini kullan; class kullanma; kodu başlangıç seviyesine uygun Türkçe yorumlarla açıkla.
- Menüde haber ekleme, kategori raporu görme ve çıkış seçenekleri olsun. Menü çıkış seçilene kadar döngüde kalsın.
- Haber başlığı, kaynak adı, yayın tarihi ve kategori al. Başlık ve kaynak boş olamasın; tarih YYYY-AA-GG biçiminde geçerli bir takvim tarihi olmalı. Gelecek tarihlere de izin ver. Kategori yalnızca Barınma, Göç, Gençlik, Eğitim veya Çalışma hayatı olabilir. Hatalı girdilerde uyarıp yeniden sor; program çökmesin.
- CSV dosyası yoksa başlık satırıyla oluştur; sonraki kayıtları ekle. Dört alanı da aynı olan bir kayıt varsa uyar ve ikinci kez kaydetme.
- Rapor beş kategorinin hepsini, kayıt olmayanların sayısı 0 olacak şekilde göstersin. Hiç kayıt yoksa “Henüz haber kaydı yok.” mesajı versin.
- En az üç fonksiyon, iki karar yapısı, döngü ve liste veya sözlük kullan.

Kodu gerçekten Python’da çalıştır. En az yedi test senaryosunu dene: normal kayıt, boş başlık, boş kaynak, imkânsız tarih, geçersiz kategori, aynı kaydı tekrar ekleme ve geçerli bir gelecek tarihi. Beklenen ve gerçek sonuçları ayrı ayrı yaz; testi yapmadıysan yapılmış gibi gösterme. Bulduğun gerçek bir sorun olursa düzeltip yeniden çalıştır. Sonuçta uygulama.py dosyasını oluştur ve kodun ne yaptığını basitçe açıkla.
~~~

### YZ yanıtı, karar ve uygulama

YZ `uygulama.py` dosyasını oluşturdu. Kod dokuz fonksiyon, bir liste, sözlükler, girdi doğrulamaları, CSV okuma/yazma ve menü döngüsü içerir. İlk test sürümünde tam metin karşılaştırması büyük/küçük harf farkıyla yinelenen haberi yakalamıyordu. YZ bunu gerçek bir sınırlılık olarak belirtti. Kullanıcı, başlık ve kaynak karşılaştırmasında harf büyüklüğünün yok sayılmasını seçti.

### Onaylanan gerekçe

“Harf büyüklüğü farkıyla girilen aynı haberin kategori sayısını yanlışlıkla artırmasını önlemek için tekrar kontrolünü bu farkı yok sayacak şekilde yapmayı seçtim. Böylece rapordaki sayılar daha güvenilir olur.”

### Değişiklik ve test sonucu

Türkçe `I/İ` harflerini de ele alan karşılaştırma eklendi; CSV’de ilk kaydın görünümü korunur. Güncel kodda 13 odaklı kontrol ve menü üzerinden 1 uçtan uca çalıştırma geçti. Kontroller; normal kayıt, boş alanlar, geçersiz tarih ve kategori, gelecek tarih, tekrar kaydı, boş rapor ve menü döngüsünü kapsar.

## Prompt 6 — Gereksinim kontrolü ve kodu anlama

### Gönderilen prompt

~~~text
Mevcut uygulama.py dosyamı GEP1316 ödev yönergesindeki program gereksinimleriyle karşılaştır. Henüz kodu değiştirme. Her gereksinimin karşılanıp karşılanmadığını mevcut koddan örnek vererek açıkla; eksik veya riskli bir nokta varsa gerçek koda dayanarak belirt, hata uydurma.

Ayrıca kodu başlangıç seviyesinde açıkla: fonksiyonlar ne yapıyor, if/elif kararları nerede, döngü ne işe yarıyor, liste veya sözlük nerede kullanılıyor ve CSV dosyasına kayıt nasıl yapılıyor? Sonunda kodu anlayıp anlamadığımı kontrol etmek için üç kısa soru ve doğru cevaplarını ver; bunları benim cevaplarım gibi gösterme. En sonda, varsa bir iyileştirme için iki seçenek ve kısa önerini sun.
~~~

### YZ yanıtı ve karar

YZ, kodun işlevsel gereksinim 1–6’yı karşıladığını, testlerin çalıştırıldığını ancak README, PROMPTLAR günlüğü ve GitHub yüklemesinin hâlâ gerektiğini belirtti. Fonksiyonları, karar yapılarını, döngüyü, liste/sözlük kullanımını ve CSV akışını açıkladı; üç kontrol sorusu ile cevaplarını verdi. Kod incelemesinde iç boşlukların yinelenen haber karşılaştırmasında birleştirilmediğini saptadı. Kullanıcı B’yi seçti ve bu kuralı eklememeyi tercih etti.

### Onaylanan gerekçe

“Mevcut tekrar kontrolünü korumayı seçtim çünkü başlık ve kaynak bilgisindeki harf büyüklüğü farklarını zaten dikkate alıyor. İç boşlukları da düzenlemek ek bir kural gerektireceğinden, başlangıç seviyesi proje için kodu daha basit tutmak istedim.”

### Uygulanan karar

Kodda değişiklik yapılmadı. README’de iç boşluk farkının ayrıca normalize edilmediği açıklandı.

## Prompt 7 — README ve örnek terminal çıktısı

### Gönderilen prompt

~~~text
Mevcut ve gerçekten test edilmiş uygulama.py dosyasına dayanarak proje klasöründe README.md oluştur. README Türkçe, anlaşılır ve başlangıç seviyesine uygun olsun. Şunları içersin:

- Uygulamanın amacı ve kimler için yararlı olduğu
- Alınan bilgiler, kategoriler, menü seçenekleri ve CSV kayıt biçimi
- Python 3 ile nasıl çalıştırılacağı
- Gerçek testlerden beklenen ve gerçekleşen sonuçları gösteren en az 7 satırlık test tablosu
- Uygulamanın gerçek çalıştırma çıktısını örnek olarak gösteren bir bölüm
- Tamamı büyük/küçük harf farkı dışında aynı olan kayıtların engellendiği; iç boşluk farkının ise henüz normalize edilmediği bilgisi

Örnek terminal çıktısını gerçekten uygulamayı çalıştırarak al ve bu çıktıyı gösteren okunaklı bir PNG oluştur. PNG’nin gerçek bilgisayar ekran görüntüsü değil, gerçek program çıktısından hazırlanmış bir örnek olduğunu açıkça belirt. README’ye PNG’yi ekle. Gerçek test sonuçları dışında sonuç uydurma ve GitHub’a yükleme yapılmış gibi yazma.
~~~

### YZ yanıtı ve karar

YZ, gerçek menü çalıştırmasından alınan terminal çıktısını kullanarak `ornek_cikti.png` hazırladı ve test tablosu içeren README oluşturdu. Görselde bunun ekran görüntüsü değil, gerçek program çıktısından hazırlanmış örnek olduğu belirtildi. Kullanıcı A seçeneğiyle README’ye kurgusal bir CSV başlığı ve veri satırı örneği eklenmesini istedi. Örnek satır dosya biçimini somutlaştırmak için eklendi. Kullanıcının daha hızlı ilerleme isteği üzerine kalan dosya çalışması bir araya getirildi.

## Eleştirel kontrol ve gerçek test aksaklığı

İlk uçtan uca test kontrolünde rapor satırındaki boşluk sayısı yanlış beklenmişti. Gerçek terminal çıktısı incelendi; uygulama sayımı doğru vermişti. Kontrol, sabit boşluk sayısı aramak yerine satırdaki kelimeleri karşılaştıracak şekilde düzeltildi ve uçtan uca akış yeniden geçti. Daha sonraki bir testte Python’ın genel `upper()` yöntemi Türkçe büyük `İ` yerine `I` ürettiği için test verisi hatalı kurulmuştu. Türkçe kurala uygun büyük harfli test girdisi hazırlanıp tekrar çalıştırıldığında 13/13 odaklı kontrol geçti. Bu iki durum uygulama hatası değildi; YZ’nin test beklentisi/test girdisi oluştururken yaptığı yanlışlar gerçek çıktı ve normalize edilmiş metinler incelenerek yakalandı.

## Test kanıtı

- Odaklı Python kontrolleri: 13/13 geçti.
- Menü üzerinden uçtan uca çalışma: 1/1 geçti; kayıt eklendi, kategori raporu gösterildi ve program çıkış yaptı.
- Örnek çıktı PNG’si gerçek menü çalıştırmasından oluşturuldu.

## GitHub yükleme durumu

`uygulama.py` ve `README.md` GitHub deposuna eklendi. `PROMPTLAR.md` şu anda ekleniyor. README’de bağlantısı bulunan `akis_semasi.png` ve `ornek_cikti.png` dosyalarının da depoya yüklenmesi gerekiyor.
