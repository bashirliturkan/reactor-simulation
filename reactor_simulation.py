class Reactor:
    def __init__(self, power_output, coolant_temp, pressure):
        self.power_output = power_output  # MW cinsinden enerji üretimi
        self.coolant_temp = coolant_temp  # Soğutma sisteminin sıcaklığı
        self.pressure = pressure  # Basınç (Pa)

    def simulate_reactor_operation(self, climate_factor):
        # İklim faktörünü hesaba katarak reaktör performansını simüle et
        adjusted_output = self.power_output * (1 - climate_factor / 100)
        adjusted_coolant_temp = self.coolant_temp + (climate_factor * 0.5)
        adjusted_pressure = self.pressure * (1 + climate_factor / 500)

        # Ek olarak güvenlik limitlerini kontrol et
        if adjusted_coolant_temp > 350:
            print("Warning: Coolant temperature exceeds safety limits!")
        if adjusted_pressure > 120000:
            print("Warning: Pressure exceeds safety limits!")

        return adjusted_output, adjusted_coolant_temp, adjusted_pressure

    def display_status(self):
        print(f"Reactor Power Output: {self.power_output} MW")
        print(f"Coolant Temperature: {self.coolant_temp} °C")
        print(f"Pressure: {self.pressure} Pa")
