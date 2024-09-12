from realtimeclimate_adaptation import ClimateData
from thermal_hydraulic_test import ThermalHydraulicTest
from neutronic_model import NeutronicModel
from autonomous_system_test import AutonomousSystemTest
from report_generator import ReportGenerator

def main():
    # Gerçek zamanlı iklim verilerini al
    climate_data = ClimateData("API_KEY")
    temp, humidity, pressure = climate_data.fetch_data()

    print(f"Temperature: {temp}, Humidity: {humidity}, Pressure: {pressure}")

    # Isıl-hidrolik testleri başlat
    th_test = ThermalHydraulicTest(temp, pressure)
    th_result = th_test.perform_test(50, 10000)
    print(f"Thermal-Hydraulic Test Result: {th_result}")

    # Nötronik modelleme
    neutron_model = NeutronicModel(neutron_flux=1e13, reactor_config="basic")
    neutronic_result = neutron_model.analyze_performance()
    print(f"Neutronic Test Result: {neutronic_result}")

    # Otonom sistem testi
    autonomous_test = AutonomousSystemTest(reactor="basic_reactor")
    auto_result = autonomous_test.simulate_autonomous_response({"temperature": temp, "pressure": pressure})
    print(f"Autonomous System Response: {auto_result}")

    # Rapor oluştur
    report = ReportGenerator()
    report.generate(temp, humidity, pressure, th_result)

if __name__ == "__main__":
    main()
