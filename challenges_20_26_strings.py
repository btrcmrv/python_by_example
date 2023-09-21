#020
#Ask the user to enter their first name and then display the length of their name.
name=input("Please enter your first name: ")
print(len(name))

#021
# Ask the user to enter their first name and then ask them to enter their surname. 
# Join them together with a space between and display the name and the length of whole name.
name=input("Please enter your first name: ")
last_name=input("Please enter your last name: ")

print(name+ " "+ last_name)
print(len(name+last_name))

#022
#Ask the user to enter their first name and surname in lower case. 
# Change the case to title case and join them together. Display the finished result.
name=input("Please enter your first name in lower case: ").title()
last_name=input("Please enter your last name in lower case: ").title()
print(name+" "+last_name)

#023
#Ask the user to type in the first line of a nursery rhyme and 
# display the length of the string. 
# Ask for a starting number and an ending number and 
# then display just that section of the text.
rhyme=input("Please type in the first line of a nursery rhyme: ")
print(len(rhyme))
start_number=int(input("Please enter a starting number: "))
end_number=int(input("Please enter an ending number: "))
print(rhyme[start_number:end_number])

#024
#Ask the user to type in any word and display it in upper case.
word=input("Please enter a word: ").upper()
print(word)

#025
#Ask the user to enter their first name. 
# If the length of their first name is under five characters, 
# ask them to enter their surname and join them together (without a space) 
# and display the name in upper case. 
# If the length of the first name is five or more characters, 
# display their first name in lower case.
name=input("Please enter your first name: ")
if len(name)<5:
    last_name=input("Please enter your last name: ")
    print(name.upper()+last_name)
else:
    print(name.lower())

#026
# Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an “ay”. 
# If a word begins with a vowel you just add “way” to the end. 
# For example, pig becomes igpay, banana becomes ananabay,and aadvark becomes aadvarkway. 
# Create a program that will ask the user to enter a word and change it into Pig Latin. 
# Make sure the new word is displayed in lower case.
word=input("Please enter a word: ").lower()

if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]== "u":
    print(word+"way")
else:
    print(word[1:len(word)]+word[0]+"ay")