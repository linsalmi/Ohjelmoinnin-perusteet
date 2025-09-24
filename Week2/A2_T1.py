# Make a Python program, which prompts the user name and two floating numbers. 
# Multiply the inserted numbers to get product. Round the product in two decimal precision. 
# Complete the program output as shown below.

#Example program run:

#Program starting.
print("Program starting.")
#What is your name: John
Name = input("What is you name: ")
#Enter a floating point number: 3.1
FirstNumber = input("Enter a floating point number: ")
FirstNumber = float(FirstNumber)
#Enter second floating point number: 5.3
SecondNumber = input("Enter second floating point number: ")
SecondNumber = float(SecondNumber)
#John you gave numbers 3.1 and 5.3
print(f"{Name} you gave numbers {FirstNumber} and {SecondNumber}")
#Multiplying first and second number will result in product 16.43
Multi = FirstNumber * SecondNumber
print(f"Multiplying first and second number will result in product {round(Multi,2)}")
#Program ending.
print("Program ending.")