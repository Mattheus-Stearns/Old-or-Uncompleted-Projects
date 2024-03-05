import random
randomNum = []
randomMean = []
sum = 0

#To calculate the probability of a given dice roll of two dice with an interchangeable amount of faces
for i in range(1, 100):
    for i in range(1, 1000):
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        z = x + y
        randomNum.append(z)

    for i in range(0, len(randomNum)):
        sum = sum + randomNum[i];

    sum = sum / len(randomNum)

    randomMean.append(sum)

for i in range(0, len(randomMean)):

    sum = sum + randomMean[i];
    sum = sum / len(randomMean)

sum *= 100

print("{:.49f}".format(sum))
