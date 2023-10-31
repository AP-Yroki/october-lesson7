import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

def ShapeSizeCalc(arr):
    shape = arr.shape
    size = arr.size
    return f'shape = {shape}, size = {size}'

print(ShapeSizeCalc(arr))