import random

#052
#Display a random integer between 1 and 100 inclusive.
num=random.randint(1,100)
print(num)

#053
#Display a random fruit from a list of five fruits.
fruits=random.choice(["apple","orange","strawberry","pear","watermelon"])
print(fruits)

#054
#Randomly choose either heads or tails (“h” or “t”). 
# Ask the user to make their choice. 
# If their choice is the same as the randomly selected value, 
# display the message “You win”, otherwise display “Bad luck”. 
# At the end, tell the user if the computer selected heads or tails.
random_coin=random.choice(["h","t"])
user_choice=input("What is your coice [h/t]? ")

if user_choice==random_coin:
    print("You win!")
else:
    print("Bad luck!")

print(f"Computer selected {random_coin}.")
    
#055
#Randomly choose a number between 1 and 5. 
# Ask the user to pick a number. 
# If they guess correctly, display the message “Well done”, 
# otherwise tell them if they are too high or too low and 
# ask them to pick a second number. 
# If they guess correctly on their second guess, 
# display “Correct”, otherwise display “You lose”.
random_number=random.randint(1,5)
ask=int(input("Guess a number: "))

if ask==random_number:
    print("Well done!")
elif ask>random_number:
    print("Too high!")
    new=int(input("Pick a second one: "))
    if new==random_number:
        print("Correct!")
    else:
        print("You lose!")
elif ask<random_number:
    print("Too low!")
    new=int(input("Pick a second one: "))
    if new==random_number:
        print("Correct!")
    else:
        print("You lose!")
        
#056
# Randomly pick a whole number between 1 and 10. 
# Ask the user to enter a number and 
# keep entering numbers until they enter the number that was randomly picked.
random_number=random.randint(1,10)
user_guess=int(input("Guess a number: "))

while random_number!=user_guess:
    user_guess=int(input("Guess a number: "))
    
#057
# Update program 056 so that it tells the user 
# if they are too high or too low before they pick again.
random_number=random.randint(1,10)
user_guess=int(input("Guess a number: "))

while random_number!=user_guess:
    user_guess=int(input("Guess a number: "))
    if user_guess>random_number:
        print("Too high")
    elif user_guess<random_number:
        print("Too low")


#058
#Make a maths quiz that asks five questions 
# by randomly generating two whole numbers to make the question 
# (e.g. [num1] + [num2]).
# Ask the user to enter the answer. 
# If they get it right add a point to their score. 
# At the end of the quiz, tell them how many they got correct 
# out of five.
score=0
for i in range(1,6):
    num1=random.randint(1,100)
    num2=random.randint(1,100)
    answer=num1+num2
    ask=int(input(f"First number is {num1}, second number is {num2}. What is {num1}+{num2}= "))
    if answer==ask:
        score=score+1
    else:
        score
print(f"You scored {score} out of 5.")


#059
#Display five colours and ask the user to pick one. 
# If they pick the same as the program has chosen, say “Well done”, 
# otherwise display a witty answer which involves the correct colour, 
# e.g. “I bet you are GREEN with envy” or 
# “You are probably feeling BLUE right now”. 
# Ask them to guess again; if they have still not got it right, 
# keep giving them the same clue and 
# ask the user to enter a colour until they guess it correctly.

colours=random.choice(["red","blue","green","black","white"])
print(colours)
ask=True

while ask==True:
    user_pick=input("Pick a colour (red, blue, green, black, white) : ").lower()
    if user_pick==colours:
        print("Well done!")
        ask=False
    else:
        if user_pick=="red":
            print("Red? Really? Pretty boring...")
        elif user_pick=="blue":
            print("Blah, you are probably feeling BLUE right now.")
        elif user_pick=="green":
            print("I bet you are GREEN with envy")
        elif user_pick=="black":
            print("The weather is not that black.")
        elif user_pick=="white":
            print("Your answer is blank as white.")

