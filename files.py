# program for understanding files

# reading a file
with open('data/pi.txt', 'r') as file:
    print(file.read())

# reading line by line
with open('data/pi.txt', 'r') as file:
    for line in file:
        print(line.lstrip().rstrip())

# read file using Pathlib
from pathlib import Path
path = Path('data/pi.txt').open('r')
content = path.read()
pi_string = ''

for a_line in content.splitlines():
    pi_string += a_line.lstrip().rstrip()
print(pi_string)

# Write to a file
with open('data/temp.txt', 'w') as file:
    file.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")