class AutonomousSystemTest:
    def __init__(self, reactor):
        self.reactor = reactor

    def simulate_autonomous_response(self, external_conditions):
        if external_conditions["temperature"] > 500:
            return "Activating emergency cooling system"
        if external_conditions["pressure"] > 200000:
            return "Activating pressure release valve"
        return "All systems stable"
