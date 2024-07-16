def main(t):
#call convert and check meal time
    if 7.00<=t<=8.00:
        print('breakfast time')
    elif 12.00<=t<=13.00:
        print('lunch time')
    elif 18.00<=t<=19.00:
        print('dinner time')


def convert(time):
#convert time to float
    h,m = time.split(':')
    m = float(m)
    m = m/60
    return float(h) + m

if __name__ == "__main__":
    main(convert(input('What time is it? ')))


