import pandas as pd
import numpy as np
from pykrige.ok import OrdinaryKriging
from pykrige.uk import UniversalKriging
from pykrige.rk import RegressionKriging
import pickle
import traceback
import dask.dataframe as dd
# from skgstat import Variogram, OrdinaryKriging as SKGOrdinaryKriging
from sklearn.linear_model import LinearRegression



def load_data(file_path):
    """
    Load data from a CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file.
    
    Returns:
    tuple: Arrays of x, y, z coordinates.
    """
    try:
        print("Loading data from CSV file...")
        data = dd.read_csv(file_path).compute()
        x = data['x'].values
        y = data['y'].values
        z = data['z'].values
        print("Data loaded successfully.")
        return x, y, z
    except Exception as e:
        print("Error loading data:", e)
        with open('error_log.txt', 'a') as f:
            f.write("Error loading data: " + str(e) + "\n")
            f.write(traceback.format_exc() + "\n")
        raise

def save_model(model, file_name):
    """
    Save the model to a file.
    
    Parameters:
    model: The model to be saved.
    file_name (str): The name of the file to save the model.
    """
    try:
        with open(file_name, 'wb') as f:
            pickle.dump(model, f)
        print(f"Model saved as {file_name}.")
    except Exception as e:
        print("Error saving model:", e)
        with open('error_log.txt', 'a') as f:
            f.write("Error saving model: " + str(e) + "\n")
            f.write(traceback.format_exc() + "\n")
        raise

def save_grid(grid, file_name):
    """
    Save the interpolated grid to a file.
    
    Parameters:
    grid: The interpolated grid to be saved.
    file_name (str): The name of the file to save the grid.
    """
    try:
        # Convert MaskedArray to ndarray
        if isinstance(grid, np.ma.MaskedArray):
            grid = grid.filled(np.nan)
        np.save(file_name, grid)
        print(f"Interpolated grid saved as {file_name}.")
    except Exception as e:
        print("Error saving grid:", e)
        with open('error_log.txt', 'a') as f:
            f.write("Error saving grid: " + str(e) + "\n")
            f.write(traceback.format_exc() + "\n")
        raise

def ordinary_kriging(x, y, z, gridx, gridy):
    """
    Perform Ordinary Kriging.
    
    Parameters:
    x, y, z: Arrays of coordinates and values.
    gridx, gridy: Grid coordinates for interpolation.
    """
    try:
        print("Performing Ordinary Kriging...")
        ok = OrdinaryKriging(x, y, z, variogram_model='linear')
        save_model(ok, 'ordinary_kriging_model.pkl')
    except Exception as e:
        print("Error in generating Ordinary Kriging model:", e)
        with open('error_log.txt', 'a') as f:
            f.write("Error in generating Ordinary Kriging model: " + str(e) + "\n")
            f.write(traceback.format_exc() + "\n")
        raise

    try:
        z_pred, ss = ok.execute('grid', gridx, gridy)
        save_grid(z_pred, 'ordinary_kriging_grid.npy')
    except Exception as e:
        print("Error in predicting Ordinary Kriging grid:", e)
        with open('error_log.txt', 'a') as f:
            f.write("Error in predicting Ordinary Kriging grid: " + str(e) + "\n")
            f.write(traceback.format_exc() + "\n")
        raise

def universal_kriging(x, y, z, gridx, gridy):
    """
    Perform Universal Kriging.
    
    Parameters:
    x, y, z: Arrays of coordinates and values.
    gridx, gridy: Grid coordinates for interpolation.
    """
    try:
        print("Performing Universal Kriging...")
        uk = UniversalKriging(x, y, z, variogram_model='linear', drift_terms=['regional_linear'])
        save_model(uk, 'universal_kriging_model.pkl')
    except Exception as e:
        print("Error in generating Universal Kriging model:", e)
        with open('error_log.txt', 'a') as f:
            f.write("Error in generating Universal Kriging model: " + str(e) + "\n")
            f.write(traceback.format_exc() + "\n")
        raise

    try:
        z_pred, ss = uk.execute('grid', gridx, gridy)
        save_grid(z_pred, 'universal_kriging_grid.npy')
    except Exception as e:
        print("Error in predicting Universal Kriging grid:", e)
        with open('error_log.txt', 'a') as f:
            f.write("Error in predicting Universal Kriging grid: " + str(e) + "\n")
            f.write(traceback.format_exc() + "\n")
        raise


def main():
    """
    Main function to perform all Kriging methods.
    """
    file_path = 'formatted_data.csv'
    x, y, z = load_data(file_path)
    x_reshaped = x.reshape(-1,1)
    y_reshaped = y.reshape(-1,1)
    z_reshaped = z.reshape(-1,1)
    gridx = np.linspace(min(x), max(x), 100)
    gridy = np.linspace(min(y), max(y), 100)

    ordinary_kriging(x_reshaped, y_reshaped, z_reshaped, gridx, gridy)
    universal_kriging(x_reshaped, y_reshaped, z_reshaped, gridx, gridy)

if __name__ == "__main__":
    main()
