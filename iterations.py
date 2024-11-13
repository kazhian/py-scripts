movies = [
    "The Matrix",
    "The Matrix Reloaded",
    "The Matrix Revolutions",
    "The Matrix Resurrections",
    "The Matrix 4",
    "The Matrix 5",
    "The Matrix 6",
    "The Matrix 7"]

for movie in movies:
    print(movie)

for i in range(10):
    print(i)

integers = list(range(10))
print(integers)    

two_digit_numbers = list(range(10, 100))
print(two_digit_numbers)

even_numbers = list(range(2, 10, 2))
print(even_numbers)

odd_numbers = list(range(1, 10, 2))
print(odd_numbers)

# Comprehensions
squares = [x**2 for x in range(10)]
print(squares)