def op(a,b,c):
    match b:
        case '+':
            return round(float(a+c),1)
        case '-':
            return round(float(a-c),1)
        case '/':
            return round(a/c,1)
        case '*':
            return round(float(a*c),1)


n = [str(i) for i in input('Expression: ').split(' ')]

x = int(n[0])
y = n[1]
z = int(n[2])

print(op(x,y,z))


