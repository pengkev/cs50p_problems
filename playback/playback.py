def spacedot(s):
    word = ''
    for c in s:
        if c == ' ':
            word += "..."
        else:
            word += c
    return word

a = input()
print(spacedot(a))

