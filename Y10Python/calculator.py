def maths1(num1, num2):
  print(num1 + num2)

def maths2(num1, num2):
  print(num1 - num2)

def maths3(num1, num2):
  print(num1 * num2)

def maths4(num1, num2):
  print(num1 / num2)

print("Hello, welcome to your caclulator.")

num1 = int(input("What is your first number? "))
num2 = int(input("What is your second number? "))

program = int(input("What is your operation? (1 for +, 2 for -, 3 for *, 4 for /) "))

if program == 1:
  maths1(num1, num2)
elif program == 2:
  maths2(num1, num2)
elif program == 3:
  maths3(num1, num2)
elif program == 4:
  maths4(num1, num2)
else:
  print("error")