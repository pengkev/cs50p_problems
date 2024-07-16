import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    try:
        begin = ''
        end = ''
        times = re.search(r'(.*) (AM|PM) to (.*) (AM|PM)',s.strip())

    ##begin
        if ':' in times.group(1):
            hour, minute = map(int, times.group(1).split(':'))
            if hour > 12 or minute > 59:
                raise ValueError
            if times.group(2) == 'PM' and hour != 12:
                hour += 12
            elif times.group(2) == 'AM' and hour == 12:
                hour = 0
            begin = f'{hour:02d}{minute:02d}'
        else:
            hour = int(times.group(1))
            if times.group(2) == 'PM' and hour != 12:
                hour += 12
            elif times.group(2) == 'AM' and hour == 12:
                hour = 0
            begin = f'{hour:02d}00'


    ##end
        if ':' in times.group(3):
            hour, minute = map(int, times.group(3).split(':'))
            if hour > 12 or minute > 59:
                raise ValueError
            if times.group(4) == 'PM' and hour != 12:
                hour += 12
            elif times.group(4) == 'AM' and hour == 12:
                hour = 0
            end = f'{hour:02d}{minute:02d}'
        else:
            hour = int(times.group(3))
            if times.group(4) == 'PM' and hour != 12:
                hour += 12
            elif times.group(4) == 'AM' and hour == 12:
                hour = 0
            end = f'{hour:02d}00'

        end = end[0:2] + ':' + end[2:4]
        begin = begin[0:2] + ':' + begin[2:4]

        return f'{begin} to {end}'
    except:
        raise ValueError

if __name__ == "__main__":
    main()
