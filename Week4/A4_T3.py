# Make Python program which prompts user to insert two integers. 
# Use these integers together with the “while-loop” structure 
# to create behaviour like in the example program run below.

print("Program starting.\n")
start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))
print("\nStarting while-loop:")
number = start
while number <= stop:
    if number == stop:
        print(number)
    else:
        print(number, end=" ")
    number += 1
print("\nProgram ending.")