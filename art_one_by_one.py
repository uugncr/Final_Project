import pandas as pd
import os
import matplotlib.pyplot as plt

# File paths
# Get the base directory of the current script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Define file paths relative to the script's location
files = {
    "par25": os.path.join(base_dir, "data_all", "par25.csv"),
    "par50": os.path.join(base_dir, "data_all", "par50.csv"),
    "par100": os.path.join(base_dir, "data_all", "par100.csv")
}

# Plot 1: N vs FOM
plt.figure(figsize=(10, 6))
for label, file_path in files.items():
    data = pd.read_csv(file_path)
    plt.scatter(data['N'], data['fom'], label=label, s=0.5)
plt.title("N vs FOM")
plt.xlabel("N")
plt.ylabel("FOM")
plt.legend()
plt.grid(True)
plt.show()

# Plot 2: Tail Integral vs FOM
plt.figure(figsize=(10, 6))
for label, file_path in files.items():
    data = pd.read_csv(file_path)
    plt.scatter(data['tail_integral'], data['fom'], label=label, s=0.5)
plt.title("Tail Integral vs FOM")
plt.xlabel("Tail Integral")
plt.ylabel("FOM")
plt.legend()
plt.grid(True)
plt.show()

# Plot 3: Total Integral vs Tail Integral
plt.figure(figsize=(10, 6))
for label, file_path in files.items():
    data = pd.read_csv(file_path)
    plt.scatter(data['total_integral'], data['tail_integral'], label=label, s=0.5)
plt.title("Total Integral vs Tail Integral")
plt.xlabel("Total Integral")
plt.ylabel("Tail Integral")
plt.legend()
plt.grid(True)
plt.show()