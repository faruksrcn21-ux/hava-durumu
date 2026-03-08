# 🌤️Python Hava Durumu Uygulaması (Terminal Tabanlı)

Bu proje, OpenWeatherMap API'sini kullanarak istenilen şehrin anlık hava durumu verilerini terminal üzerinden hızlı ve güvenli bir şekilde sunan bir Python uygulamasıdır. 

## Öne Çıkan Özellikler
* **API Entegrasyonu:** OpenWeatherMap üzerinden anlık sıcaklık ve hava durumu açıklaması çeker.
* **Girdi Temizleme (Regex):** Kullanıcının hatalı tuşlamalarını (örneğin rakam veya noktalama işaretleri) arka planda temizleyerek API'ye doğru veriyi gönderir.
* **Güvenli Ortam Değişkenleri:** Hassas API anahtarı kodun içine yazılmamış, `python-dotenv` kütüphanesi kullanılarak `.env` dosyasında güvenli bir şekilde saklanmıştır.
* **Dayanıklı Hata Yönetimi:** İnternet bağlantısı sorunları, API zaman aşımı veya geçersiz şehir isimleri `Try-Except` blokları ile yakalanarak programın çökmesi engellenmiştir.

## Kullanılan Teknolojiler
* **Python 3.x**
* **Requests:** API ile HTTP haberleşmesi için.
* **Python-dotenv:** Çevre değişkenleri (Environment variables) yönetimi için.
* **Regex (re):** Girdi doğrulaması için.

## Kurulum ve Çalıştırma

 ### 1. Projeyi çalıştırabilmek için önce dosyaları bilgisayarınıza almanız gerekir:
* **Seçenek A (Önerilen):** Terminale şu komutu yazarak klonlayın:
 ```bash
git clone https://www.google.com/search?q=https://github.com/faruksrcn21/hava-durumu.git
cd hava-durumu
* **Seçenek B:** GitHub sayfasındaki yeşil **"Code"** butonuna tıklayıp **"Download ZIP"** diyerek indirin ve klasöre çıkartın.

### 2. Gerekli Kütüphaneleri Yükleyin
Terminali açın ve proje klasöründeyken aşağıdaki komutu çalıştırın (Bu komut `requests` ve `python-dotenv` kütüphanelerini otomatik yükler):
```bash
pip install -r requirements.txt

### 3. API Anahtarını Ayarlayın
Uygulamanın veri çekebilmesi için kişisel bir API anahtarına ihtiyacı vardır:
1. [OpenWeatherMap](https://openweathermap.org/api) adresine gidin ve ücretsiz üye olun.
2. "API Keys" sekmesinden ücretsiz anahtarınızı alın.
3. Proje ana dizininde `.env` dosyası oluşturup anahtarınızı ekleyin.
>
*Not: Güvenlik nedeniyle benim şahsi anahtarım `.gitignore` ile gizlenmiştir.*
