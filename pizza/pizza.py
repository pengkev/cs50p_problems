import sys
import csv
from tabulate import tabulate

try:
    if len(sys.argv) >2:
        sys.exit('Too many arguments')
    elif len(sys.argv) < 2:
        sys.exit('Too little arguments')
    elif sys.argv[1][-4:] != '.csv':
        sys.exit('File extension must end in .csv')
except FileNotFoundError:
    sys.exit('Please input a valid file name')

kindapizza = (sys.argv[1].split('.')[0].title() + ' Pizza')
food_items = []

with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        food_items.append({kindapizza:row[kindapizza], 'Small':row['Small'], 'Large':row['Large']})

print(tabulate(food_items,headers = 'keys',tablefmt="grid"))
