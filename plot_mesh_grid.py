import numpy as np

import matplotlib.pyplot as plt

def plot_grid(filename, title, save_file):
    # Load the saved grid_x, grid_y, and z_rbf from files
    grid_x = np.load(filename + "x.npy")
    grid_y = np.load(filename + "y.npy")
    z_rbf = np.load(filename + "z.npy")
    
    # Plot the 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(grid_x, grid_y, z_rbf)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    plt.savefig(save_file)

def plot_no_bump():
    # Plot the rbf interpolated grid for the no bump data
    grid_file = 'rbf/no_bump/rbf_grid_'
    plot_grid(grid_file, 'RBF Interpolated Grid - No Bump', 'rbf/no_bump/rbf_no_bump.png')

    # Plot the uk interpolated grid for the no bump data
    grid_file = 'uk/no_bump/universal_kriging_grid_'
    plot_grid(grid_file, 'UK Interpolated Grid - No Bump', 'uk/no_bump/uk_no_bump.png')

    # Plot the ok interpolated grid for the no bump data
    grid_file = 'ok/no_bump/ordinary_kriging_grid_'
    plot_grid(grid_file, 'OK Interpolated Grid - No Bump', 'ok/no_bump/ok_no_bump.png')

def plot_bump():
    # Plot the rbf interpolated grid for the bump data
    grid_file = 'rbf/bump/rbf_grid_'
    plot_grid(grid_file, 'RBF Interpolated Grid - Bump', 'rbf/bump/rbf_bump.png')

    # Plot the uk interpolated grid for the bump data
    grid_file = 'uk/bump/universal_kriging_grid_'
    plot_grid(grid_file, 'UK Interpolated Grid - Bump', 'uk/bump/uk_bump.png')

    # Plot the ok interpolated grid for the bump data
    grid_file = 'ok/bump/ordinary_kriging_grid_'
    plot_grid(grid_file, 'OK Interpolated Grid - Bump', 'ok/bump/ok_bump.png')

def main():
    plot_no_bump()
    plot_bump()

if __name__ == '__main__':
    main()
