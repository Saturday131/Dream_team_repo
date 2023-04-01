import numpy as np

matrix = np.array([[1, 2], [3, 4], [5, 6]])

arr = matrix.reshape(-1)

mean = np.mean(arr)

std = np.std(arr)

new_matrix = arr.reshape(matrix.shape[0], matrix.shape[1])

mult_matrix = np.multiply(matrix, new_matrix)

sum_mult_matrix = np.sum(mult_matrix)

print(f"Original matrix:\n{matrix}")
print(f"Reshaped 1D array:\n{arr}")
print(f"Mean of 1D array:\n{mean}")
print(f"Standard deviation of 1D array:\n{std}")
print(f"Reshaped 2D matrix:\n{new_matrix}")
print(f"Element-wise multiplied matrix:\n{mult_matrix}")
print(f"Sum of all elements in element-wise multiplied matrix:\n{sum_mult_matrix}")



print("Whatever")
print("some more text")

mult_matrices = sum_mult_matrix * sum_mult_matrix

print(f"Multiplied matrices:\n{mult_matrices}")
