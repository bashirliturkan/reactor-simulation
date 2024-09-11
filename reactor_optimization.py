class ReactorOptimizer:
    def __init__(self, power_output, coolant_temp, pressure):
        self.power_output = power_output
        self.coolant_temp = coolant_temp
        self.pressure = pressure

    def optimize(self):
        # Basit bir optimizasyon algoritması
        optimized_output = self.power_output * 0.9  # %10 azaltılmış güç
        optimized_coolant_temp = self.coolant_temp - 10  # Sıcaklık düşüşü
        optimized_pressure = self.pressure * 0.95  # Basınç düşüşü

        return optimized_output, optimized_coolant_temp, optimized_pressure

# Kullanım
optimizer = ReactorOptimizer(power_output=450, coolant_temp=320, pressure=101500)
opt_output, opt_temp, opt_pressure = optimizer.optimize()
print(f"Optimize edilmiş güç: {opt_output} MW, Sıcaklık: {opt_temp} °C, Basınç: {opt_pressure} Pa")
