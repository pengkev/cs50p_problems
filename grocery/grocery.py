def main():
    print_list((get_list()))

def check_add(item, grocery_list):
        if item.upper() not in grocery_list:
            grocery_list |= {item.upper():1}
        elif item.upper() in grocery_list:
            grocery_list[item.upper()] += 1
        return grocery_list

def get_list():
    glist = {}
    while True:
        try:
            check_add(input(),glist)
        except EOFError:
            break
        except:
            continue
    return glist

def print_list(d):
    for key,value in sorted(d.items()):
        print (value, key)

main()
