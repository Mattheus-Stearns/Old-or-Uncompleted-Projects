# I thought that there was an easy way to make a search engine from scratch but it turns out that there isn't
words = ["apples", "pears", "oranges", "grapefruits", "mandarins", "limes", "nectarines", "apricots", "peaches", "plums", "bananas", "mangoes", "strawberries", "raspberries", "blueberries", "kiwifruit", "passionfruit", "watermelons", "rockmelons"]
score = 0
lenWords = len(words) - 1
database = [["" for X in range(2)] for Y in range(len(words))]

for i in range(0, lenWords):
    database[i][0] = words[i]


search = input("What would you like to search?\n")

searchCharacters = list(search)

for i in range(0, lenWords):
    score = 0
    characters = list(words[i])
    print(characters)
    for i in range(0, len(searchCharacters)):
        if searchCharacters[i] in characters:
            score += 1
    score = str(score)
    database[i][1] = score
    print(database[i][1])

print(database)
