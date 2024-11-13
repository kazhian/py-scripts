# Workbench for learning dictionaries
# https://docs.python.org/3/library/datetime.html
# https://www.w3schools.com/python/python_dictionaries.asp

xuv_500 = {
    'name': 'XUV-500',
    'type': 'SUV',
    'color': 'Blue',
    'year': 2018,
    'fuel_type': 'Petrol'
}

print(xuv_500)

# Modifying a dictionary
xuv_500['color'] = 'Red'
print("color changed :", xuv_500)

# Adding a new key-value pair
xuv_500['mileage'] = 10
print("mileage added:", xuv_500)

# Deleting a key-value pair
del xuv_500['mileage']
print("mileage deleted:", xuv_500)

# Iterating over a dictionary
for key in xuv_500:
    print(key, ":", xuv_500[key])

# get method
print(f"color: {xuv_500.get('color')}")
print(f"Reg Number: {xuv_500.get('reg_number', 'Not available')}")