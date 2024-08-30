import pandas as pd
import numpy as np 

df = pd.read_csv('terrain_with_bump.csv')
position_x = []
position_y = []
position_z = []

for column in df.columns:
    if 'X' in column:
        position_x.append(df[column].mean())
    elif 'Z' in column:
        position_y.append(df[column].mean())
    elif 'Y' in column:
        position_z.append(df[column].mean())
print(np.shape(position_x), np.shape(position_y), np.shape(position_z))
df = pd.DataFrame({'x': position_x, 'y': position_y, 'z': position_z})

df.to_csv('formatted_data_bump.csv', index=False)

