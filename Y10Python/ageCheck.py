# I am going to use the number 21 instead of 18, because it lets me set the tone of at a bar

ageCheck = int(input("\nHello, welcome to our established inn. \n\nFirst, before you drink you have to submit your age:\n\n"))

if (ageCheck >= 21):
    print("\n\nWelcome to the tavern my laddie, here you can have a fine brew.\n")
else:
    YearsUntilofAge = 21 - ageCheck
    print("\n\nI am sorry youngin, but you need to wait another", YearsUntilofAge, "years.\n")
