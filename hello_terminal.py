#!/usr/bin/env python3

# This is a simple Python program to demonstrate basic concepts

# Print a message to the terminal
print("Hello, Terminal!")
print("This is a basic Python program to show fundamental concepts.")
print("-" * 50)  # This prints 50 dashes as a separator

# Variables
name = input("What is your name? ")  # Get user input and store it in a variable
age_string = input("How old are you? ")
age = int(age_string)  # Convert the string input to an integer

# Conditional logic (if/else)
if age >= 18:
    print(f"Hello {name}, you are an adult!")
else:
    print(f"Hello {name}, you are not yet an adult.")

# Lists
favorite_things = []  # Create an empty list
print("\nLet's add some of your favorite things to a list.")

# Loop
for i in range(3):  # This will run 3 times (0, 1, 2)
    thing = input(f"Enter favorite thing #{i+1}: ")
    favorite_things.append(thing)  # Add the input to our list

# Working with the list
print("\nYour favorite things:")
for index, item in enumerate(favorite_things):
    print(f"{index+1}. {item}")

# Simple calculation
print("\nLet's do a quick calculation.")
print(f"In 10 years, you'll be {age + 10} years old.")

# Final message
print("\nThanks for trying this program!")
print("Now you've seen basic Python concepts like:")
print("- Printing to the screen")
print("- Getting user input")
print("- Variables and type conversion")
print("- Conditional logic (if/else)")
print("- Lists and loops")
print("- String formatting")

print("\nThese are the building blocks for more complex programs like the Snake game!")

