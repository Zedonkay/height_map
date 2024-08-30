import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plot_grid(file_name, title,savename):
    """
    Plot the interpolated grid from a CSV file.
    
    Parameters:
    file_name (str): Path to the CSV file containing the grid data.
    title (str): Title of the plot.
    """
    try:
        # Load the grid data from the CSV file
        x = np.load()
        
        # Plot the grid data
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis')
        
        # Set plot title and labels
        ax.set_title(title)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        
        # Show the plot
        plt.savefig(savename)
    except Exception as e:
        print("Error plotting grid:", e)
        with open('error_log.txt', 'a') as f:
            f.write("Error plotting grid: " + str(e) + "\n")
            f.write(traceback.format_exc() + "\n")
        raise

def main():
    # Plot the rbf interpolated grid for the no bump data
    grid_file = 'rbf/no_bump/grid_'
    plot_grid(grid_file, 'RBF Interpolated Grid - No Bump', 'rbf/no_bump/rbf_no_bump.png')

    #Plot the uk interpolated grid for the no bump data
    grid_file = 'uk/no_bump/universal_kriging_grid_'
    plot_grid(grid_file, 'UK Interpolated Grid - No Bump', 'uk/no_bump/uk_no_bump.png')

    #plot the ok interpolated grid for the no bump data
    grid_file = 'ok/no_bump/ordinary_kriging_grid_'
    plot_grid(grid_file, 'OK Interpolated Grid - No Bump', 'ok/no_bump/ok_no_bump.png')

if __name__ == '__main__':
    main()

