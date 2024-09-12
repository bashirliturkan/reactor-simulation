class ReactorSimulator:
    def __init__(self, reactor_type='default'):
        self.reactor_type = reactor_type
        self.reactor_configurations = {
            'default': {'power_output': 1000.0, 'coolant_temp': 50.0},
            'fast_breeder': {'power_output': 1500.0, 'coolant_temp': 60.0},
            'thermal': {'power_output': 2000.0, 'coolant_temp': 70.0}
        }

    def simulate(self, power_output, coolant_temp, pressure, climate_data):
        config = self.reactor_configurations.get(self.reactor_type, self.reactor_configurations['default'])
        # Simülasyon kodu burada yer alacak
        return {
            'output': power_output * (coolant_temp / config['coolant_temp']),
            'status': 'success'
        }
