import sys
import requests

def main():
    print(f'${price_get(bitcoins()):,.4f}')

def bitcoins():
    try:
        return float(sys.argv[1])
    except:
        sys.exit('Please give a floating point decimal input')

def price_get(n):
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    return (n * r.json()['bpi']['USD']['rate_float'])

if __name__ == '__main__':
    main()
