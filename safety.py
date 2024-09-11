class Safety:
    def __init__(self, risk_level, safety_measures):
        self.risk_level = risk_level
        self.safety_measures = safety_measures

    def simulate_failure(self):
        # Olası bir arıza simülasyonu
        failure_occurred = False
        if self.risk_level > 70:  # Risk seviyesi yüksekse arıza ihtimali var
            failure_occurred = True
            print("Arıza gerçekleşti! Güvenlik sistemleri devrede.")

        return failure_occurred

    def apply_safety_measures(self):
        if self.simulate_failure():
            # Güvenlik sistemlerini devreye sok
            print(f"Güvenlik önlemleri devrede: {', '.join(self.safety_measures)}")

# Kullanım
safety = Safety(risk_level=85, safety_measures=["Backup Cooling", "Pressure Release System"])
safety.apply_safety_measures()
