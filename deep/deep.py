def ans(s):
    if (s.strip(' ')).isdigit() == True and float(s) == 42:
        return True
    elif s.lower() ==  'forty two' or s.lower() == 'forty-two':
        return True
    else:
        return False

s = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')
if ans(s) == True:
    print('Yes')
else:
    print('No')
