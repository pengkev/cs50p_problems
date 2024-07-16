def iv(s):
    w = ''
    for c in s:
        if ord(c) > 64 and ord(c)< 91:
            c = chr(ord(c) + 32)
        w += c
    return w

speech = input()
print (iv(speech))

#/workspaces/102827400/indoor/indoor.py
#indoor/indoor.py
