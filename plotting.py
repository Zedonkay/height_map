import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def plot_grid(file_name, title):
    """
    Plot the interpolated grid from a CSV file.
    
    Parameters:
    file_name (str): Path to the CSV file containing the grid data.
    title (str): Title of the plot.
    """
    try:
        # Load the grid data from the CSV file
        grid_df = pd.read_csv(file_name)
        
        # Create a meshgrid for plotting
        x = grid_df.columns.astype(float).values
        y = grid_df.index.astype(float).values
        X, Y = np.meshgrid(x, y)
        Z = grid_df.values
        
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
        plt.show()
    except Exception as e:
        print("Error plotting grid:", e)
        with open('error_log.txt', 'a') as f:
            f.write("Error plotting grid: " + str(e) + "\n")
            f.write(traceback.format_exc() + "\n")
        raise

# Example usage
plot_grid("rbf_output.csv", "RBF Interpolated Grid")
