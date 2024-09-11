import tkinter as tk
from tkinter import messagebox
from reactor_simulation import Reactor
from climate_adaptation import Climate
from safety_optimization import Safety
from database_manager import DatabaseManager

class ReactorSimulatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reactor Simulation")

        # Grid layout configuration
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_rowconfigure(7, weight=1)
        self.root.grid_rowconfigure(8, weight=1)
        self.root.grid_rowconfigure(9, weight=1)
        self.root.grid_rowconfigure(10, weight=1)

        # Reactor Power Output
        self.label_power = tk.Label(root, text="Reactor Power Output (MW):")
        self.label_power.grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.entry_power = tk.Entry(root)
        self.entry_power.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        # Coolant Temperature
        self.label_coolant_temp = tk.Label(root, text="Coolant Temperature (°C):")
        self.label_coolant_temp.grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.entry_coolant_temp = tk.Entry(root)
        self.entry_coolant_temp.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        # Pressure
        self.label_pressure = tk.Label(root, text="Pressure (Pa):")
        self.label_pressure.grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.entry_pressure = tk.Entry(root)
        self.entry_pressure.grid(row=2, column=1, padx=10, pady=5, sticky='w')

        # Climate Temperature
        self.label_climate_temp = tk.Label(root, text="Climate Temperature (°C):")
        self.label_climate_temp.grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.entry_climate_temp = tk.Entry(root)
        self.entry_climate_temp.grid(row=3, column=1, padx=10, pady=5, sticky='w')

        # Humidity
        self.label_humidity = tk.Label(root, text="Humidity (%):")
        self.label_humidity.grid(row=4, column=0, padx=10, pady=5, sticky='e')
        self.entry_humidity = tk.Entry(root)
        self.entry_humidity.grid(row=4, column=1, padx=10, pady=5, sticky='w')

        # Climate Pressure
        self.label_climate_pressure = tk.Label(root, text="Climate Pressure (Pa):")
        self.label_climate_pressure.grid(row=5, column=0, padx=10, pady=5, sticky='e')
        self.entry_climate_pressure = tk.Entry(root)
        self.entry_climate_pressure.grid(row=5, column=1, padx=10, pady=5, sticky='w')

        # Simulate Button
        self.simulate_button = tk.Button(root, text="Simulate", command=self.simulate)
        self.simulate_button.grid(row=6, column=0, columnspan=2, pady=10)

        # Output Labels for Simulation Results
        self.label_result_output = tk.Label(root, text="Adjusted Power Output (MW):")
        self.label_result_output.grid(row=7, column=0, padx=10, pady=5, sticky='e')
        self.label_result_output_value = tk.Label(root, text="")
        self.label_result_output_value.grid(row=7, column=1, padx=10, pady=5, sticky='w')

        self.label_result_temp = tk.Label(root, text="Adjusted Coolant Temp (°C):")
        self.label_result_temp.grid(row=8, column=0, padx=10, pady=5, sticky='e')
        self.label_result_temp_value = tk.Label(root, text="")
        self.label_result_temp_value.grid(row=8, column=1, padx=10, pady=5, sticky='w')

        self.label_result_pressure = tk.Label(root, text="Adjusted Pressure (Pa):")
        self.label_result_pressure.grid(row=9, column=0, padx=10, pady=5, sticky='e')
        self.label_result_pressure_value = tk.Label(root, text="")
        self.label_result_pressure_value.grid(row=9, column=1, padx=10, pady=5, sticky='w')

        self.label_result_risk = tk.Label(root, text="Optimized Risk Level:")
        self.label_result_risk.grid(row=10, column=0, padx=10, pady=5, sticky='e')
        self.label_result_risk_value = tk.Label(root, text="")
        self.label_result_risk_value.grid(row=10, column=1, padx=10, pady=5, sticky='w')

    def simulate(self):
        try:
            # Kullanıcıdan giriş verilerini al
            power_output = float(self.entry_power.get())
            coolant_temp = float(self.entry_coolant_temp.get())
            pressure = float(self.entry_pressure.get())

            climate_temp = float(self.entry_climate_temp.get())
            humidity = float(self.entry_humidity.get())
            climate_pressure = float(self.entry_climate_pressure.get())

            # Reaktör, iklim ve güvenlik simülasyonları
            reactor = Reactor(power_output=power_output, coolant_temp=coolant_temp, pressure=pressure)
            climate = Climate(temperature=climate_temp, humidity=humidity, pressure=climate_pressure)
            safety = Safety(risk_level=75, safety_measures=["Backup Cooling", "Pressure Release System"])

            climate_factor = climate.calculate_climate_factor()
            adjusted_output, adjusted_coolant_temp, adjusted_pressure = reactor.simulate_reactor_operation(climate_factor)
            optimized_risk = safety.optimize_safety()

            # Sonuçları GUI'ye yansıt
            self.label_result_output_value.config(text=str(adjusted_output))
            self.label_result_temp_value.config(text=str(adjusted_coolant_temp))
            self.label_result_pressure_value.config(text=str(adjusted_pressure))
            self.label_result_risk_value.config(text=str(optimized_risk))

            # Simülasyon sonuçlarını veritabanına kaydet
            db = DatabaseManager()
            db.save_simulation(adjusted_output, adjusted_coolant_temp, adjusted_pressure, climate_factor, optimized_risk)
            db.close()

        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numerical values.")

# Ana programı başlat
if __name__ == "__main__":
    root = tk.Tk()
    app = ReactorSimulatorApp(root)
    root.mainloop()
