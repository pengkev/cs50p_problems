import re


def main():
    print(count(input("Text: ")))


def count(s):
    first = int(0)
    if s.lower()[0]+s.lower()[1] == 'um':
        first = 1
    return len(re.findall(r'\Wum\W',s.lower())) + first


if __name__ == "__main__":
    main()
