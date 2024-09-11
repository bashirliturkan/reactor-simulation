class Safety:
    def __init__(self, risk_level, safety_measures):
        self.risk_level = risk_level  # Risk seviyesi (0-100)
        self.safety_measures = safety_measures  # Alınan güvenlik önlemleri

    def optimize_safety(self):
        # Güvenlik önlemlerine göre riski azalt
        optimized_risk = self.risk_level - (len(self.safety_measures) * 5)
        optimized_risk = max(0, optimized_risk)  # Risk 0'ın altına düşemez
        return optimized_risk

    def display_safety_status(self):
        print(f"Risk Level: {self.risk_level}")
        print(f"Safety Measures: {self.safety_measures}")
