#012
# Ask for two numbers. 
# If the first one is larger than the second, display the second number first 
# and then the first number, otherwise show the first number first and then the second.
number1=int(input("Please enter a number: "))
number2=int(input("Please enter another number: "))

if number1>number2:
    print(number2, number1)
else:
    print(number1, number2)

#013
# Ask the user to enter a number that is under 20. 
# If they enter a number that is 20 or more, display the message “Too high”, 
# otherwise display “Thank you”.
number=int(input("Please enter a number that is less than 20: "))
if number>=20:
    print("Too High!")
else:
    print("Thank you.")

#014
#Ask the user to enter a number between 10 and 20 (inclusive). 
# If they enter a number within this range, display the message “Thank you”, 
# otherwise display the message “Incorrect answer”.
num=int(input("Please enter a number between 10 and 20: "))
if 10<=num<=20:
    print("Thank you!")
else:
    print("Incorrect answer!")

#015
#Ask the user to enter their favourite colour. 
# If they enter “red”, “RED” or “Red” display the message “I like red too”, 
# otherwise display the message “I don’t like [colour], I prefer red”.
fav_colour=input("What is your favourite colour? ").lower()

if fav_colour=="red":
    print("I like red too")
else:
    print(f"I don't like {fav_colour}, I prefer red")

#016
#Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case they type it in. 
# If they answer “yes”, ask if it is windy. If they answer “yes” to this second question, 
# display the answer “It is too windy for an umbrella”, 
# otherwise display the message “Take an umbrella”. 
# If they did not answer yes to the first question, display the answer “Enjoy your day”.
rain=input("Is it raining?[Y/N] ").lower()

if rain=="y":
    windy=input("Is it windy?[Y/N] ").lower()
    if windy=="y":
        print("It is too windy for an umbrella.")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy your day.")


#017
#Ask the user’s age. 
# If they are 18 or over, display the message “You can vote”, 
# if they are aged 17, display the message “You can learn to drive”, 
# if they are 16, display the message “You can buy a lottery ticket”, 
# if they are under 16, display the message “You can go Trick- or-Treating”.
age=int(input("What is your age? "))

if age>=18:
    print("You can vote.")
elif age==17:
    print("You can learn to drive.")
elif age==16:
    print("You can buy a lottery ticket")
else:
    print("You can go Trick- or-Treating")
    

#018
#Ask the user to enter a number. 
# If it is under 10, display the message “Too low”, 
# if their number is between 10 and 20, display “Correct”, 
# otherwise display “Too high”.
number=int(input("Please enter a number: "))
if number<10:
    print("Too low.")
elif 10<=number<=20:
    print("Correct.")
else:
    print("Too high")
    
#019
#Ask the user to enter 1, 2 or 3. 
# If they enter a 1, display the message “Thank you”, 
# if they enter a 2, display “Well done”, 
# if they enter a 3, display “Correct”. 
# If they enter anything else, display “Error message”.
number=int(input("Please enter either 1, 2 or 3: "))

if number==1:
    print("Thank you.")
elif number==2:
    print("Well done.")
elif number==3:
    print("Correct.")
else:
    print("Error message.")