def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def twol(s):
    if (s[0:2]).isalpha():
        return True
    else:
        return False

def minmax(s):
    return True if 1 < len(s) < 7 else False

def numend(s):
    for c in s:
        if c.isdigit():
            break
    if c == '0':
        return False
    if s[s.find(c): -1].isdigit() and not s.isalpha():
        return True
    elif s.isalpha():
        return True
    else:
        return False

def spp(s):
    for c in s:
        if not c.isalnum():
            return False
    return True

def is_valid(s):
    if minmax(s) and twol(s) and numend(s) and spp(s):
        return True

if __name__ == '__main__':
    main()
