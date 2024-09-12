from reactor_simulation1 import ReactorSimulator

class LocalReactorSimulator(ReactorSimulator):
    def __init__(self, reactor_type='default', local_configuration=None):
        super().__init__(reactor_type)
        self.local_configuration = local_configuration if local_configuration else {}

    def simulate(self, power_output, coolant_temp, pressure, climate_data):
        config = self.reactor_configurations.get(self.reactor_type, self.reactor_configurations['default'])
        local_adjustment = self.local_configuration.get('power_adjustment', 1.0)
        return {
            'output': power_output * (coolant_temp / config['coolant_temp']) * local_adjustment,
            'status': 'success'
        }
