# testproject.py

# Ask for name and age
name = input("What's your name? ")
age = int(input("How old are you? "))

# Calculate future age
future_age = age + 10

# Display message
with open("result.txt", "a") as file:
    file.write(f"Hello, {name}! In 10 years you will be {future_age} years old.\n")

