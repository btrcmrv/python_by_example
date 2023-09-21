import math

#027 
# Ask the user to enter a number with lots of decimal places. 
# Multiply this number by two and display the answer.
number=float(input("Please enter a number with lots of decimal places: "))
print(number*2)

#028
# Update program 027 so that it will display the answer to two decimal places.
print(round(number*2,2))

#029
# Ask the user to enter an integer that is over 500. 
# Work out the square root of that number and display it to two decimal places.
number=int(input("Please enter an integer that is over 500: "))
print(round(math.sqrt(number),2))

#030
# Display pi (π) to five decimal places.
print(round(math.pi,5))

#031
# Ask the user to enter the radius of a circle (measurement from the centre point to the edge). 
# Work out the area of the circle (π*radius2).
radius=float(input("Please enter the radius of a circle: "))
area=math.pi*(radius**2)
print(area)


##032
# Ask for the radius and the depth of a cylinder and work out the total volume 
# (circle area*depth) rounded to three decimal places.
radius=float(input("Please enter the radius of a cylinder: "))
depth=float(input("Please enter the radius of a cylinder: "))
cylinder_volume=math.pi*(radius**2)*depth
print(f" The volume of the cylinder is: {round(cylinder_volume,3)}")

#033
# Ask the user to enter two numbers. 
# Use whole number division to divide the first number by the second 
# and also work out the remainder and display the answer in a user-friendly way 
# (e.g. if they enter 7 and 2 display “7 divided by 2 is 3 with 1 remaining”)
number1=int(input("Please enter a number: "))
number2=int(input("Please enter anothe number: "))
print(f"{number1} divided by {number2} is {number1//number2} with {number1%number2} remaining.")


#034
# Display the following message:
# 1)square:
# 2)Triangle:
# enter a number    
# If the user enters 1, 
# then it should ask them for the length of one of its sides and display the area. 
# If they select 2, 
# it should ask for the base and height of the triangle and display the area. 
# If they type in anything else, it should give them a suitable error message..
message= int(input('''
      1)Square:
      2)Triangle:
      Enter a number: '''))

if message==1:
    side=int(input("What is the side of the square? "))
    print(f"The area of the square is {side**2}.")
elif message==2:
    base=int(input("What is the base of the triangle? "))
    height=int(input("What is the height of the triangle? "))
    print(f"The area of the triangle is {(base*height)/2}.")
else:
    print("Invalid Option.")