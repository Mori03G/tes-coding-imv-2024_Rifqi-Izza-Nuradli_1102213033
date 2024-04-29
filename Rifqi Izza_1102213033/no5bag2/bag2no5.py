import numpy as np
 
a = np.array([1, 2, 3, 4, 5])
print("a: ", a)
 
v = np.array([4, 3, 2, 1, 2, 3, 4])
print("b: ", v)
 
print(np.convolve(a, v, mode='full'))