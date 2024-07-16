def coin(s):
    match int(s):
        case 5:
            return 5
        case 10:
            return 10
        case 25:
            return 25
        case _:
            return 0

def main():
    p = int(0)
    while p < 50:
        print('Amount Due:', 50 - p)
        p += coin(input('Insert Coin: '))
    print('Change Owed:', p - 50)

main()
