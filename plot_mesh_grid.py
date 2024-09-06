import numpy as np
import matplotlib.pyplot as plt

def plot_grid(filename_grid, filename, title):
    # Load the saved grid_x, grid_y, and z_rbf from files
    grid_x, grid_y, grid_z = add_constant_to_grids(filename_grid)
    
    # Plot the 3D scatter plot with gradient colors based on z value
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    cmap = plt.get_cmap('summer')
    cmap=cmap.reversed()
    ax.scatter(grid_x, grid_y, grid_z, c=grid_z, cmap=cmap)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)
    ax.set_xlim([np.min(grid_x), np.max(grid_x)])
    ax.set_ylim([np.min(grid_y), np.max(grid_y)])
    ax.set_zlim([np.min(grid_z), np.max(grid_z)*2.5])
    
    # Save the plot as PNG
    save_file_png = filename + '.png'
    plt.savefig(save_file_png)
    
    # Save the plot as SVG
    save_file_svg = filename + '.svg'
    plt.savefig(save_file_svg, format='svg')

def plot_sim_grid(filename_grid, filename, title):
    grid_x=np.load(filename_grid + "x" + ".npy")
    grid_y=np.load(filename_grid + "y" + ".npy")
    grid_z = np.load(filename_grid + "z" + ".npy")
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(grid_x, grid_y, grid_z)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(title)

    # Save the plot as PNG
    save_file_png = filename + '.png'
    plt.savefig(save_file_png)

    # Save the plot as SVG
    save_file_svg = filename + '.svg'
    plt.savefig(save_file_svg, format='svg')
def plot_rbf():
    # # Plot the rbf interpolated grid for the no bump data
    # grid_file = 'rbf/no_bump/rbf_grid_'
    # plot_file= 'rbf/no_bump/rbf_plot'
    # plot_grid(grid_file, plot_file,'Extracted Terrain Model')

    # Plot the rbf interpolated grid for the bump data
    grid_file = 'rbf/bump/rbf_grid_'
    plot_file= 'rbf/bump/rbf_plot'
    plot_grid(grid_file, plot_file,'Extracted Terrain Model')

    grid_file = 'rbf/sim/rbf_grid_'
    plot_file= 'rbf/sim/rbf_plot'
    plot_sim_grid(grid_file, plot_file,'Simulated Terrain Model')

def add_constant_to_grids(filename):
    # Load the saved grid_x, grid_y, and z_rbf from files
    grid_x = np.load(filename + "x" + ".npy")
    grid_y = np.load(filename + "y" + ".npy")
    grid_z = np.load(filename + "z" + ".npy")
    
    # Add a constant value to each grid
    constant_x = 750
    constant_y = 0
    grid_x += constant_x
    grid_y += constant_y
    
    # Return the updated grids
    return grid_x, grid_y, grid_z

def main():
    plot_rbf()

if __name__ == '__main__':
    main()
