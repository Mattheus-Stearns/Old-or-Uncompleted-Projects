
weapons = ["shiv", "knife", "sword", "bow and arrow", "magical staff", "zombie killer 3000"]

zombieWeakness = ["zombie killer 3000"]

print("You have encoutered a zombie and you should prepare to fight.")

print("Here are your possible weapons:", weapons)

weapon = int(input("Please choose one to kill the zombie, or input one of your own. (0 or 1): "))

if weapon == 0:
  
  print("Here are your possible weapons:", weapons)

  playerChoice = int(input("Please choose one of the weapons. (0 to 6): "))

  if playerChoice == 6:
    
    print("You have beaten the zombie, and you scavage its remains. You find: +1 Magical Potion, +1 Ripped Leather Cloak, +1 Damaged Wooden Shiv")

  else: 
    print("You have chosen the wrong weapon. The zombie has resistance and tears you limb from limb. YOU DIED.")
  
elif weapon == 1:

  playerChoice = input("Please input a pointless weapon: ")

  weapons.append(playerChoice)

  weapon = 0

else:
  print("Error!")
  
if weapon == 0:
  
  print("Here are your possible weapons:", weapons)

  playerChoice = int(input("Please choose one of the weapons. (0 to 7)"))

  if playerChoice == 6:
    
    print("You have beaten the zombie, and you scavage its remains. You find: +1 Magical Potion, +1 Ripped Leather Cloak, +1 Damaged Wooden Shiv")

  else: 
    print("You have chosen the wrong weapon. The zombie has resistance and tears you limb from limb. YOU DIED.")
else:
  print("")