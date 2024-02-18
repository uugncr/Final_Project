"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Veri setlerini yükleme
df1 = pd.read_csv('/Users/uuu/Final_Project/par25.csv')
df2 = pd.read_csv('/Users/uuu/Final_Project/par50.csv')
df3 = pd.read_csv('/Users/uuu/Final_Project/par100.csv')
df = pd.concat([df1, df2, df3])

# Girdi (X) ve hedef (y) sütunlarını ayarlama
X = df[['t0', 't1', 't2', 't3', 't4', 'N', 'd_r', 'd_f', 'total_integral', 'tail_integral','fom']]
y = df[['s_r', 's_f']]

# Modeli tanımlama
def create_model(input_dim):
    model = Sequential()
    model.add(Dense(128, input_dim=input_dim, activation='relu'))  # Giriş katmanı
    model.add(Dense(64, activation='relu'))  # Gizli katman
    model.add(Dense(32, activation='relu'))  # Ek gizli katman
    model.add(Dense(16, activation='relu'))
    model.add(Dense(2, activation='linear'))  # Çıktı katmanı
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# Ölçeklendirici tanımlama
scaler = MinMaxScaler()

for random_state in range(0, 101, 10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=random_state)
    
    # Veriyi ölçeklendirme
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Modeli oluşturma ve eğitme
    model = create_model(X_train_scaled.shape[1])
    model.fit(X_train_scaled, y_train, epochs=100, batch_size=256, verbose=0)  # epochs 1000'den 100'e düşürüldü hızlı sonuç için
    
    # Eğitim ve test setleri için tahminler
    train_predictions = model.predict(X_train_scaled)
    test_predictions = model.predict(X_test_scaled)
    
    # Performans metrikleri
    train_mse = mean_squared_error(y_train, train_predictions)
    train_r2 = r2_score(y_train, train_predictions)
    test_mse = mean_squared_error(y_test, test_predictions)
    test_r2 = r2_score(y_test, test_predictions)
    
    print(f"Random State: {random_state}")
    print(f"Eğitim Seti MSE: {train_mse}, Eğitim Seti R^2: {train_r2}")
    print(f"Test Seti MSE: {test_mse}, Test Seti R^2: {test_r2}")
    print('-' * 50)
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Veri setlerini yükleme
df1 = pd.read_csv('/Users/uuu/Final_Project/par25.csv')
df2 = pd.read_csv('/Users/uuu/Final_Project/par50.csv')
df3 = pd.read_csv('/Users/uuu/Final_Project/par100.csv')
df = pd.concat([df1, df2, df3])

# Girdi (X) ve hedef (y) sütunlarını ayarlama
X = df[['t0', 't1', 't2', 't3', 't4', 'N', 'd_r', 'd_f', 'total_integral', 'tail_integral','fom']]
y = df[['s_r', 's_f']]

# Sabit random_state değeri
random_state = 80

# Modeli tanımlama
def create_model(input_dim):
    model = Sequential()
    model.add(Dense(128, input_dim=input_dim, activation='relu'))  # Giriş katmanı
    model.add(Dense(64, activation='relu'))  # Gizli katman
    model.add(Dense(32, activation='relu'))  # Ek gizli katman
    model.add(Dense(16, activation='relu'))
    model.add(Dense(2, activation='linear'))  # Çıktı katmanı
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# Ölçeklendirici tanımlama
scaler = MinMaxScaler()

# test_size için döngü
for test_size in [x * 0.1 for x in range(1, 10)]:  # 0.1'den 0.9'a kadar
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    # Veriyi ölçeklendirme
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Modeli oluşturma ve eğitme
    model = create_model(X_train_scaled.shape[1])
    model.fit(X_train_scaled, y_train, epochs=100, batch_size=256, verbose=0)  # epochs 1000'den 100'e düşürüldü hızlı sonuç için
    
    # Eğitim ve test setleri için tahminler
    train_predictions = model.predict(X_train_scaled)
    test_predictions = model.predict(X_test_scaled)
    
    # Performans metrikleri
    train_mse = mean_squared_error(y_train, train_predictions)
    train_r2 = r2_score(y_train, train_predictions)
    test_mse = mean_squared_error(y_test, test_predictions)
    test_r2 = r2_score(y_test, test_predictions)
    
    print(f"Test Size: {test_size}")
    print(f"Eğitim Seti MSE: {train_mse}, Eğitim Seti R^2: {train_r2}")
    print(f"Test Seti MSE: {test_mse}, Test Seti R^2: {test_r2}")
    print('-' * 50)
