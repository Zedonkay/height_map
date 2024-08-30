import numpy as np
import pandas as pd
from scipy.interpolate import Rbf
import pickle

# Load your data from CSV
data = pd.read_csv('formatted_data.csv')
x = data['x'].values
y = data['y'].values
z = data['z'].values

# Perform RBF Interpolation
print("Performing RBF Interpolation...")
try:
    rbf = Rbf(x, y, z, function='multiquadric', epsilon=2)
    print("RBF Interpolation completed successfully.")
except Exception as e:
    error_message = str(e)
    with open('error_log.txt', 'w') as f:
        f.write(error_message)
    print("RBF Interpolation failed. Error message saved in error_log.txt.")

# Save the model to a file
print("Saving the model to rbf_model.pkl...")
try:
    with open('rbf_model.pkl', 'wb') as f:
        pickle.dump(rbf, f)
    print("Model saved successfully.")
except Exception as e:
    error_message = str(e)
    with open('error_log.txt', 'w') as f:
        f.write(error_message)
    print("Failed to save the model. Error message saved in error_log.txt.")

# Define the grid for interpolation
grid_x, grid_y = np.meshgrid(np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100))

# Interpolate the grid
print("Interpolating the grid...")
try:
    z_rbf = rbf(grid_x, grid_y)
    print("Grid interpolation completed successfully.")
except Exception as e:
    error_message = str(e)
    with open('error_log.txt', 'w') as f:
        f.write(error_message)
    print("Grid interpolation failed. Error message saved in error_log.txt.")

# Save the interpolated grid to a CSV file
print("Saving the interpolated grid to rbf_output.csv...")
try:
    np.savetxt('rbf_output.csv', z_rbf, delimiter=',')
    print("Interpolated grid saved successfully.")
except Exception as e:
    error_message = str(e)
    with open('error_log.txt', 'w') as f:
        f.write(error_message)
    print("Failed to save the interpolated grid. Error message saved in error_log.txt.")
