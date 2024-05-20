import matplotlib.pyplot as plt

def plot_data(file_path, dx, dy, color):
    # Open the file and read the data
    with open(file_path, 'r') as file_obj:
        data = file_obj.readlines()

    # Extract x and y coordinates from the data
    x_coords = []
    y_coords = []
    for line in data[1:]:
        line = line.strip().split(',')
        x = float(line[0]) + dx  # Translate x-coordinate
        y = float(line[1]) + dy  # Translate y-coordinate
        x_coords.append(x)
        y_coords.append(y)

    # Create the scatter plot with the translated points
    plt.scatter(x_coords, y_coords, color=color)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Translated Scatter Plot')
    plt.grid(True)

    # Show the plot
    plt.show()

# Example usage
file_path = r"C:\Users\muley\OneDrive\Desktop\tafadzwa\coordinate_file.csv"
dx = 2.0  # Translation in x-direction
dy = 3.0  # Translation in y-direction
color = 'red'  # Color for the translated points

plot_data(file_path, dx, dy, color)