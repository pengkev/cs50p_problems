import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if 'iframe' not in s:
        return None
    html = s
    link = re.search('src=(?:"(.*)")',html)
    if url := re.search(r'(?:https|http)://(?:www\.)?youtube\.com/embed/(.+)',link.group(1)):
        return 'https://youtu.be/' + url.group(1)
    else:
        return None


if __name__ == "__main__":
    main()
