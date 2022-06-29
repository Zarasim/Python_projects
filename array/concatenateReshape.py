import numpy as np

x = np.array([[1]*2, 4*[3], [5, 6]], dtype='object')

z = np.concatenate(x)

print(z)
