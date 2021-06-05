size = input("Enter pizza size\n* L - Large\n* M - Medium\n* S - Small\nInput: ")
pepperoni = input("Do you want add pepperoni?(Y or N) ")
extra_cheese = input("Do you want add extra cheese?(Y or N) ")

bill = 0

if(size == "S"):
  bill = bill + 15
  if(pepperoni == "Y"):
    bill = bill + 2
  if(extra_cheese == "Y"):
    bill = bill + 1
  print(f"Your bill is: ${ bill }")
elif(size == "M"):
  bill = bill + 20
  if(pepperoni == "Y"):
    bill = bill + 3
  if(extra_cheese == "Y"):
    bill = bill + 1
  print(f"Your bill is: ${ bill }")
elif(size == "L"):
  bill = bill + 25
  if(pepperoni == "Y"):
    bill = bill + 3
  if(extra_cheese == "Y"):
    bill = bill + 1
  print(f"Your bill is: ${ bill }")
else:
  print("Invalid input!")
