def main():
    g = input('Greeting: ')
    print('$',end='')
    print(int(money(g)))

def money(s):
    if 'hello' in s.lower():
        return 0
    elif s.lower()[0] == 'h':
        return 20
    else:
        return 100

if __name__ == '__main__':
    main()
