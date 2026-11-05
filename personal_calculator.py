
#Practice Problem 1: Personal Information & Simple Calculator
#------------------------------------------------------------#
# 1. Ask the user for their name.
# 2. Ask for their age.
# 3. Ask for two numbers.
# 4. Calculate the sum, subtraction, multiplication, and division of those two numbers.
# 5. Display all information in a well-formatted output using f-strings

# Expected Output Example:
# Enter your name: Rahim
# Enter your age: 22
# Enter first number: 20
# Enter second number: 10
# Hello, Rahim!
# Your age is 22.
# Addition: 30
# Subtraction: 10
# Multiplication: 200
# Division: 2.0


name = input("Enter your name: Rahim \n")
age = int(input("Enter your age: 22 \n"))
num1 = int(input("Enter first number: 20 \n"))
num2 = int(input("Enter second number: 10 \n"))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

# Display information using f-strings
print(f"\nHello, {name}!")
print(f"Your age is {age}.")
print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")


