numbers = range(1, 21)

print("Numbers:")
print(*numbers, sep='\n')

print("\nSquares:")
print(*map(lambda x: x**2, numbers), sep='\n')

print("\nEven numbers:")
print(*map(lambda x: f"{x} is even" if x % 2 == 0 else f"{x} is odd", numbers), sep='\n')