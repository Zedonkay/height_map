import pandas as pd

def modify_csv_file(file_path, x_offset=0, y_offset=0, z_offset=0, divide_by=1):
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(file_path)

    # Add offsets to x, y, and z columns
    data['x'] += x_offset
    data['y'] += y_offset
    data['z'] += z_offset

    # Divide x, y, and z columns by divide_by
    data['x'] /= divide_by
    data['y'] /= divide_by
    data['z'] /= divide_by

    # Write the modified data back to the CSV file
    data.to_csv(file_path, index=False)

def modify_files():
    csv_file_path_no_bump = '/Users/ishayu/Documents/GitHub/height_map/formatted_data_no_bump.csv'
    csv_file_path_bump = '/Users/ishayu/Documents/GitHub/height_map/formatted_data_bump.csv'

    # Modify the no bump file
    modify_csv_file(csv_file_path_no_bump, x_offset=750, y_offset=1000, divide_by=1000)

    # Modify the bump file
    modify_csv_file(csv_file_path_bump, x_offset=1000, divide_by=1000)

if __name__ == "__main__":
    # Call the function to modify the files
    modify_files()
