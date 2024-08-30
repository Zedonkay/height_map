import numpy as np

import matplotlib.pyplot as plt

def plot_grid(filename, title, save_file):
    # Load the saved grid_x, grid_y, and z_rbf from files
    grid_x = np.load(filename+"x.npy")
    grid_y = np.load(filename+"y.npy")
    z_rbf = np.load(filename+"z.npy")
    
    # Plot the 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(grid_x, grid_y, z_rbf)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    plt.savefig(save_file)

def main():
    # Plot the rbf interpolated grid for the no bump data
    grid_file ='rbf/no_bump/rbf_grid_'
    plot_grid(grid_file, 'RBF Interpolated Grid - No Bump', 'rbf/no_bump/rbf_no_bump.png')

    #Plot the uk interpolated grid for the no bump data
    grid_file = 'uk/no_bump/universal_kriging_grid_'
    plot_grid(grid_file, 'UK Interpolated Grid - No Bump', 'uk/no_bump/uk_no_bump.png')

    #plot the ok interpolated grid for the no bump data
    grid_file = 'ok/no_bump/ordinary_kriging_grid_'
    plot_grid(grid_file, 'OK Interpolated Grid - No Bump', 'ok/no_bump/ok_no_bump.png')

if __name__ == '__main__':
    main()
