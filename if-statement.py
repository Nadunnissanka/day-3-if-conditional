print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if (height >= 120):
  print("you can ride the rollercoaster!")
  age = int(input("Enter your age: "))
  if age >= 18:
    print("you have to pay $12")
  else:
    print("you have to pay $7")
else:
  print("You are too short sorry!")