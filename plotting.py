import pandas as pd
import numpy as np
from pykrige.uk import UniversalKriging
import pickle
from multiprocessing import Pool

# Load data
data = pd.read_csv('formatted_data.csv')
x = data['px'].values
y = data['py'].values
height = data['pz'].values

# Define grid
grid_x, grid_y = np.meshgrid(np.linspace(min(x), max(x), 100), np.linspace(min(y), max(y), 100))

# Function to process a batch
def n(args):
    start, end = args
    x_batch = x[start:end]
    y_batch = y[start:end]
    height_batch = height[start:end]
    uk = UniversalKriging(x_batch, y_batch, height_batch, variogram_model='linear')
    z_batch, ss_batch = uk.execute('grid', grid_x, grid_y)
    return z_batch

# Batch size
batch_size = 500

# Process batches in parallel using multiprocessing
with Pool() as pool:
    results = pool.map(process_batch, [(i, min(i+batch_size, len(x))) for i in range(0, len(x), batch_size)])

# Combine results (consider a different method if averaging is not suitable)
z_combined = np.mean(results, axis=0)

# Train the final model on the entire dataset
uk_final = UniversalKriging(x, y, height, variogram_model='linear')
z_final, ss_final = uk_final.execute('grid', grid_x, grid_y)

# Save the final model to a file
with open('universal_kriging_model.pkl', 'wb') as f:
    pickle.dump(uk_final, f)

# Save grid_x, grid_y, and z_combined to a CSV file
data = {'grid_x': grid_x.flatten(), 'grid_y': grid_y.flatten(), 'z': z_combined.flatten()}
df = pd.DataFrame(data)
df.to_csv('grid_data.csv', index=False)
