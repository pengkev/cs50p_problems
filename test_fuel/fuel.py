def main():
    frac = input("Fraction: ")
    pct = convert(frac)
    print(gauge(pct))


def convert(fraction):
    x, y = fraction.split("/")
    if y == '0':
        raise ZeroDivisionError
    elif int(x)/int(y) > 1:
        raise ValueError
    return int(round(int(x)/int(y) * 100))


def gauge(percentage):
    try:
        if 0 <= percentage <= 1:
            return "E"
        elif 99 <= percentage <= 100:
            return "F"
        elif 1 < percentage < 99:
            return f"{int(percentage)}%"
        else:
            raise TypeError
    except TypeError:
        pass

if __name__ == "__main__":
    main()
