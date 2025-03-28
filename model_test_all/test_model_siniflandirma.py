#Test Loss: 0.00010376739373896271, Test Accuracy: 0.9999555349349976
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler  # Eğer ölçeklendirme yapılacaksa
from keras.utils import to_categorical  # Eğer çıktıyı kategorik formata dönüştürmeniz gerekiyorsa
from sklearn.metrics import accuracy_score

model_path = '/Users/uuu/Final_Project/sinniflandirma.keras'
# Veri setlerinin gerçek yolları
df1_path = '/Users/uuu/Final_Project/par25.csv'
df2_path = '/Users/uuu/Final_Project/par50.csv'
df3_path = '/Users/uuu/Final_Project/par100.csv'


# Veri setlerini yükleme ve birleştirme
df1 = pd.read_csv(df1_path)
df2 = pd.read_csv(df2_path)
df3 = pd.read_csv(df3_path)
df = pd.concat([df1, df2, df3])

# Modeli yükle
model = load_model(model_path)

selected_features = df.columns[:13]  # İlk 13 özelliği seçin

# Sadece seçilen özellikleri içeren bir DataFrame oluştur
X_new = df[selected_features]

# Eğer modeliniz ölçeklendirme gerektiriyorsa, burada ölçeklendirme işlemini yapın
# scaler = MinMaxScaler()
# X_new = scaler.fit_transform(X_new)

# Model üzerinde tahmin yap
predictions = model.predict(X_new)
predicted_classes = predictions.argmax(axis=1)

# Her bir sınıfın sayısını hesapla
electrons_count = (predicted_classes == 0).sum()
neutrons_count = (predicted_classes == 1).sum()
photons_count = (predicted_classes == 2).sum()

print(f'Elektron Sayısı: {electrons_count}')
print(f'Nötron Sayısı: {neutrons_count}')
print(f'Foton Sayısı: {photons_count}')

