#Split the message into different objects in an array, determine what letters are on the even parts of the array by using a remainder function, and then make two different arrays. Then, add them together and you get the message

message = input("Please input the message you want to encrypt: ")

def split(message):
    return [char for char in message]

encrypt = split(message)
print(encrypt)

even = [a for i, a in enumerate(encrypt) if i%2!=0] 
odd = [a for i,a in enumerate(encrypt) if i%2==0]

print(even)
print(odd)

encrypt = ''.join(map(str, encrypt))
encrypt2 = even + odd

encrypt2 = ''.join(map(str, encrypt2))

print(encrypt)
print(encrypt2)

# OPTIMALLY

#message = input("Please input the message you want to encrypt: ")

#def split(message):
#    return [char for char in message]

#encrypt = split(message)

#even_Num = [a for i, a in enumerate(encrypt) if i%2!=0] 
#odd_Num = [a for i,a in enumerate(encrypt) if i%2==0]

#encrypt2 = even_Num + odd_Num

#encrypt2 = ''.join(map(str, encrypt2))

#print("Here is your encrypted message:", encrypt2)