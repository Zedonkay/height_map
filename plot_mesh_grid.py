import numpy as np

import matplotlib.pyplot as plt

def plot_grid(filename, title, save_file, terrain):
    # Load the saved grid_x, grid_y, and z_rbf from files
    grid_x = np.load(filename + "x_" + terrain + ".npy")
    grid_y = np.load(filename + "y_" + terrain + ".npy")
    grid_z = np.load(filename + "z_" + terrain + ".npy")
    
    # Plot the 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(grid_x, grid_y, grid_z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    plt.savefig(save_file)

def plot_rbf():
    # Plot the rbf interpolated grid for the no bump data
    grid_file = 'rbf/no_bump/grid_'
    plot_grid(grid_file, 'RBF Interpolated Grid - No Bump', 'rbf/no_bump/rbf_no_bump.png','no_bump')

    # Plot the rbf interpolated grid for the bump data
    grid_file = 'rbf/bump/grid_'
    plot_grid(grid_file, 'RBF Interpolated Grid - Bump', 'rbf/bump/rbf_bump.png','bump')

def main():
    plot_rbf()

if __name__ == '__main__':
    main()
