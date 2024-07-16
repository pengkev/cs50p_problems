#light work baby
import random

def main():
    binsearch(level())

def level():
    while True:
        try:
            n = int(input('Level: '))
            a = random.randint(1,n)
            return a
        except:
            continue

def binsearch(a):
    g = int(0)
    while g != a:
        try:
            g = int(input('Guess: '))
            if g == a:
                print('Just right!')
                break
            elif g > a:
                print('Too large!')
            elif g < a:
                print('Too small!')
        except:
            continue

if __name__ == '__main__':
    main()
