import numpy as np
import pandas as pd
from scipy.interpolate import Rbf
import pickle

import matplotlib.pyplot as plt

def load_data(file_path):
    # Load data from CSV
    data = pd.read_csv(file_path)
    x = data['x'].values
    y = data['y'].values
    z = data['z'].values
    return x, y, z

def perform_rbf_interpolation(x, y, z):
    try:
        # Perform RBF Interpolation
        rbf = Rbf(x, y, z, function='multiquadric', epsilon=2)
        print("RBF Interpolation completed successfully.")
        return rbf
    except Exception as e:
        error_message = str(e)
        with open('error_log.txt', 'w') as f:
            f.write(error_message)
        print("RBF Interpolation failed. Error message saved in error_log.txt.")
        return None

def save_model(rbf, file_path):
    try:
        # Save the model to a file
        with open(file_path, 'wb') as f:
            pickle.dump(rbf, f)
        print("Model saved successfully.")
    except Exception as e:
        error_message = str(e)
        with open('error_log.txt', 'w') as f:
            f.write(error_message)
        print("Failed to save the model. Error message saved in error_log.txt.")

def main():
    # Load data
    file_path = 'formatted_data_bump.csv'
    x, y, z = load_data(file_path)

    # Perform RBF Interpolation
    rbf = perform_rbf_interpolation(x, y, z)

    # Define the grid for interpolation
    grid_x, grid_y = np.meshgrid(np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100))

    if rbf is not None:
         # Interpolate the grid
        z_rbf = rbf(grid_x, grid_y)
        # Save the model
        model_file_path = 'rbf/bump/rbf_model_bump.pkl'
        save_model(rbf, model_file_path)
        # Save the grid_x, grid_y, and z_rbf to files
        np.save('rbf/no_bump/grid_x_bump.npy', grid_x)
        np.save('rbf/no_bump/grid_y_bump.npy', grid_y)
        np.save('rbf/no_bump/z_rbf_bump.npy', z_rbf)

       




if __name__ == "__main__":
    main()
