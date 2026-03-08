import requests
import os
import re
from dotenv import load_dotenv

load_dotenv()

def hava_durumu_sorgula(sehir):
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": sehir,
        "appid": api_key,
        "units": "metric",
        "lang": "tr"
    }

    try:
        cevap = requests.get(url, params=params, timeout=10)
        
        if cevap.status_code == 200:
            veri = cevap.json()
            sicaklik = veri["main"]["temp"]
            durum = veri["weather"][0]["description"]
            api_sehir_adi = veri["name"] 
            
            print(f"\n>>> {api_sehir_adi}: {sicaklik}°C - {durum.capitalize()}")
        
        elif cevap.status_code == 404:
            print(f"\n[!] '{sehir}' bulunamadı. Yazımı kontrol et.")
        else:
            print(f"\n[!] Hata: {cevap.status_code}")

    except Exception as e:
        print(f"\n[!] Bağlantı hatası: {e}")

if __name__ == "__main__":
    print("--- Hava Durumu Uygulaması ---")
    
    while True:
        ham_girdi = input("\nŞehir ismi girin (Çıkış için 'q'): ").strip()
        
        if ham_girdi.lower() == 'q':
            print("Uygulamadan çıkılıyor. Görüşmek üzere!")
            break
            
        temiz_girdi = re.sub(r'[^\w\s]', '', ham_girdi)
        
        if temiz_girdi:
            hava_durumu_sorgula(temiz_girdi)
        else:
            print("Lütfen bir şehir adı yazın.")