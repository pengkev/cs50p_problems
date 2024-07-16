import requests

def rate_rarity(inputname):
    #how unique is the name? how many others have this name
    #return a value from 0-25
    #extracting names from new york json and making dict of all names containing the name and the frequency of the name
    r = requests.get('https://data.cityofnewyork.us/api/views/25th-nujf/rows.json')

    name_and_freq = {inputname:1}
    for person in (r.json()['data']):
        if person[11].title() not in name_and_freq:
            name_and_freq.update({person[11].title():1})
        else:
            name_and_freq[person[11].title()] += 1

    #scoring the name and returning it
    sum = 0
    for key in name_and_freq:
        sum += name_and_freq[key]

    unique_score = 31 - ((name_and_freq[inputname]*100000000/sum)) ** (1/4)
    return round(unique_score)


def rate_value(name):
    #how valuable is the name? how many cultures and people have this name come from, how much information is there about it
    #return a value from 0-25
    #getting data about given name from behindthename.com (specific spellings
    r = requests.get(f'https://www.behindthename.com/api/lookup.json?name={name}&key=ke873866252&exact=yes')
    #score the name based on how long the json returned is (the longer the json the higher the score)
    value_score = round((len(str(r.json())) ** (1/2))/(1.6))
    return value_score

def rate_nicknames(name):
    #how many nicknames and alternate versions are there of this name (spelling/exact version does not matter for this)
    #the more nicknames, the higher the score - nicknames are cool
    #return a value from 0-25
    r = requests.get(f'https://www.behindthename.com/api/related.json?name={name}&usage=eng&key=ke873866252')

    #score the name based on how many nicknames there are
    try:
        if len(r.json()['names']) > 25:
            return 25
        else:
            return len(r.json()['names'])
    except KeyError:
        return 0

def rate_pronounceability(name):
    #how hard is it to pronounce and read the name?
    #see key and peele skit on a-a-ron
    #return a value from 0-25

    #similar to name length but for every vowel the name is harder to pronounce, especially the letter y
    difficulty = 0
    for c in name.lower():
        if c == 'y':
            difficulty += 6
        elif c in 'aeiou':
            difficulty += 3
        else:
            difficulty += 1

    #convert the score into something that is lower the harder it is to pronounce
    difficulty_score = 25 - round(difficulty ** (1/1.2))
    return difficulty_score

def main():
    #get a real name input
    while True:
        try:
            n = input('Give us your name, and we\'ll give it a score! ').title()
            if not n.strip():
                raise ValueError('An actual name please')
            else:
                break
        except:
            continue

    r = rate_rarity(n)
    v = rate_value(n)
    k = rate_nicknames(n)
    p = rate_pronounceability(n)

    print(f'Your rarity score is: {r}')
    print(f'Your value score is: {v}')
    print(f'Your nickname score is: {k}')
    print(f'Your pronouncability score is: {p}')
    print(f'Your overall score is: {r+v+k+p}')

if __name__ == "__main__":
    main()
