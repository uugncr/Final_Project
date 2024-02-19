import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import mean_squared_error, r2_score
from keras.optimizers import RMSprop
from tensorflow.keras.optimizers import SGD
import joblib

df1 = pd.read_csv('/Users/uuu/Final_Project/par25.csv')
df2 = pd.read_csv('/Users/uuu/Final_Project/par50.csv')
df3 = pd.read_csv('/Users/uuu/Final_Project/par100.csv')
df = pd.concat([df1, df2, df3])


# Belirtilen sütunları girdi (X) ve hedef (y) olarak ayarlama
X = df[['t0', 't1', 't2', 't3', 't4', 'N', 'd_r', 'd_f', 'total_integral', 'tail_integral','fom']]
y = df[[ 's_r', 's_f']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)

# Veri normalizasyonu (MinMaxScaler kullanıyoruz çünkü genellikle ANN için iyi çalışır)
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = Sequential()
model.add(Dense(128, input_dim=X_train_scaled.shape[1], activation='relu'))  # Giriş katmanı
model.add(Dense(64, activation='relu'))  # Gizli katman
model.add(Dense(32, activation='relu'))  # Ek gizli katman
model.add(Dense(16, activation='relu'))

model.add(Dense(2, activation='linear'))  # Çıktı katmanı - 's_r' ve 's_f' için iki nöron

model.compile(loss='mean_squared_error', optimizer='adam')

# Modeli eğitme
model.fit(X_train_scaled, y_train, epochs=20, batch_size=1)

# Eğitim seti üzerinde modelin performansını ölçme
train_predictions = model.predict(X_train_scaled)
train_mse = mean_squared_error(y_train, train_predictions)
train_r2 = r2_score(y_train, train_predictions)

# Test seti üzerinde tahminler yapma
test_predictions = model.predict(X_test_scaled)
# Test seti için MSE ve R^2 hesaplama
test_mse = mean_squared_error(y_test, test_predictions)
test_r2 = r2_score(y_test, test_predictions)

# Performans metriklerini yazdırma
print(f"Eğitim Seti MSE: {train_mse}")
print(f"Eğitim Seti R^2: {train_r2}")
print(f"Test Seti MSE: {test_mse}")
print(f"Test Seti R^2: {test_r2}")
# Scaler'ı kaydet
scaler_filename = "scaler.save"
#joblib.dump(scaler, scaler_filename)
#model.save('patrick.keras')

"""
# df4 için giriş ve hedefi ayarlayın (Varsayım: df4, X ve y için aynı sütunlara sahiptir)
X_df4 = df4[['t0', 't1', 't2', 't3', 't4', 'N', 'd_r', 'd_f', 'total_integral', 'tail_integral','fom']]
y_df4 = df4[['s_r', 's_f']]

# df4 veri setini ölçeklendirin
X_df4_scaled = scaler.transform(X_df4)

# Modeli kullanarak df4 üzerinde tahminler yapın
predictions_df4 = model.predict(X_df4_scaled)

# Performans metriklerini hesaplayın
mse = mean_squared_error(y_df4, predictions_df4)
r2 = r2_score(y_df4, predictions_df4)

print(f"MSE: {mse}")
print(f"R^2: {r2}")
"""
