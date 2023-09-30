import numpy as np
import matplotlib.pyplot as plt

def noise_function(time_range, noise_type='normal', mean=0, stddev=1):
    if noise_type == 'normal':
        noise = np.random.normal(mean, stddev, len(time_range))
    elif noise_type == 'uniform':
        noise = np.random.uniform(mean, stddev, len(time_range))
    elif noise_type == 'poisson':
        noise = np.random.poisson(mean, len(time_range))
    else:
        raise ValueError("Invalid noise type. Possible values: 'normal', 'uniform', 'poisson'")
    
    return noise

# Define the time range
time_range = np.linspace(0, 1, 100)

# Generate noise using the noise_function
noise = noise_function(time_range, noise_type='normal', mean=0, stddev=0.1)

# Add noise to a function
function_with_noise =  noise

# Plot the function with noise
plt.figure(figsize=(10, 4))
plt.plot(time_range, function_with_noise, label='Function with Noise')
plt.xlabel('Time')
plt.ylabel('Function Value')
plt.title('Function with Noise')
plt.legend()
plt.grid(True)
plt.show()
