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

def plot_mesh_grid(rbf_model, x, y):
    # Define the grid for interpolation
    grid_x, grid_y = np.meshgrid(np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100))

    # Interpolate the grid
    z_rbf = rbf_model(grid_x, grid_y)

    # Plot the mesh grid
    plt.figure()
    plt.pcolormesh(grid_x, grid_y, z_rbf, shading='auto')
    plt.colorbar()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Interpolated Mesh Grid')
    plt.show()

def main():
    # Load data
    file_path = 'formatted_data.csv'
    x, y, z = load_data(file_path)

    # Perform RBF Interpolation
    rbf = perform_rbf_interpolation(x, y, z)

    if rbf is not None:
        # Save the model
        model_file_path = 'rbf_model.pkl'
        save_model(rbf, model_file_path)

        # Plot the mesh grid
        plot_mesh_grid(rbf, x, y)

if __name__ == "__main__":
    main()
