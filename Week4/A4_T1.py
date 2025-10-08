# Create a Python program which prompts user to insert two integers. 
# Use these integers together with the “for-loop” structure to create 
# behaviour like in the example program example run below.


print("Program starting.\n")
start = int(input("Insert starting value: "))
stop = int(input("Insert stopping value: "))
print("\nStarting for-loop:")
for i in range(start, stop + 1):
    print(i)
print("\nProgram ending.")

