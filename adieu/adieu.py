import inflect

def list_get():
    p = inflect.engine()
    l = []
    while True:
        try:
            l.append(input('Name: '))
        except EOFError:
            print('\n'+'Adieu, adieu, to '+p.join(l))
            break
        except:
            continue

if __name__ == '__main__':
    list_get()

