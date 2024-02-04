import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Load the data from your files
data_25 = pd.read_csv('/Users/uuu/Final_Project/parameters25_50000.csv')
data_50 = pd.read_csv('/Users/uuu/Final_Project/parameters50_50000.csv')
data_100 = pd.read_csv('/Users/uuu/Final_Project/parameters100_50000.csv')

# Plotting the data
plt.figure(figsize=(10, 6))

# Plot density plot for each dataset with specified color
sns.kdeplot(data_25['total_integral'], color='red', label='Parameter 25')
sns.kdeplot(data_50['total_integral'], color='green', label='Parameter 50')
sns.kdeplot(data_100['total_integral'], color='blue', label='Parameter 100')

# Add labels and title
plt.xlabel('X-axis label')
plt.ylabel('Density')
plt.title('Density Plots for Different Parameters')

# Show legend
plt.legend()

# Show plot
plt.show()
