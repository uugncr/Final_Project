import pandas as pd
import matplotlib.pyplot as plt

# Load the data from your files
data_25 = pd.read_csv('/Users/uuu/Final_Project/parameters25.csv')
data_50 = pd.read_csv('/Users/uuu/Final_Project/parameters50.csv')
data_100 = pd.read_csv('/Users/uuu/Final_Project/parameters100.csv')

# Plotting the data
plt.figure(figsize=(10, 6))

# Plot each dataset with the specified color
plt.scatter(data_25['N'], data_25['fom'], color='red', label='Parameter 25')
plt.scatter(data_50['N'], data_50['fom'], color='blue', label='Parameter 50')
plt.scatter(data_100['N'], data_100['fom'], color='green', label='Parameter 100')

# Adding labels and title
plt.xlabel('N (x-axis)')
plt.ylabel('fom (y-axis)')
plt.title('Scatter Plot of Parameters')
plt.legend()

# Show the plot
plt.show()

