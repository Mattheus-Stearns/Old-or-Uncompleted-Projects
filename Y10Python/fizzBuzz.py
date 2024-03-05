
fizzBuzz = 1

while (fizzBuzz <= 100):

    if (fizzBuzz%3 == 0 and fizzBuzz%5 != 0):
        print("Fizz")
    elif (fizzBuzz%5 == 0 and fizzBuzz%3 != 0):
        print("Buzz")
    elif (fizzBuzz%3 == 0 & fizzBuzz%5 == 0):
        print("FizzBuzz")
    else:
        print(fizzBuzz)

    fizzBuzz = fizzBuzz + 1
