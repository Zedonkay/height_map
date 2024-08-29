import pandas as pd
import numpy as np 

df = pd.read_csv('filtered_data.csv')
position_x = []
position_y = []
position_z = []

for column in df.columns:
    if 'px' in column:
        position_x.append(df[column].mean())
    elif 'py' in column:
        position_y.append(df[column].mean())
    elif 'pz' in column:
        position_z.append(df[column].mean())
print(np.shape(position_x), np.shape(position_y), np.shape(position_z))
df = pd.DataFrame({'px': position_x, 'py': position_y, 'pz': position_z})

df.to_csv('formatted_data.csv', index=False)

