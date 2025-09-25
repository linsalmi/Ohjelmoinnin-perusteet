# Make Python program and implement if-statements in proper places.

# Ask user to insert two integers
# Compare the integers and then announce the greater number
# Create sum of the two integers
# Check the parity of the sum (see modulo-operator ‘%’)
# Other possible output variants:

# Integer comparison
# Integers are the same.
# First integer is greater.
# Parity check
# Sum is even.

# Example program run

# run 1 run 2 run 3

print("Program starting.")
print("Insert two integers.")
int1 = int(input("Insert first integer: "))
int2 = int(input("Insert second integer: "))
print("Comparing inserted integers.")

if int1 == int2:
    print("Integers are the same.")
if int1 > int2:
    print("First integer is greater.")
if int1 < int2:
    print("Second integer is greater.")
print("\nAdding integers together")
print(f"{int1} + {int2} = {int1+int2}\n")
print("Checking the parity of the sum...")
if (int1+int2)%2 == 0:
    print("Sum is even.")
else:
    print("Sum is odd.")
print("Program ending.")






