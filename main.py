from reactor_simulation import Reactor
from climate_adaptation import Climate
from safety_optimization import Safety
from database_manager import DatabaseManager

def main():
    # Reaktör ve iklim koşulları
    reactor = Reactor(power_output=1000, coolant_temp=300, pressure=100000)
    climate = Climate(temperature=35, humidity=50, pressure=101325)
    safety = Safety(risk_level=75, safety_measures=["Backup Cooling", "Pressure Release System"])

    # İklim faktörünü hesapla
    climate_factor = climate.calculate_climate_factor()

    # Reaktör operasyonunu simüle et
    adjusted_output, adjusted_coolant_temp, adjusted_pressure = reactor.simulate_reactor_operation(climate_factor)

    # Güvenliği optimize et
    optimized_risk = safety.optimize_safety()

    # Veritabanına sonuçları kaydet
    db = DatabaseManager()
    db.save_simulation(adjusted_output, adjusted_coolant_temp, adjusted_pressure, climate_factor, optimized_risk)
    db.close()

    # Sonuçları görüntüle
    reactor.display_status()
    print(f"Adjusted Power Output: {adjusted_output} MW")
    print(f"Adjusted Coolant Temperature: {adjusted_coolant_temp} °C")
    print(f"Adjusted Pressure: {adjusted_pressure} Pa")
    print(f"Optimized Risk Level: {optimized_risk}")

if __name__ == "__main__":
    main()
