import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

# Veri setlerini yükleme ve birleştirme
df1 = pd.read_csv('/Users/uuu/Final_Project/parameters25.csv')
df2 = pd.read_csv('/Users/uuu/Final_Project/parameters50.csv')
df3 = pd.read_csv('/Users/uuu/Final_Project/parameters100.csv')
df = pd.concat([df1, df2, df3])
df_test = pd.read_csv('/Users/uuu/Final_Project/test.csv')
# Girdi ve hedef sütunlarını ayarlama
X = df[['t0', 't1', 't2', 't3', 't4', 'N', 'd_r', 'd_f', 'total_integral', 'tail_integral','fom']]
y = df[['s_r', 's_f']]

# Veri normalizasyonu için MinMaxScaler örneği
scaler = MinMaxScaler()

best_r2 = -np.inf  # R^2 için maksimum değeri bulmak istiyoruz, bu yüzden başlangıç değeri olarak -sonsuz kullanılır
best_mse = np.inf  # MSE için minimum değeri bulmak istiyoruz, bu yüzden başlangıç değeri olarak +sonsuz kullanılır
best_test_size_r2 = 0  # En iyi R^2 değerine sahip test_size
best_test_size_mse = 0  # En iyi MSE değerine sahip test_size

# Döngü içinde test_size ile denemeler
for test_size in np.arange(0.1, 1.0, 0.1):
    # Veri setini eğitim ve test seti olarak bölme
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6 ,random_state=80)
    
    # Verileri ölçeklendirme
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Yapay Sinir Ağı modelini oluşturma ve eğitme
    model = Sequential([
        Dense(128, input_dim=X_train_scaled.shape[1], activation='relu'),
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(16, activation='relu'),
        Dense(2, activation='linear')
    ])
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(X_train_scaled, y_train, epochs=100, batch_size=256, verbose=0)  # Eğitim sırasında çıktıyı gösterme
    
    # Modeli değerlendirme
    predictions = model.predict(X_test_scaled)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    print(f"Test Size: {test_size:.1f}, MSE: {mse:.4f}, R^2: {r2:.4f}")
    
    # En iyi MSE ve R^2 değerlerini güncelleme
    if mse < best_mse:
        best_mse = mse
        best_test_size_mse = test_size
    if r2 > best_r2:
        best_r2 = r2
        best_test_size_r2 = test_size

# En iyi sonuçları yazdırma
print("\nEn İyi Sonuçlar:")
print(f"En iyi R^2: {best_r2:.4f} (Test Size: {best_test_size_r2:.1f})")
print(f"En iyi MSE: {best_mse:.4f} (Test Size: {best_test_size_mse:.1f})")
# Modeli kaydetme (İsteğe bağlı)
model.save('patric_best.keras')


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
