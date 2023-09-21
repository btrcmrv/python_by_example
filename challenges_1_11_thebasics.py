#001 
# Ask for the user’s first name and display the output message Hello [First Name] .
first_name=input("What is your first name? ")
print(f"Hello {first_name}.")

#002 
# Ask for the user’s first name and then ask for their surname and display the output message Hello [First Name] [Surname].
first_name=input("What is your first name? ")
last_name=input("What is your last name? ")
print(f"Hello {first_name} {last_name}.")

#003
# Write code that will display the joke “What do you call a bear with no teeth?” 
# and on the next line display the answer “A gummy bear!” 
# Try to create it using only one line of code.
print('''What do you call a bear with no teeth?
A gummy bear!''')

#004 
# Ask the user to enter two numbers. 
# Add them together and display the answer as The total is [answer].
number1=int(input("Please enter one number: "))
number2=int(input("Please enter another number: "))
addition=number1+number2
print(f"The total is {addition}.")

#005 Ask the user to enter three numbers. 
# Add together the first two numbers and then multiply this total by the third. 
# Display the answer as The answer is [answer].
number1=int(input("Please enter the first number: "))
number2=int(input("Please enter the second number: "))
number3=int(input("Please enter the third number: "))
answer=(number1+number2)*number3
print(f"The answer is {answer}.")

# 006
# Ask how many slices of pizza the user started with and ask how many slices they have eaten.
# Work out how many slices they have left and display the answer in a user- friendly format.
start_slices=int(input("How many slices of pizza you started with? "))
eaten_slices=int(input("How many slices of pizza you have eaten? "))
left_over=start_slices-eaten_slices
print(f"You have {left_over} slices of pizza left over.")

# 007
# Ask the user for their name and their age.
# Add 1 to their age and display the output [Name] next birthday you will be [new age].
name=input("What is your name? ")
age=int(input("What is your age? "))
print(f"{name} next birthday you will be {age+1}.")

# 008
# Ask for the total price of the bill, then ask how many diners there are. 
# Divide the total bill by the number of diners and show how much each person must pay.
the_bill=int(input("What is the total cost of the bill? "))
people=int(input("How many people are in the diner? "))
print(f"Each person needs to pay {the_bill/people}€.")

# 009 
# Write a program that will ask for a number of days and then will show 
# how many hours, minutes and seconds are in that number of days.
days=int(input("Please type the number of the days: "))
hours=24*days
minutes=hours*60
seconds=minutes*60
print(f"In {days} days, there are {hours} hours, {minutes} minutes, and {seconds} seconds.")


# 010 
# There are 2,204 pounds in a kilogram. 
# Ask the user to enter a weight in kilograms and convert it to pounds.
weight=int(input("Please enter a weight in kilograms: "))
print(f"{weight}kg is equal to {weight*2204} pounds")

# 011 
# ask the user to enter a number over 100 
# and then enter a number under 10 and 
# tell them how many times the smaller number goes into the larger number in a user-friendly format.
number_over=int(input("Please enter a number over 100: "))
number_under=int(input("Please enter a number under 100: "))
print(f"The smaller number goes {number_over//number_under} times into the larger number.")