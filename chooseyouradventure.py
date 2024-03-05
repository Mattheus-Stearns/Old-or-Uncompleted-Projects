import time

time.sleep(3)

q1 = str(input('\n' * 20 + 'You wake up. Do you have Frosted Flakes, or Corn Flakes?\n\n'))
q11 = q1.lower()

#Obtaining string and making it usable.


if q11 != "corn flakes" or "frosted flakes":
	print("Break")
	exit()
elif q11 == "corn flakes":
	print("You really are healthy aren't you?")
else:
	print("Satisfying your 'needs', huh?")