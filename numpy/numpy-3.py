import numpy as np

# Random functions in NumPy
rand = np.random.rand(3, 3)
print("Random array:\n", rand)
print("minimum value:", rand.min())
print("maximum value:", rand.max())
print("mean value:", rand.mean())
print("standard deviation:", rand.std())

# 1D array
rand = np.random.randint(1, 5, 10) 
print("Random 1D array:\n", rand)
print(rand > 3 )
print(rand[rand > 3])
print(rand[rand > 3].sum())
rand[rand > 3]=0
print(rand)

# 2D array
rand = np.random.randint(1, 10, [3,3])
print("Random 2D array:\n", rand)

# accessing 2D array
print("row 1:", rand[0])
print("row 1 column 1:", rand[0, 0])
print("rand[1:3,3:5]:\n", rand[1:3,3:5])
rand_copy = rand.copy()
rand_copy[:] = 3
print("change all values to 3:\rand_copy:\n", rand_copy)

matrix = np.arange(1,10).reshape(3,3)
matrix[0:2,1:2] = 0
print(matrix)

