PLAYNOVA — PYTHON / PYGAME OYUN YAYINLAMA PLATFORMU
====================================================

MİMARİ
- Site: HTML + CSS + JavaScript (statik, sunucu gerektirmez)
- Oyun: Python + Pygame
- Tarayıcıya paketleme: Pygbag (Python/WebAssembly)
- Ücretsiz statik yayınlama: GitHub Pages
- Siteye oyun ekleme: oyunun paketlenmiş web çıktısını /games/oyun-adi/build/web/ içine koyup kart linki eklemek.

ÖNEMLİ
GitHub Pages Python dosyalarını sunucuda çalıştırmaz. Pygame oyunu önce Pygbag ile tarayıcı uyumlu web çıktısına dönüştürülmelidir.
Her Pygame oyunu sorunsuz dönüşmeyebilir; dosya erişimi, bazı kütüphaneler, ses ve senkron oyun döngüleri uyarlama isteyebilir.

1) BİLGİSAYARDA ÇALIŞTIRMA (Windows)
- Python'u python.org üzerinden kur.
- Proje klasöründe terminal aç.
- Kurulum:
    py -m pip install pygame-ce pygbag
- Oyunu masaüstünde test etmek istersen:
    py games/neon-dodge/main.py

2) TARAYICI İÇİN PAKETLEME
Pygbag, oyunun ana dosyasının main.py olmasını ve oyun döngüsünün async uyumlu olmasını bekler.
Proje kökünde terminal aç ve çalıştır:
    py -m pygbag --build games/neon-dodge

Çıktıyı kontrol et:
    games/neon-dodge/build/web/index.html

Bazı pygbag sürümlerinde CLI seçenekleri farklılık gösterebilir. Sorun olursa:
    py -m pygbag --help games/neon-dodge
Resmi rehber: https://pygame-web.github.io/wiki/pygbag/

3) WEB PAKETİNİ TEST ETME
Paketlemenin ardından proje kökünde çalıştır:
    py -m pygbag games/neon-dodge
ve tarayıcıda http://localhost:8000 adresini aç. Gerekirse oyun sayfasını seç.
Site içindeki oyun sayfası build/web/index.html dosyasını iframe içinde açar.

4) ÜCRETSİZ HOSTING (GitHub Pages)
- GitHub'da yeni bir PUBLIC repository oluştur.
- ZIP içeriğini çıkar ve tüm proje dosyalarını repoya yükle.
- Pygbag build çıktısı olan games/neon-dodge/build/web/ klasörünü de repoya ekle.
- Repository > Settings > Pages bölümünde yayın kaynağını seç (genellikle Deploy from a branch, main / root).
- Yayın adresin https://KULLANICI_ADIN.github.io/REPO_ADI/ biçiminde olur.
- GitHub Pages statik barındırmadır; Python backend çalıştırmaz.
Doküman: https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site

5) YENİ PYGAME OYUNU EKLEME
- games/yeni-oyun/ klasörü aç.
- Kaynak kodunu main.py adıyla koy; resim/ses dosyalarını da aynı oyun klasörüne yerleştir.
- Pygbag ile web çıktısını üret ve test et.
- index.html içindeki oyun kartını kopyalayıp düzenle.
- Kart linkini games/yeni-oyun/index.html olarak ayarla.
- Oyun sayfasındaki iframe src yolunu yeni oyunun build/web/index.html dosyasına göre düzenle.
- Tüm asset dosyalarını oyun klasörünün içinde tut. Web için PNG/JPG/WEBP ve OGG tercih et; büyük dosyaları optimize et.

İLK SÜRÜMDE NELER VAR?
- Responsive oyun portalı
- Oyun arama ve kategori filtreleri
- Örnek Pygame oyunu kaynak kodu
- Oyun sayfası ve iframe entegrasyonu
- Build ve ücretsiz yayınlama rehberi

İLK PAKETLEMEDEN ÖNCE:
Pygbag kurulumu ve web çıktısı oluşturulmadığı için bu ZIP içindeki oyun sayfası ilk açılışta build/web/index.html bulamayabilir. Önce yukarıdaki paketleme adımını çalıştır. Pygbag üretilen web dosyalarını ekledikten sonra site ve oyun birlikte yayınlanabilir.
