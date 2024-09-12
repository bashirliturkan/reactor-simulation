import time
import unittest
from reactor_simulation1 import ReactorSimulator

class PerformanceTestReactorSimulator(unittest.TestCase):
    def setUp(self):
        self.simulator = ReactorSimulator()

    def test_performance(self):
        start_time = time.time()
        for _ in range(1000):  # 1000 simülasyon testi
            self.simulator.simulate(1000, 50, 200000, {'temperature': 25, 'humidity': 60, 'pressure': 101300})
        end_time = time.time()
        duration = end_time - start_time
        self.assertLess(duration, 5, "Simülasyon süresi 5 saniyeden uzun")

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
