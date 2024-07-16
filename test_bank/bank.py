def main():
    g = input('Greeting: ')
    print('$',end='')
    print(value(g))

def value(s):
    if 'hello' in s.lower():
        return 0
    elif len(s)>0 and s.lower()[0] == 'h':
        return 20
    else:
        return 100

if __name__ == '__main__':
    main()
