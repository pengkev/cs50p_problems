def main():
    c = float(0)
    while True:
        try:
            c += cost(input("Item: \n"))
            print(f"Total: ${c:.2f}\n")
        except EOFError:
            break
        except:
            continue


def cost(s):
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    if s.title() in menu:
        return menu[s.title()]
    else:
        raise KeyError
main()
