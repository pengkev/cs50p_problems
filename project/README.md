# Name Rater
### Video Demo: https://youtu.be/kZegCcr__X0
### Description:

This project is inspired by my own given name "Kevin", the typical ongoing stereotype of people named Kevin, and an ongoing trend on Instagram with a list of names posted on many reels consisting of "If name mentioned,  ___ owes you bubble tea" and then going on to display an image of an extensively long list of names. This sparks the question of how valuable a name is, and while this is largely a very intangible and subjective view, I attempted in a half-jokingly sort-of way to create a program that successfully scores inputted names.

There are many factors that go into the quality of a name. The 4 that I chose to focus on were rarity, value, nicknamability, and pronouncibilty. For each of these factors, I created a unique function to assess and assign a value for an inputted name.

The first function, rate_rarity, determines the uniqueness of a name by analyzing its frequency in the New York public baby names database. The function compiles a dictionary of unique names and their frequencies, then by checking the frequency of the name in that set, the name is scored based on how uncommon it is.

The second function, rate_value, uses the API of the website behindthename.com under a free account, and then gets a json file returned from behindthename.com. The json file has the usage details including various origins and languages the name may have a background in, as well as gender. I simplified this into just scoring based on how long the json was, because it doesn't really matter the content of the json so much as the length, and also tuning it so the score would be between 0 and 25.

The third function, rate_nicknames, also uses the behindthename.com API under the same account. It returns a json file with a list of known nicknames for a given name, and I also pass into the request an optional parameter that lets alternate spellings of names be considered the same, as I did not consider this to be significant when determining nicknames. I did however think it necessary for the rate_value function, because the rate_value function is based on the return of the json which would vary in length depending on the specific origin or spelling of a specific name.

Finally, the fourth function, rate_pronounceability, was somewhat hard to approach. After considering that many people from many backgrounds may find certain things easier to prounounce and harder to pronounce, I decided to start with the length of the name, as long names tend to be harder to read and thus pronounce. From there, I decided that more vowels implied more syllables which implied a longer name, in terms of speaking aloud. Then I thought that the specific letter 'Y' is often hard to distinguish the sound of. The end result function is simple and primitive, but somewhat effective.

All the rating functions are then used in the main() function, where a name is taken from the user using input(). The name is then passed through each rating function and stored in a variable(so the rating functions only have to be run once per name), and then the final score is printed as well as a breakdown of how well in each metric the name scored. I have yet to determine the name with the highest score.

Resources:

https://www.reddit.com/r/namenerds/

https://www.behindthename.com/api/

https://data.cityofnewyork.us/api/views/25th-nujf/rows.json
