import sys
from PIL import Image
from PIL import ImageOps
from os.path import splitext

try:
    if len(sys.argv) != 3:
        sys.exit('Exactly two command line arguments please')
    input = sys.argv[1]
    output = sys.argv[2]
    file1=splitext(sys.argv[1])
    file2=splitext(sys.argv[2])
    if file1[-1] != file2[-1]:
        sys.exit('Ensure the output file is in the same format as the input')
    if file1[-1] not in ['.jpg','jpeg','.png']:
        sys.exit('double check extension names')
    if file2[-1] not in ['.jpg','jpeg','.png']:
        sys.exit('double check extension names')
except FileNotFoundError:
    sys.exit('File not found try again')

with Image.open('shirt.png') as im:
    size = im.size
    shirt = im
    shirt = ImageOps.fit(shirt,size)

with Image.open(input) as im:
    person = im
    person = ImageOps.fit(person, size)

with person as im:
    person.paste(shirt,shirt)
    im.save(output)




