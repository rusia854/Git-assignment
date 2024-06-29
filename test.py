print("Hello, World!")  # Print a message to the console

# Ask the user for their name
name = input("What is your name? ")

# Print a personalized greeting
print("Hello, " + name + "!")

# Ask the user for their age
age = int(input("How old are you? "))

# Print a message based on the user's age
if age < 18:
    print("You're still young!")
else:
    print("You're all grown up!")

# Calculate the user's birth year
birth_year = 2023 - age
print("You were born in", birth_year)