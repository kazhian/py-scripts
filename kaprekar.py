def largest_number(n):
    return int(''.join(sorted(str(n), reverse=True)))

def smallest_number(n):
    return int(''.join(sorted(str(n))))

def kaprekar(a):
    largest = largest_number(a)
    smallest = smallest_number(a)
    return largest, smallest, largest - smallest

def all_digits_same(n):
    return len(set(str(n))) == 1

def kaprekar_p(p):
    return p == 6174

for i in range(1000, 10000):
    if all_digits_same(i):
        continue

    attempts = 1
    current_value = i
    while True:
        largest, smallest, k = kaprekar(current_value)
        print(f"{i}. Attempt #{attempts}.  {largest}-{smallest}={k}{'*' if kaprekar_p(k) else ''}")
        if kaprekar_p(k):
            break
        attempts += 1
        current_value = k  # Update current_value to k
        if all_digits_same(current_value):  # Check if all digits are the same
            break