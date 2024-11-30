import numpy as np


# Run this command to install google drive
# pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib

# Saving and Loading NumPy Arrays
# Create an identity matrix
identity_matrix = np.eye(3)
print("identity matrix:\n", identity_matrix)
np.save('identity_matrix', identity_matrix)
loaded_array = np.load('identity_matrix.npy')
print("loaded array:\n", loaded_array)

# savez function
# Generate a 3x3 identity matrix
identity_matrix_3 = np.identity(3)
print("3x3 Identity Matrix:")
print(identity_matrix_3)

# Generate a 4x4 identity matrix
identity_matrix_4 = np.identity(4)
print("\n4x4 Identity Matrix:")
print(identity_matrix_4)

np.savez('multi_matrices.npz',
         identity_matrix_3=identity_matrix_3,
         identity_matrix_4=identity_matrix_4)

# Load the files now

loaded_data = np.load('multi_matrices.npz')

loaded_identity_matrix_3 = loaded_data['identity_matrix_3']
loaded_identity_matrix_4 = loaded_data['identity_matrix_4']

print("Loaded 3x3 Identity Matrix:")
print(loaded_identity_matrix_3)

print("\nLoaded 4x4 Identity Matrix:")
print(loaded_identity_matrix_4)