def fibonacci(n):
    """
    Recursive function to calculate the nth Fibonacci number.
    
    Args:
        n (int): The position of the Fibonacci number to calculate.
    
    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_series(n):
    """
    Prints the Fibonacci series up to the nth number.
    
    Args:
        n (int): The number of Fibonacci numbers to print.
    """
    for i in range(1, n+1):
        print(fibonacci(i), end=" ")

# Example usage:
print_fibonacci_series(10)