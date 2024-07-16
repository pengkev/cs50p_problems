import sys
from random import choice
from pyfiglet import Figlet

fig = Figlet()
def main():
    if len(sys.argv) == 1:
        figletize(choice(Figlet().getFonts()))
    elif (len(sys.argv) == 3) and (sys.argv[1] in ['-f','--font']) and (sys.argv[2] in Figlet().getFonts()):
        figletize(sys.argv[2])
    else:
        sys.exit('Invalid usage')

def figletize(f):
    s = input('Input: ')
    fig.setFont(font=f)
    print('Output:')
    print(fig.renderText(s))

if __name__ == '__main__':
    main()
