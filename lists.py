import os
os.system('cls' if os.name == 'nt' else 'clear')

def map_hetro_to_string(hetro):
    """Maps arrays to a comma separated string."""
    return ','.join(map(str, hetro))
def map_to_string(array):
    """Maps list to a comma separated string."""
    return ','.join(array)
# integer array
integers = range(1, 11)
big_list = True if len(integers) > 5 else False

# Lists
food = ['pizza', 'spaghetti', 'hotdog', 'hamburger', 'pudding']
print("given list         :", map_to_string(food))

food[0] = 'sushi'
print("food[0] = 'sushi'  :", map_to_string(food))

food.append('ice cream')
print("append('ice cream'):", map_to_string(food))

del food[0]
print("del food[0]        :", map_to_string(food))

food.insert(0, 'browny')
print("insert('browny')   :", map_to_string(food))

food.remove('ice cream')
print("remove('ice cream'):", map_to_string(food))

popped = food.pop()
print("popped             :", popped)
print("after pop()        :", map_to_string(food))

food.reverse
print("food.reverse()     :", map_to_string(food))

print("sorted(food)       :", map_to_string(sorted(food)))

food.sort(reverse=True)
print("sort(reverse=True) :", map_to_string(food))

food.sort()
print("sort()             :", map_to_string(food))

food.clear()
print("clear()            :", map_to_string(food))

hetrogenous = [1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e']
print("heterogenous       :", map_hetro_to_string(hetrogenous))

# Slicing Lists
dates = range(1, 31)
print("slicing first 5    :", map_hetro_to_string(dates[:5]))
print("slicing 10 to 20   :", map_hetro_to_string(dates[10:20]))
print("slicing 25 to end  :", map_hetro_to_string(dates[25:]))
print("slicing last 10    :", map_hetro_to_string(dates[-10:]))

# Comparing Lists
first = [1, 2, 3]
second = [2, 3, 4]

print("first == second    :", first == second)
print("first != second    :", first != second)
print("first > second     :", first > second)
print("first < second     :", first < second)
print("first >= second    :", first >= second)
print("first <= second    :", first <= second)

first.append(4)
if (first in second):
    print("first is in second")
else:
    print("first is not in second")

a = Great Learning