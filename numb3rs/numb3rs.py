import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        if len(ip.split('.')) != 4:
            return False
        for num in ip.split('.'):
            if int(num)>255:
                return False
        return True
    except:
        return False

if __name__ == "__main__":
    main()
