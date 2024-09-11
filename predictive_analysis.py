from sklearn.linear_model import LinearRegression
import numpy as np

class MLModel:
    def __init__(self):
        self.model = LinearRegression()

    def train_model(self, training_data, target_data):
        # Eğitim verisi iklim koşullarına dayalı olacak
        self.model.fit(training_data, target_data)

    def predict_performance(self, climate_data):
        # Modeli kullanarak performans tahmini yap
        return self.model.predict(np.array(climate_data).reshape(1, -1))

# Örnek veri ile kullanım
training_data = np.array([[25, 60, 101325], [30, 55, 101000], [20, 70, 100800]])  # Sıcaklık, nem, basınç
target_data = np.array([400, 450, 380])  # Güç çıktısı (MW)
ml_model = MLModel()
ml_model.train_model(training_data, target_data)

climate_data = [28, 65, 101200]
predicted_output = ml_model.predict_performance(climate_data)
print(f"Tahmin edilen güç çıktısı: {predicted_output[0]} MW")
