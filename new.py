import os
import numpy as np

dizin = '/Users/uuu/Final_Project'
data_path = os.path.join(dizin, 'gaussian.csv')
data = np.genfromtxt(data_path, delimiter=',')

std = np.std(data)
mean = np.mean(data)

peak = None

for i in range(1, len(data) - 1):
    if data[i] > data[i-1] and data[i] > data[i+1]:
        peak = i
        break

if peak is not None:
    print("En yüksek tepe noktası:", (peak, data[peak]))
else:
    print("Tepe noktası bulunamadı!")
    
print(mean, std)
