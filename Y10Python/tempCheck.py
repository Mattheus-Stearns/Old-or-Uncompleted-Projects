tempCheck = int(input("\nPlease input the temperature of your water.\n\n"))

if (tempCheck <= 0):
    print("\nYour Water is either frozen or on the cusp on freezing.\n")
elif (tempCheck >= 100):
    print("\nYour Water is either boiling or on the cusp of boiling.\n")
elif (tempCheck == 25):
    print("\nYour Water is room temperature.\n")
else:
    print("\nYour Water is inbetween boiling and freezing.\n")
