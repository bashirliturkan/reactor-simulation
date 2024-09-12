import unittest
from reactor_simulation1 import ReactorSimulator
from local_reactor_simulator import LocalReactorSimulator

class TestReactorSimulator(unittest.TestCase):
    def setUp(self):
        self.simulator = ReactorSimulator()
        self.local_simulator = LocalReactorSimulator()

    def test_reactor_simulation(self):
        power_output = 1200
        coolant_temp = 55
        pressure = 30
        climate_data = {'temperature': 22, 'humidity': 65}
        
        result = self.simulator.simulate(power_output, coolant_temp, pressure, climate_data)
        self.assertEqual(result['status'], 'success')

    def test_local_reactor_simulation(self):
        power_output = 1200
        coolant_temp = 55
        pressure = 30
        climate_data = {'temperature': 22, 'humidity': 65}
        self.local_simulator.local_configuration = {'power_adjustment': 1.1}
        
        result = self.local_simulator.simulate(power_output, coolant_temp, pressure, climate_data)
        self.assertEqual(result['status'], 'success')

if __name__ == '__main__':
    unittest.main()
