# Load and visualize data from a MATLAB .mat file using SciPy and Matplotlib.
# Useful for analyzing scientific measurements like image-based signal intensities.


import scipy.io
import matplotlib.pyplot as plt
import numpy as np

# Load the .mat file
mat = scipy.io.loadmat('your_file.mat')  # Replace with your actual file name

# Access a specific variable from the file
data = mat['CYratioCyt']  # Replace with the actual variable name from the .mat file

# Print the shape of the data
print("Shape of CYratioCyt:", data.shape)

# Display the data (assumes it's 2D or can be reshaped to 2D)
plt.imshow(data, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title('CYratioCyt Visualization')
plt.show()
