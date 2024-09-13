import numpy as np

from las_test import x, y, z, r, g, b, num_points

xyz = np.vstack([x, y, z])
print(xyz[:4], xyz.shape, sep='\n') #, sep='\n')
xxyz = np.rot90(xyz) #
print(xxyz.shape, xxyz[:4], sep='\n')

point_size = np.full(
  shape=num_points,
  fill_value=8)

rgb = np.vstack([x, y, z])
las_dat = np.rot90(np.vstack([x, y, z, point_size, x, y]))
print('las for gl', las_dat[:3])
ravel_dat = np.ravel(las_dat[:2])
np.set_printoptions(suppress=True)
print('las for gl', ravel_dat)
print(type(x[0]), type(ravel_dat[0]))

las_dat2 = np.ravel(np.rot90(np.vstack([x/max(x), y/max(y), z/max(z), point_size, x/max(x), y/max(y)]))).tolist()
las_dat2 = np.round(las_dat2, 2)
print(las_dat2[:12])