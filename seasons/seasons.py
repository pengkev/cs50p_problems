import datetime
import sys
import inflect

p = inflect.engine()

def main():
    print(ageinminutes(birth_get(input('Date of birthday: '))).capitalize())

def birth_get(givendate):
    try:
        byear,bmonth,bday = givendate.split('-')
        return datetime.date(int(byear), int(bmonth), int(bday))
    except:
        sys.exit('Please input a valid date consisting of yyyy-mm-dd')

def ageinminutes(birthday):
    tdate = datetime.date.today()
    diff = tdate - birthday
    minutes = p.number_to_words(int(diff.total_seconds()/60), andword="")
    return str(minutes+' minutes')


if __name__ == "__main__":
    main()
