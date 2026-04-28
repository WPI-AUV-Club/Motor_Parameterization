#Credit to: https://www.geeksforgeeks.org/python/3d-curve-fitting-with-python/

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import csv
# Load CSV into numpy array (x, y, z columns)
csv_data = np.loadtxt('T200_Performance.csv', delimiter=',')
#csv_data[:, 1] -= 15

x = csv_data[:, 0]
y = csv_data[:, 1]
z = csv_data[:, 2]

# Or as array of [x, y, z] rows
data = np.array([x, y, z])  # shape: (3, N)

# Define mathematical function for curve fitting
def func(xy, a, b, c, d, e, f):
    x, y = xy
    return a + b*x + c*y + d*x**2 + e*y**2 + f*x*y

# Perform curve fitting
popt, pcov = curve_fit(func, (x, y), z)

# Print optimized parameters
print(popt)

# Create 3D plot of the data points and the fitted curve
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, color='blue')
x_range = np.linspace(-6, 6, 50)
y_range = np.linspace(10, 20, 50)
X, Y = np.meshgrid(x_range, y_range)
Z = func((X, Y), *popt)
ax.plot_surface(X, Y, Z, color='red', alpha=0.5)
ax.set_xlabel('Thrust(X)')
ax.set_ylabel('Voltage(Y)')
ax.set_zlabel('Throttle')
plt.show()
