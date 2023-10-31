import numpy as np

list = [[1, 2, 3], [4, 5, 6]]
def ListToNumpy(list):
    np_array = np.array(list, dtype=float)
    return np_array

print(ListToNumpy(list))