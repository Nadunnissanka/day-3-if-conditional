name1 = input("Enter name one: ")
name2 = input("Enter name two: ")

name1 = name1.lower()
name2 = name2.lower()
combined = name1+name2

true_word = combined.count("t") + combined.count("r") + combined.count("u") + combined.count("e")
love_word = combined.count("l") + combined.count("o") + combined.count("v") + combined.count("e")

print("your love score is: "+str(true_word)+str(love_word)+"%")
fullscore_cal = str(true_word)+str(love_word)
final_fullscore = int(fullscore_cal)

if final_fullscore < 10 or final_fullscore >90:
  print(f"Your final score is: {final_fullscore}%, You go together like coke and mentos.")
elif final_fullscore > 40 and final_fullscore < 50:
  print(f"Your final score is: {final_fullscore}%, You Two are alright!!.")
else:
  print(f"Your score is {final_fullscore}")

