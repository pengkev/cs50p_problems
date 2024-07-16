def convert(s):
    t=s.replace(':)','🙂')
    u=t.replace(':(','🙁')
    return u

def main(t):
    print(convert(t))

main(input())

