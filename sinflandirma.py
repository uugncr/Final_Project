import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

# Veri setlerini yükleme ve birleştirme
df1 = pd.read_csv('/Users/uuu/Final_Project/par25.csv')
df2 = pd.read_csv('/Users/uuu/Final_Project/par50.csv')
df3 = pd.read_csv('/Users/uuu/Final_Project/par100.csv')

# Etiketlerin eklenmesi
df1['label'] = 0  # Elektron
df2['label'] = 1  # Nötron
df3['label'] = 2  # Foton

# Veri setlerinin birleştirilmesi
df = pd.concat([df1, df2, df3])

# Girdi (X) ve çıktı (Y) değişkenlerinin ayrılması
X = df.drop('label', axis=1)
Y = df['label']

# Çıktıyı kategorik formata dönüştürme
Y = to_categorical(Y)

# Eğitim ve test setlerine ayrılması
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=40)

# Modelin oluşturulması
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))  # Giriş katmanı ve 1. gizli katman
model.add(Dense(32, activation='relu'))  # 2. gizli katman
model.add(Dense(Y.shape[1], activation='softmax'))  # Çıkış katmanı

# Modelin derlenmesi
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Modelin eğitilmesi
model.fit(X_train, Y_train, epochs=100, batch_size=100, validation_split=0.2)

# Modelin değerlendirilmesi
loss, accuracy = model.evaluate(X_test, Y_test)
print(f'Test Loss: {loss}, Test Accuracy: {accuracy}')

model.save('sinniflandirma.keras')
