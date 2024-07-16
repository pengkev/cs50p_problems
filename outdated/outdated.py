def main():
    while True:
        try:
            s = input('Date: ')
            m = month_get(s)
            d = day_get(s)
            y = year_get(s)
        except:
            continue
        else:
            print(f'{y}-{m}-{d}')
            break

def month_get(s):
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    if '/' not in s and (s.split()[0].title().strip() in months):
        for month in months:
            if month in s.title():
                if months.index(month)>8:
                    return months.index(month)+1
                elif months.index(month)<9:
                    return '0'+ str(months.index(month)+1)
    elif '/' in s:
        if int(s.split('/')[0])<10:
            return '0'+s.split('/')[0].strip()
        elif int(s.split('/')[0])<12:
            return s.split('/')[0].strip()
        else:
            raise ValueError
    else:
        raise ValueError

def year_get(s):
    if '/' in s:
        return s.split('/')[2].strip()
    elif '/' not in s.lower():
        return s.split(',')[1].strip()
    else:
        raise ValueError

def day_get(s):
    if '/' in s:
        if  int(s.split('/')[1])<10:
            return '0'+s.split('/')[1]
        elif int(s.split('/')[1])<32:
            return +s.split('/')[1]
        else:
            raise ValueError
    elif '/' not in s:
        w = ''
        inDay = False
        for c in s:
            if c.isdigit():
                inDay = True
            if not c.isdigit() and inDay:
                break
            if inDay:
                w += c
        if int(w)<10:
            return '0'+w
        elif int(w)<32:
            return w
        else:
            raise ValueError
    else:
        raise ValueError

main()
