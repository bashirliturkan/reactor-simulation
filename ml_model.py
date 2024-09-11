from sklearn.linear_model import LinearRegression
import numpy as np

class MLModel:
    def __init__(self):
        self.model = LinearRegression()

    def train_model(self, training_data, target_data):
        self.model.fit(training_data, target_data)

    def predict_performance(self, climate_data):
        return self.model.predict(np.array(climate_data).reshape(1, -1))

# Örnek kullanım
if __name__ == "__main__":
    model = MLModel()
    X_train = np.array([[1, 2], [2, 3], [3, 4]])
    y_train = np.array([1, 2, 3])
    model.train_model(X_train, y_train)
    
    climate_data = [4, 5]
    prediction = model.predict_performance(climate_data)
    print("Prediction:", prediction)
