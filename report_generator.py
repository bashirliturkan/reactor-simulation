import matplotlib.pyplot as plt

class ReportGenerator:
    def __init__(self, power_outputs, coolant_temps, pressures):
        self.power_outputs = power_outputs
        self.coolant_temps = coolant_temps
        self.pressures = pressures

    def generate_report(self):
        # Güç çıktısı grafiği
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 3, 1)
        plt.plot(self.power_outputs, label="Power Output (MW)")
        plt.title("Power Output")
        plt.legend()

        # Soğutma sıcaklığı grafiği
        plt.subplot(1, 3, 2)
        plt.plot(self.coolant_temps, label="Coolant Temp (°C)")
        plt.title("Coolant Temperature")
        plt.legend()

        # Basınç grafiği
        plt.subplot(1, 3, 3)
        plt.plot(self.pressures, label="Pressure (Pa)")
        plt.title("Pressure")
        plt.legend()

        plt.tight_layout()
        plt.show()

# Kullanım
power_outputs = [380, 400, 420]
coolant_temps = [300, 310, 320]
pressures = [100000, 101000, 101500]
report = ReportGenerator(power_outputs, coolant_temps, pressures)
report.generate_report()
