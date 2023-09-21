#035
# Ask the user to enter their name and then display their name three times.
name=input("What is your name? ")
for i in range(0,3):
    print(name)

#036
# Alter program 035 so that it will ask the user to enter their name and a number 
# and then display their name that number of times.
name=input("What is your name? ")
number=int(input("Type a number: "))
for i in range(0,number):
    print(name)

# 037
# Ask the user to enter their name and display each letter in their name on a separate line.
name=input("What is your name? ")
for i in name:
    print(i)

# 038
# Change program 037 to also ask for a number.
# # Display their name (one letter at a time on each line) and 
# repeat this for the number of times they entered.
name=input("What is your name? ")
number=int(input("Type a number: "))

for x in range(0,number):
    for i in name:
        print(i)


# 039
# Ask the user to enter a number between 1 and 12 and 
# then display the times table for that number.
number=int(input("Please enter a number between 1 and 12: "))

for e in range(1,13):
    answer=e*number
    print(f"{e} times {number} = {answer}")

# 040
# Ask for a number below 50 and then count down from 50 to that number, 
# making sure you show the number they entered in the output.
number=int(input("Please enter a number below 50: "))
for i in range(50,number-1,-1):
    print(i)
    
# 041
# Ask the user to enter their name and a number. 
# If the number is less than 10, then display their name that number of times; 
# otherwise display the message “Too high” three times.
name=input("What is your name? ")
number=int(input("Type a number: "))

if number<10:
    for i in range(0,number):
        print(name)
else:
    for i in range(0,3):
        print("Too high")

# 042
# Set a variable called total to 0. 
# Ask the user to enter five numbers and 
# after each input ask them if they want that number included. 
# If they do, then add the number to the total. 
# If they do not want it included, don’t add it to the total. 
# After they have entered all five numbers, display the total.
total=0

for i in range(0,5):
    number=int(input("Please enter a number: "))
    included=input("Do you want to include this number into total? [y/n]: ").lower()
    if included=="y":
        total=total+number
    else:
        print(total)
print(f"The total is {total}")

# 043
# Ask which direction the user wants to count (up or down). 
# If they select up, then ask them for the top number and then count from 1 to that number. 
# If they select down, ask them to enter a number below 20 and then count down from 20 to that number. 
# If they entered something other than up or down, display the message “I don’t understand”.
direction=input("Which direction you would like to count (up or down)? ").lower()

if direction=="up":
    ask=int(input("Enter a top number "))
    for i in range(1,ask+1):
        print(i)
elif direction=="down":
    ask=int(input("Enter a number below 20 "))
    for i in range(20,ask+1,-1):
        print(i)


# 044
# Ask how many people the user wants to invite to a party. 
# If they enter a number below 10, ask for the names and after each name display “[name] has been invited”. 
# If they enter a number which is 10 or higher, display the message “Too many people”.

guest_amount=int(input("How many people would you like to invite to a party? "))

if guest_amount<10:
    for i in range(0,guest_amount):
        names=input("What are the names? ")
        print(f"{names} has invited.")
elif guest_amount>=10:
    print("Too many people! ")