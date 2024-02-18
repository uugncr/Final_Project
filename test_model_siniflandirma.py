#Test Loss: 0.00010376739373896271, Test Accuracy: 0.9999555349349976
import pandas as pd
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler  # Eğer ölçeklendirme yapılacaksa
# from keras.utils import to_categorical  # Eğer çıktıyı kategorik formata dönüştürmeniz gerekiyorsa
from sklearn.metrics import accuracy_score

model_path = '/Users/uuu/Final_Project/sinniflandirma.keras'
new_data_path = '/Users/uuu/Final_Project/main_data/parameters100.csv'

# Modeli yükle
model = load_model(model_path)

# Yeni veri setini yükle
new_data = pd.read_csv(new_data_path)

# Model eğitimi sırasında kullanılan özellikleri seç
# Bu, modelinizin eğitimi sırasında kullanılan özelliklerin tam listesidir
selected_features = new_data.columns[:13]  # İlk 13 özelliği seçin, burada özellik sıralamasının önemli olduğunu varsayıyoruz

# Sadece seçilen özellikleri içeren bir DataFrame oluştur
X_new = new_data[selected_features]

# Model üzerinde tahmin yapma
predictions = model.predict(X_new)

# Tahmin sonuçlarını işle (örneğin, en yüksek olasılığa sahip sınıfı bulma)
predicted_classes = predictions.argmax(axis=1)

# Tahmin sonuçlarını görüntüle
print(predicted_classes)
