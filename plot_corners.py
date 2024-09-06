import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the CSV file
file_path = 'start_end.csv'
data = pd.read_csv(file_path)

# Extract marker names and coordinates from the CSV
marker_names = [
    "fish:Marker1", "fish:Marker2", "fish:Marker3",
    "fish 002:Marker1", "fish 002:Marker2", "fish 002:Marker3"
]

# Extract X, Y, Z coordinates for each marker
marker_coords = {
    "fish:Marker1": data.iloc[1, 0:3].astype(float).values,
    "fish:Marker2": data.iloc[1, 3:6].astype(float).values,
    "fish:Marker3": data.iloc[1, 6:9].astype(float).values,
    "fish 002:Marker1": data.iloc[1, 9:12].astype(float).values,
    "fish 002:Marker2": data.iloc[1, 12:15].astype(float).values,
    "fish 002:Marker3": data.iloc[1, 15:18].astype(float).values
}

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot each marker with its coordinates
for marker, coords in marker_coords.items():
    ax.scatter(coords[0], coords[1], coords[2], label=marker)
    ax.text(coords[0], coords[1], coords[2], marker, fontsize=9)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Marker Plot')

# Display the plot
plt.show()
