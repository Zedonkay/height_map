import pandas as pd
import numpy as np
from pykrige.uk import UniversalKriging
import matplotlib.pyplot as plt
import pickle

data = pd.read_csv('formatted_data.csv')
x = data['px'].values
y = data['py'].values
height = data['pz'].values
grid_x, grid_y = np.meshgrid(np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100))

print("training model")
uk = UniversalKriging(x, y, height, variogram_model='linear')
z, ss = uk.execute('grid', grid_x, grid_y)
# Save the model to a file
with open('universal_kriging_model.pkl', 'wb') as f:
    pickle.dump(uk, f)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(grid_x, grid_y, z, cmap='viridis')

plt.show()