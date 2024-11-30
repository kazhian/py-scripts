import numpy as np

# Operations on Matrices
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
identity_matrix = np.eye(3)

print("matrix:\n", matrix)
print("identity matrix:\n", identity_matrix)
print("addition:", matrix + identity_matrix)
print("subtraction:", matrix - identity_matrix)
print("multiplication:", matrix * identity_matrix)  
print("division:", matrix / identity_matrix)

# Linear Algebra    
matrix1 = np.arange(1, 10).reshape(3, 3)
matrix2 = np.arange(11, 20).reshape(3, 3)

# Linear algebra functions
print("matrix1:\n", matrix1)
print("matrix2:\n", matrix2)
print("matrix1 @ matrix2:\n", matrix1 @ matrix2)

# Transpose
print("matrix1:\n", matrix1)
print("matrix1.T:\n", matrix1.T)
print("np.transpose(matrix1):\n", np.transpose(matrix1))
