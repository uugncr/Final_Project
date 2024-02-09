import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import mean_squared_error, r2_score
from keras.optimizers import RMSprop
from tensorflow.keras.optimizers import SGD

# Ayrı ayrı veri setlerini yükleme
df1 = pd.read_csv('/Users/uuu/Final_Project/parameters25.csv')
df2 = pd.read_csv('/Users/uuu/Final_Project/parameters50.csv')
df3 = pd.read_csv('/Users/uuu/Final_Project/parameters100.csv')
df4 = pd.read_csv('/Users/uuu/Final_Project/test.csv')
# Veri setlerini birleştirme
df = pd.concat([df1, df2, df3])

# Belirtilen sütunları girdi (X) ve hedef (y) olarak ayarlama
X = df[['t0', 't1', 't2', 't3', 't4', 'N', 'd_r', 'd_f', 'total_integral', 'tail_integral','fom']]
y = df[[ 's_r', 's_f']]

# Veri setini eğitim ve test seti olarak bölme
#
# Test_size~Train R^2 :: 0.1/0.4/0.6 (en iyi/en iyi/is yapar)
# Test_size~Test R^2 :: 0.6 (en iyi)
# Random_state R^2 :: 10/80 (en iyi/is yapar)
# Random_state R^2 :: 20/80 (en iyi/is yapar)
# Bu degerlendirmeler sonnucununda kodun bu kismi tamamlandi
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.6, random_state=80)

# Veri normalizasyonu (MinMaxScaler kullanıyoruz çünkü genellikle ANN için iyi çalışır)
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Yapay Sinir Ağı modelini oluşturma
#                  AKTIVASYON FOKSIYOLARI
# ReLU icin degerler;
#   run_1 = mse :: 1.692, R^2 :: 0.7150
#   run_2 = mse :: 1.801, R^2 :: 0.707
#   run_3 = mse :: 1.132, R^2 :: 0.8168
# Sigmoid icin degerler;
#   run_1 = mse :: 78.487, R^2 :: 0.343
#   run_2 = mse :: 56.995, R^2 :: 0.3629
#   run_3 = mse :: 84.346, R^2 :: 0.3084
# Tanh icin degerler;
#   run_1 = mse :: 15.35, R^2 :: 0.581
#   run_2 = mse :: 100.61, R^2 :: 0.426
#   run_3 = mse :: 52.16, R^2 :: 0.100
# Bu degerlendirmeler sonucu aktivasyon fonksiyonu ReLU secildi, Cikis katmani asla degistirilmedi.
# Giris katmani::2048, Gizli katman::1024, Gizli katman::512, Gizli katman::256, Gizli katman::64,
# Gizli katman::16, # Çıktı katmanı::2 denendi test_mse::1.0670, test_R^2::0.6693 cikti
model = Sequential()
model.add(Dense(128, input_dim=X_train_scaled.shape[1], activation='relu'))  # Giriş katmanı
model.add(Dense(64, activation='relu'))  # Gizli katman
model.add(Dense(32, activation='relu'))  # Ek gizli katman
model.add(Dense(16, activation='relu'))

model.add(Dense(2, activation='linear'))  # Çıktı katmanı - 's_r' ve 's_f' için iki nöron
###############################################################
#                   OPTIMIZASYON
# ADAM icin degerler;
#   epochs = 100 ;
#       train - mse :: 0.1029,
#               R^2 :: 0.8858,
#       test - mse :: 1.7370,
#               R^2 :: 0.7978,
#   epochs = 1000 ;
#       train - mse :: 0.0184,
#               R^2 :: 0.9411,
#       test - mse :: 1.1434,
#               R^2 :: 0.8414,
#   epochs = 2000 ;
#       train - mse :: 0.0121,
#               R^2 :: 0.9707,
#       test - mse :: 0.5863,
#               R^2 :: 0.8468,
#   epochs = 3000 ;
#       train - mse :: 0.00863,
#               R^2 :: 0.97175
#       test - mse :: 0.78838,
#               R^2 :: 0.25123
# SGD degerleri null cikti, ADAM degerleri iyi cikinca yapmadim.
# RMSprop icin degerler;
#   epochs = 100 ;
#       train - mse :: 0.08835,
#               R^2 :: 0.6626
#       test - mse :: 9.101,
#               R^2 :: -0.4056
#   epochs = 1000 ;
#       train - mse :: 0.3854,
#               R^2 :: 0.7996
#       test - mse :: 10.6209,
#               R^2 :: 0.4226
#   epochs = 2000 ;
#       train - mse :: 0.0495,
#               R^2 :: 0.9115
#       test - mse :: 3.4475,
#               R^2 :: 0.3994
#   epochs = 3000 ;
#       train - mse :: 0.0740,
#               R^2 :: 0.8991
#       test - mse :: 10.4462,
#               R^2 :: -0.5379

# Modeli derleme ----------------------1
model.compile(loss='mean_squared_error', optimizer='adam')
# SGD optimizasyon algoritması ile modeli derleme -------------2
#sgd_optimizer = SGD()
#model.compile(loss='mean_squared_error', optimizer=sgd_optimizer)

# RMSprop optimizasyon algoritması ile modeli derleme -------3
#rmsprop_optimizer = RMSprop()
#model.compile(loss='mean_squared_error', optimizer=rmsprop_optimizer)

###############################################################
# Modeli eğitme
model.fit(X_train_scaled, y_train, epochs=3000, batch_size=256)
# Eğitim seti üzerinde modelin performansını ölçme
train_predictions = model.predict(X_train_scaled)
train_mse = mean_squared_error(y_train, train_predictions)
train_r2 = r2_score(y_train, train_predictions)
# Performans metriklerini yazdırma
print(f"Eğitim Seti MSE: {train_mse}")
print(f"Eğitim Seti R^2: {train_r2}")

###############################################################
# Modeli kaydetme (İsteğe bağlı)----------------1
model.save('patric_adam.keras')
# Modeli kaydetme (İsteğe bağlı)----------------2
#model.save('patric_sgd.keras')
# Modeli kaydetme (İsteğe bağlı)----------------3
#model.save('patric_rmspropv2.keras')
###############################################################

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

