import numpy as np
import time

t_start = time.time()

a = np.random.random([6000,6000])
a = a + a.T
b = np.linalg.pinv(a)

t_delta = time.time() - t_start

print('Seconds taken to invert a symmetric 6000x6000 matrix: %f' % (t_delta))
