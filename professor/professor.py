import random

def main():
    l = get_level()
    correct = int(0)
    for i in range(10):
        attempt = int(0)
        x = generate_integer(l)
        y = generate_integer(l)
        print(f'{x} + {y} = ',end='')
        while True:
            try:
                if attempt > 2:
                    print(x+y)
                    attempt = 0
                    break
                ans = int(input())
                if ans == x + y:
                    correct += 1
                    break
                else:
                    raise ValueError
            except:
                print('EEE')
                attempt += 1
                print(f'{x} + {y} = ')
    print(f'Score: {correct}')

def get_level():
    while True:
        try:
            n = int(input('Level: '))
            if n not in [1,2,3]:
                raise ValueError
        except:
            continue
        else:
            return n

def generate_integer(level):
    if level > 2:
        return random.randint(100,999)
    elif level > 1:
        return random.randint(10,99)
    else:
        return random.randint(0,9)

if __name__ == "__main__":
    main()
