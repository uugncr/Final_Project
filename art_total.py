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

# Create a figure with 3 subplots
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Plot 1: N vs FOM
for label, file_path in files.items():
    data = pd.read_csv(file_path)
    axes[0].scatter(data['N'], data['fom'], label=label, s=0.5)
axes[0].set_title("N vs FOM")
axes[0].set_xlabel("N")
axes[0].set_ylabel("FOM")
axes[0].legend()
axes[0].grid(True)

# Plot 2: Tail Integral vs FOM
for label, file_path in files.items():
    data = pd.read_csv(file_path)
    axes[1].scatter(data['tail_integral'], data['fom'], label=label, s=0.5)
axes[1].set_title("Tail Integral vs FOM")
axes[1].set_xlabel("Tail Integral")
axes[1].set_ylabel("FOM")
axes[1].legend()
axes[1].grid(True)

# Plot 3: Total Integral vs Tail Integral
for label, file_path in files.items():
    data = pd.read_csv(file_path)
    axes[2].scatter(data['total_integral'], data['tail_integral'], label=label, s=0.5)
axes[2].set_title("Total Integral vs Tail Integral")
axes[2].set_xlabel("Total Integral")
axes[2].set_ylabel("Tail Integral")
axes[2].legend()
axes[2].grid(True)

# Adjust layout and show the plots
plt.tight_layout()
plt.show()