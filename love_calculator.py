# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

words = ['true', 'love']

combined_name_lower = (name1+name2).lower()

first_digit = 0
second_digit = 0

for letter in words[0]:
    first_digit += combined_name_lower.count(letter)

for letter in words[1]:
    second_digit += combined_name_lower.count(letter)

percent = int(str(first_digit)+str(second_digit))

if percent > 90 or percent < 10:
    print(f"Your score is {percent}, you go together like coke and mentos.")
elif 40 < percent < 50:
    print(f"Your score is {percent}, you are alright together.")
else:
    print(f"Your score is {percent}.")
