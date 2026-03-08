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

Projeyi bilgisayarınızda denemek için aşağıdaki adımları izleyebilirsiniz:

**1. Repoyu Klonlayın**
```bash
git clone [https://github.com/faruksrcn21/hava-durumu.git](https://github.com/faruksrcn21/hava-durumu.git)
cd hava-durumu
