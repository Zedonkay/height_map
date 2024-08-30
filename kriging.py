import numpy as np
import pandas as pd
from pykrige.ok import OrdinaryKriging
import pickle

# Load your data from CSV
data = pd.read_csv('formatted_data.csv')
x = data['x'].values
y = data['y'].values
z = data['z'].values

# Perform Ordinary Kriging
print("Performing Ordinary Kriging...")
try:
    OK = OrdinaryKriging(x, y, z, variogram_model='spherical', verbose=False, enable_plotting=False)
    print("Ordinary Kriging completed successfully.")
except Exception as e:
    error_message = str(e)
    with open('error_log.txt', 'w') as f:
        f.write(error_message)
    print("Error occurred during Ordinary Kriging. Error message saved in error_log.txt.")

# Save the model to a file
print("Saving the model to a file...")
try:
    with open('kriging_model.pkl', 'wb') as f:
        pickle.dump(OK, f)
    print("Model saved successfully.")
except Exception as e:
    error_message = str(e)
    with open('error_log.txt', 'w') as f:
        f.write(error_message)
    print("Error occurred while saving the model. Error message saved in error_log.txt.")

# Define the grid for interpolation
grid_x, grid_y = np.meshgrid(np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100))

# Interpolate the grid
print("Interpolating the grid...")
try:
    z_kriged, ss = OK.execute('grid', grid_x, grid_y)
    print("Grid interpolation completed successfully.")
except Exception as e:
    error_message = str(e)
    with open('error_log.txt', 'w') as f:
        f.write(error_message)
    print("Error occurred during grid interpolation. Error message saved in error_log.txt.")

# Save the interpolated grid to a CSV file
print("Saving the interpolated grid to a CSV file...")
try:
    np.savetxt('kriging_output.csv', z_kriged, delimiter=',')
    print("Interpolated grid saved successfully.")
except Exception as e:
    error_message = str(e)
    with open('error_log.txt', 'w') as f:
        f.write(error_message)
    print("Error occurred while saving the interpolated grid. Error message saved in error_log.txt.")

# # Function to predict z value for specific x and y
# def predict_kriging(x_val, y_val):
#     with open('kriging_model.pkl', 'rb') as f:
#         OK = pickle.load(f)
#     z_val, ss = OK.execute('points', np.array([x_val]), np.array([y_val]))
#     return z_val[0]

# # Example usage
# print(predict_kriging(1.0, 2.0))
