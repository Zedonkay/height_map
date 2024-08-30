import numpy as np
import matplotlib.pyplot as plt

def plot_mesh_grid(x, y):
    # Load the saved grid_x, grid_y, and z_rbf from files
    grid_x = np.load('rbf/grid_x_bump.npy')
    grid_y = np.load('rbf/grid_y_bump.npy')
    z_rbf = np.load('rbf/z_rbf_bump.npy')
    
    # Plot the mesh grid
    plt.figure()
    plt.pcolormesh(grid_x, grid_y, z_rbf, shading='auto')
    plt.colorbar()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Interpolated Mesh Grid')
    plt.show()