import sys

try:
    _ = sys.argv[1]
    if len(sys.argv) >2:
        raise IndexError
    if sys.argv[1][-3:] != '.py':
        sys.exit('Please input the name of a Python file ending in .py')
except IndexError:
    sys.exit('Please input exactly the name of the file')
except FileNotFoundError:
    sys.exit('Please input the name of a file that exists')

with open(sys.argv[1]) as file:
    lines = file.readlines()

count=0

for line in lines:
    if not(line.lstrip().startswith('#') or line.isspace()):
        count+=1

print(count)
