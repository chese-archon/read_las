import pylas
import rasterio
from rasterio.crs import CRS
from rasterio.transform import Affine
import numpy as np
from scipy.interpolate import griddata
from matplotlib.cbook import get_sample_data
from matplotlib.colors import LightSource
import matplotlib.pyplot as plt

inFile = pylas.read("C:/Users/zilberman/Downloads/serpent-small.las")

print('The total point is:', inFile.header.point_count)

print(*inFile.point_format.dimension_names, sep='\n')
# x, y, z
points = list(zip(inFile.x, inFile.y, inFile.z))
x, y, z = inFile.x, inFile.y, inFile.z
# Assign band variable
r = inFile.red
g = inFile.green
b = inFile.blue

#plot
# Create figure
fig = plt.figure()#figsize=[20, 5])

# Create RGB natural color composite
#RGB = np.dstack((Red, Green, Blue))

# Let's see how our color composite looks like
#plt.imshow(RGB)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, s=0.3,label='las file')
# Customize plot
plt.title('True color image', fontweight='bold')
plt.xlabel('width')
plt.ylabel('height')


# Show plot
plt.show()