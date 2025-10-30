# open up the vscode from previous day
# create a new file called: week11_day1.py
# ----------------------------------------
# Day 2 Review Activity: My Personal Info Generator
# ----------------------------------------

print(" Welcome to the Python Review Activity!")
print("You’ll review variables, strings, numbers, and print formatting.\n")

# Step 1: Create Variables
# TODO: Replace the values below with your own info
first_name = "Jesus"
age = 17
favorite_color = "Purple"
favorite_number = 24

#  Step 2: Practice String Operations
# 1. Print your name in uppercase

print(first_name.upper())

# 2. Print how many letters are in your name

print(len(first_name))

# 3. Combine your name and favorite color into one message

print(first_name, "favorite color is", favorite_color)

#  Step 3: Math Practice
# Use arithmetic operators with your favorite number

print(age + 5)

#  Step 4: User Input Practice
# Ask the user two questions and combine answers

question1 = input("What is your favorite movie?: ")
question2 = input("What would you rate the movie out of ten?: ")

# print("My favorite movie is ", question1, "and I would rate it a", question2, "out of 10")

print(f"My favorite movie is {question1} and I would rate it a {question2} out of 10 ")


# ⚙️ Step 5: Final Challenge (combine it all)
# Use math and strings together

MathQuestion = 5 / 3
Math_Input = float(input(f"What is 5 / 3?: "))

print("My answer is".upper(), Math_Input)