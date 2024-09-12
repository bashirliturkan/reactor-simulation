class ThermalHydraulicTest:
    def __init__(self, initial_temp, initial_pressure):
        self.temp = initial_temp
        self.pressure = initial_pressure

    def perform_test(self, temp_increment, pressure_increment):
        new_temp = self.temp + temp_increment
        new_pressure = self.pressure + pressure_increment
        if new_temp > 500:  # Example threshold for overheating
            return "Overheating risk"
        if new_pressure > 200000:  # Example pressure threshold
            return "Pressure risk"
        return new_temp, new_pressure
