# To-Do-List
kullanıcı adı: user

şifre: admin

Görev ekleme, görev görüntüleme, görev tamamlama ve görev silme işlemleri mevcuttur. 
Görev eklerken görev ismi, içeriği QLineEdit şeklinde alınır. Görev başlangıç ve bitiş tarihini ise QDateTime sınıfından nesne oluşturarak alınır. Görev eklerken başlangıç tarihi bitiş tarihinden önce olursa program hata verir.

Görev görüntüleme kısmında QTableWidget vardır. Görev bilgilerini içerir. Görev tarihi şuanki tarihten sonra ise görev henüz başlamamıştır, aktif değildir. Görev aktifken görevi tamamlayabiliriz eğer bitiş tarihi şuanki tarihten sonra bir tarih olursa görevin tarihi geçer ve tamamlanamaz ve görev teslim süresi geçti şeklinde uyarı verir. Görev içeriği butonuna tıklarsak ayrıntılı bilgi ekranı karşımıza çıkar.

Görev tamamlama ve silme seçeneğinde seçtiğimiz göreve tıklayarak tamamlayabilir veya silebiliriz. Yalnızca aktif olan görevler tamamlanabilir. Silinen görevler görev görüntüleme kısmında görüntülenemez.
