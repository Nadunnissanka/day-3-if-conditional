height = float(input("enter your height in m: "))
weight = float(input("enter your wieght in kg: "))

bmi = round(weight / (height ** 2))
print(f"Your body mass index is: {bmi}")

if bmi >= 18.5 and bmi <= 35:
  if bmi >= 18.5 and bmi <=25:
    print("Normal Weight")
  elif bmi > 25 and bmi <= 30:
    print("overweight")
  else:
    print("obses")
elif bmi < 18.5:
  print("underwieght")
else:
  print("clinically obese")