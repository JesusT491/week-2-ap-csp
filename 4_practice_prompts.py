
# ----------------------------------------
# Print Practice Exercises
# ----------------------------------------

# Print Practice #1
# Write Python code that prints the sentence: I love learning Python
print("I love learning Python")


# Print Practice #2
# Write Python code that prints the sentence: Learning with 'TOTAL Python' is super fun!
print("Learning with 'TOTAL Python' is super fun!")


# Print Practice #3
# Write Python code that prints the number 555 to the screen as a result of a mathematical expression
print(500 + 55)

##############################################################################################################
# Find 3 objects around the room and create variables from it,
# Insert those variables into an f-string sentence(look at slide 22)in repl.it

mouse = "mouse"
desk = "desk"
paper = "Paper"
print(f"{mouse} {desk} {paper}")

# Familiarize yourself with the syntax of the print() function.
# Print your name.
your_name = "Jesus and Logan"
your_age = 17
print("Jesus, Logan")
# Print today's date.
print("10/30/2025")
# Print the name of your favorite movie.
print("idk")

# Print your name and age on separate lines using a single print() function.
print(f"jesus", "17")
print(f"{your_name}\n{your_age}")
# Use f-strings to print a message like: "In 10 years, [Your Name] will be [Your Age + 10] years old."

print(f"In 10 years, {your_name} will be {your_age + 10} years old.")

###########################String Practice##################################
#syntax is the way we write code
# print("Hello World")
# name = "John"
#in other languages, this is different
# in javascript for example, you define
#variables with let or const or var
#in python, you just give your variables a
#name and then define it with a value

#challenge
# find a summary of the movie blue beetle online and create a 
# variable called blue_beetle_summary and print it it out to the screen

bbsummary = "Jaime Reyes suddenly finds himself in possession of an ancient relic of alien biotechnology called the Scarab. When the Scarab chooses Jaime to be its symbiotic host, he's bestowed with an incredible suit of armor that's capable of extraordinary and unpredictable powers, forever changing his destiny as he becomes the superhero Blue Beetle."

# print the length of the summary
print(len(bbsummary))
# upper case the entire summary
print(bbsummary.upper())
# print the summary
print(bbsummary)
# print the summary in lowercase
print(bbsummary.lower())
# replace the word blue with red
summaryreplace = bbsummary.replace("Blue", "Red")
# print the summary
print(summaryreplace)
# string index the word beetle and print it out
wordindex = bbsummary[50:56]
print(str(wordindex))
# print the last word of the summary
last_word = bbsummary.split()[-1]
print(last_word)
# print the summary in reverse
print(bbsummary[::-1])
##########################input practice#############################################
#input is when we ask the user for input/data
# Ask the user to enter their name.

# Input Practice #1
# Write Python code that allows the user to enter their answer, by making them the following question:
# What are you learning today?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).

QUESTION = input("What are you learning today?: ")
print(QUESTION)

# Input Practice #2
# Write Python code that allows the user to enter their answer, by making them the following question:
# Where are you from?
# Your code must be able to print to the screen whatever is entered by the user (use the print function).

Question_1 = input("Where are you from?: ")
print(Question_1)

# Input Practice #3
# Write Python code that displays the user's full name on the screen, by allowing them to enter their first and last name with the following instructions:
# What is your name?
# What is your surname?
# The code must be able to print the user's first and last name on the screen, separated by a space.

Question_2 = input("What is your name?: ")
Question_3 = input("What is your surname?: ")
print(Question_2 + Question_2)

# Exercise:
# Write a program that asks the user for their name and favorite color, then prints a message using both pieces of information.

Favorite_Color = input("What is your favorite color?: ")
Your_Name = input("What is your Name?: ")
print(f"your name is {Your_Name} and your favorite color is {Favorite_Color}")




