class Climate:
    def __init__(self, temperature, humidity, pressure):
        self.temperature = temperature  # Dış ortam sıcaklığı
        self.humidity = humidity  # Nem oranı
        self.pressure = pressure  # Hava basıncı

    def calculate_climate_factor(self):
        # İklim koşullarına bağlı bir faktör hesapla (örnek bir basit formül)
        factor = (self.temperature * 0.3) + (self.humidity * 0.2) + (self.pressure * 0.1)
        return factor

    def display_climate_status(self):
        print(f"Temperature: {self.temperature} °C")
        print(f"Humidity: {self.humidity} %")
        print(f"Pressure: {self.pressure} Pa")
