# Learning NumPy
import numpy as np

# Creating a NumPy array
cars = ["bmw", "audi", "toyota", "subaru"]
cars_array = np.array(cars)
print("NumPy cars array:", cars_array)
print("Type of cars array:", type(cars_array))

num_array = np.array([1, 2, 3, 4, 5])
print("NumPy num array:", num_array)
print("Type of num array:", type(num_array))

# Creating a 2D NumPy array
cars_array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("NumPy 2D cars array:", cars_array_2d)
print("Type of 2D cars array:", type(cars_array_2d))

# NumPy functions
integers = np.arange(0, 10)
print("NumPy integers:", integers)

even_nums = np.arange(0, 10, 2)
print("NumPy even numbers:", even_nums)

odd_nums = np.arange(1, 10, 2)
print("NumPy odd numbers:", odd_nums)

# linspace - (stop - start) / (total elements - 1)
linespace = np.linspace(10,20,10) # 3rd param is by default is 50
print("NumPy linespace:", linespace)

# zeros and ones
zeros = np.zeros([3,5])
print("NumPy zeros:\n", zeros)

ones = np.ones(5, dtype=int)
print("NumPy ones:", ones)

# eye - identity matrix
eye = np.eye(5, dtype=int)
print("NumPy identity matrix:\n", eye)

# arrange
arrange = np.arange(0, 10, 2)
print("NumPy arrange:", arrange)

# reshape
reshape = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
reshape = reshape.reshape(3, 4)
print("NumPy reshape:\n", reshape)

reshape = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
if len(reshape) == 16:
    reshape = reshape.reshape(4, 4)
else:
    print("Length of array is not 16. So, not reshaping")

print("NumPy reshape:\n", reshape)

# Trignometric functions
print("sin(0):", np.sin(90))
print("cos(0):", np.cos(0))
print("tan(0):", np.tan(0))

#Exponential functions
print("exp(0):", np.exp(0))
print("exp(reshape):", np.exp(reshape))
print("log(2):", np.log(2))

#Logarithmic functions
print("log10(100):", np.log10(100))
print("log2(100):", np.log2(100))
print("log(100):", np.log(100))

# arithmatic operations on arrays
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print("a + b:", a + b)
print("a - b:", a - b)
print("a * b:", a * b)
print("a / b:", a / b)
print("a % b:", a % b)
print("a ** b:", a ** b)