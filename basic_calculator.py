#Instructions:
#Basic Calculator Program
#Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
#Perform the operation based on the user's input and print the result.
#Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.

num1 = int(input("Enter the first number: " ))
num2 = int(input("Enter the second number: " ))
operator = input("Enter the mathematical operation(+-*/): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "/":
    result = num1 / num2
elif operator == "*":
    result = num1 * num2
else:
    print("Invalid") 

print(f"{num1} {operator} {num2} = {result}")
#print(f"Result: {result}")         



