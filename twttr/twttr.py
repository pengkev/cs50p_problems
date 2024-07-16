def main():
    print('Output:',shorten(input('Input: ')))

def shorten(s):
    w = ''
    for c in s:
        if c.lower() not in ['a','e','i','o','u']:
            w += c
    return w

if __name__ == '__main__':
    main()
