import unittest
from reactor_simulation1 import ReactorSimulator, Database

class TestReactorSimulator(unittest.TestCase):
    def setUp(self):
        # Testler için örnek veriler
        self.simulator = ReactorSimulator()
        self.db = Database()

    def test_reactor_simulation(self):
        # Örnek veri
        power_output = 1000.0
        coolant_temp = 50.0
        pressure = 200000.0
        climate_data = {'temperature': 25.0, 'humidity': 60.0, 'pressure': 101300.0}

        # Simülasyonu çalıştır
        result = self.simulator.simulate(power_output, coolant_temp, pressure, climate_data)

        # Beklenen sonuçları tanımla
        expected_output = 1000.0  # Örneğin, beklenen çıktılar
        self.assertEqual(result['output'], expected_output)
        self.assertTrue('error' not in result)  # Hata olup olmadığını kontrol et

    def test_database_save(self):
        # Veritabanına veri kaydetme testi
        test_data = {
            'power_output': 1000.0,
            'coolant_temp': 50.0,
            'pressure': 200000.0,
            'climate_data': {'temperature': 25.0, 'humidity': 60.0, 'pressure': 101300.0}
        }

        # Veriyi veritabanına kaydet
        self.db.save_simulation(**test_data)

        # Veritabanındaki verileri kontrol et
        saved_data = self.db.get_last_entry()
        self.assertIsNotNone(saved_data, "Veritabanından veri alınamadı.")
        self.assertEqual(saved_data.get('power_output'), test_data['power_output'])
        self.assertEqual(saved_data.get('coolant_temp'), test_data['coolant_temp'])
        self.assertEqual(saved_data.get('pressure'), test_data['pressure'])

    def tearDown(self):
        # Testler tamamlandıktan sonra kaynakları temizle
        self.db.close()

if __name__ == '__main__':
    unittest.main()
