import sys
import csv

try:
    if len(sys.argv) != 3:
        sys.exit('Please input exactly 2 command-line arguments')
    if sys.argv[1][-4:] != '.csv':
        sys.exit('Please input a file ending in the extension \'.csv\'')
    filename = sys.argv[1]
except FileNotFoundError:
    sys.exit('File could not be found')

after = []

with open(sys.argv[1]) as file:
    reader = csv.DictReader(file)
    for row in reader:
        after.append({'first':row['name'].split(',')[1].lstrip(),'last':row['name'].split(',')[0],'house':row['house']})

with open(sys.argv[2],'w') as file:
    writer = csv.DictWriter(file, fieldnames=['first','last','house'])
    writer.writeheader()
    for row in after:
        writer.writerow({'first':row['first'],'last':row['last'],'house':row['house']})





