def main():
    print(perorfull(getfract()))

def getfract():
    while True:
        try:
            x,y = input("Fraction: ").split('/')
            if int(x) > int(y) or (y == 0):
                raise ValueError
            return int(x)/int(y)
        except ValueError:
            pass

def perorfull(fract):
    if fract <= 0.01:
        return 'E'
    elif fract >= 0.99:
        return 'F'
    else:
        return f'{round(fract * 100)}%'

main()
