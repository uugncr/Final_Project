import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Önceki eğitim sırasında kaydedilen model ve scaler'ı yükle
model_path = '/Users/uuu/Final_Project/iron_patrickv02.keras'
scaler_path = '/Users/uuu/Final_Project/scaler.save'
data_path = '/Users/uuu/Final_Project/test04.csv'

model = load_model(model_path)
scaler = joblib.load(scaler_path)

# Veri setini yükle
data = pd.read_csv(data_path)

# Girdi ve hedef sütunlarını ayarlama
X_test = data[['t0', 't1', 't2', 't3', 't4', 'N', 'd_r', 'd_f', 'total_integral', 'tail_integral', 'fom']]
y_test = data[['s_r', 's_f']].to_numpy()

# Test veri setini ölçeklendir
X_test_scaled = scaler.transform(X_test)

# Modeli test verileri üzerinde değerlendir
predictions_y = model.predict(X_test_scaled)

# MSE ve R^2 skorlarını hesaplayın
mse_sr = mean_squared_error(y_test[:, 0], predictions_y[:, 0])
r2_sr = r2_score(y_test[:, 0], predictions_y[:, 0])

mse_sf = mean_squared_error(y_test[:, 1], predictions_y[:, 1])
r2_sf = r2_score(y_test[:, 1], predictions_y[:, 1])

print(f"MSE (s_r): {mse_sr}")
print(f"R^2 (s_r): {r2_sr}")
print(f"MSE (s_f): {mse_sf}")
print(f"R^2 (s_f): {r2_sf}")

