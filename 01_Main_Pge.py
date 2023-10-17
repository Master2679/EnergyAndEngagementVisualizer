import matplotlib.pyplot as plt
import pandas as pd
from decimal import Decimal, getcontext

# Set precision for Decimal
getcontext().prec = 50

# Accept user input for data points
def get_user_input():
    print('Enter y-axis data points. One point per line. When done, type STOP.')
    y_points = []
    while (line.upper() != 'STOP'):
        line = input()
        y_points.append(Decimal(line))
    
    # Generate x-axis data points (iterations)
    x_points = list(range(1, len(y_points) + 1))
    return list(zip(x_points, y_points))

# Get user inputted error value
def get_error_value():
    error = input('Enter the absolute error value (e.g., 1.2e-20 for 1.2 x 10^-20): ')
    return Decimal(error)

# Plotting the data with custom axis labels
def generate_graph(data_points, y_label):
    x, y = zip(*data_points)
    plt.plot(x, [float(val) for val in y])
    plt.xlabel('Number of Iterations')
    plt.ylabel(y_label)
    plt.title(f'Graph of {y_label}')
    plt.show()

# Generate absolute error values based on user inputted error
def generate_absolute_errors(data_points, error_value):
    return [(x, abs(y - error_value)) for x, y in data_points]

# Save the data to an Excel file using pandas
def save_to_excel(data_points):
    df = pd.DataFrame(data_points, columns=['Number of Iterations', 'Absolute Error'])
    df['Absolute Error'] = df['Absolute Error'].apply(lambda x: float(x))
    filename = 'absolute_errors3.xlsx'
    df.to_excel(filename, index=False)
    print(f'Data saved to {filename}')

# Run the functions
data_points = get_user_input()
error_value = get_error_value()
generate_graph(data_points, 'Value')
absolute_errors = generate_absolute_errors(data_points, error_value)
generate_graph(absolute_errors, 'Absolute Error')
save_to_excel(absolute_errors)