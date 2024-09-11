import requests

class RealTimeClimateAdaptation:
    def __init__(self, api_url):
        self.api_url = api_url

    def fetch_data(self):
        try:
            response = requests.get(self.api_url)
            data = response.json()

            # API yanıtını kontrol et
            if data.get('cod') != 200:
                raise Exception(f"API Error: {data.get('message')}")

            # Yanıtın 'main' kısmını kontrol et
            if 'main' in data:
                temperature = data['main']['temp']  # Kelvin cinsindendir, Celsius’a çevirmek gerekebilir
                humidity = data['main']['humidity']
                pressure = data['main']['pressure']
                return temperature, humidity, pressure
            else:
                raise KeyError("API yanıtında 'main' verisi bulunamadı.")
        
        except Exception as e:
            print(f"Hata: {e}")
            return None, None, None

# OpenWeatherMap API'ye örnek istek URL'si (API anahtarınızı buraya ekleyin)
api_url = "https://www.meteosource.com/api/v1/free/point?place_id=london&sections=all&timezone=UTC&language=en&units=metric&key=YOUR-API-KEY"
climate_data = RealTimeClimateAdaptation(api_url)

# Verileri al ve yazdır
temp, humidity, pressure = climate_data.fetch_data()

if temp is not None:
    print(f"Temperature: {temp}°C, Humidity: {humidity}%, Pressure: {pressure} Pa")
else:
    print("Veri alınamadı.")
