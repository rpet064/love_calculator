
#python 3
#love_calculator.py
#This app is based on a buzzfeed article about love
#This programme uses the words true love and people's
# to see how compatiable they are

count = {}
true_love_score = 0
names_true = 0
names_love = 0
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_names_lower = name1.lower()+name2.lower()
names_true += combined_names_lower.count("t")
names_true += combined_names_lower.count("r")
names_true += combined_names_lower.count("u")
names_true += combined_names_lower.count("e")
true_love_score += (names_true*10 )
names_love += combined_names_lower.count("l")
names_love += combined_names_lower.count("o")
names_love += combined_names_lower.count("v")
names_love += combined_names_lower.count("e")
true_love_score += names_love

print(f'your true love score is ***{true_love_score}***')
if true_love_score > 50:
    print("You go together like coke and mentos")
elif  40 <= true_love_score <= 50:
    print("You are alright together")
    
#answer in a loop (not my answer)

combined_names = (name1 + name2).lower()

true_score = 0
love_score = 0

for letter in set("true"):
  true_score += combined_names.count(letter)
for letter in set("love"):
  love_score += combined_names.count(letter)

total_score = int(str(true_score) + str(love_score))

if total_score < 10 or total_score > 90:
  print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
  print(f"Your score is {total_score}, you are alright together.")
else:
  print(f"Your score is {total_score}")