import numpy as np

def ArrayIndexing(arr, rows, val):
    selected_rows = arr[rows]
    transformed_array = selected_rows[:, ::val + 1]
    return transformed_array

array = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
rows = [0, 1]
val = 2

result_array = ArrayIndexing(array, rows, val)
print(result_array)
