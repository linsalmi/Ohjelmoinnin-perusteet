# In this task the idea is to create a program where user can define an integer and choose the decision structure being applied to the inserted integer. 
# Certain rules must be applied to specified value tresholds and the decision structure has partial role in the end results. 
# Structure, order and operators matter, so do exactly as the task describes.

# Prompt user to insert value as an integer.
# Display menu
# option 1 - In one multi-branched decision
# option 2 - Independent if-statement decisions
# option 0 - Exit
# Prompt user to choose option
# Apply following math operations in the options 1 & 2
# One multi-branched decision structure:
# Value is 400 or more => add 44 to the existing value
# Value is 200 or more => add 22 to the existing value
# Value is 100 or more => add 11 to the existing value
# Independent if-statement decisions one after another:
# Value is 400 or more => add 44 to the existing value
# Value is 200 or more => add 22 to the existing value
# Value is 100 or more => add 11 to the existing value
# Exit: “Exiting…”
# At the end of the options 1 & 2, show the results like in the example program runs.
# Other possible output variats:

# “Unknown option.”
# Example program runs


# Program starting.
print("Program starting.")
# Testing decision structures.
print("Testing decision structures.")
# Insert an integer: 250
numero = int(input("Insert an integer: "))
# Options:
print("Options:")
# 1 - In one multi-branched decision
print("1 - In one multi-branched decision")
# 2 - In multiple independent if-statements
print("2 - In multiple independent if-statements")
# 0 - Exit
print("0 - Exit")
# Your choice: 1
valinta = int(input("Your choice: "))
if valinta == 1:
# Using one multi-branched decision structure.
    print("Using one multi-branched decision structure.")
# Result is 272
    if numero >= 400:
        print(f"Result is {numero + 44}")
    elif numero >= 200:
        print(f"Result is {numero + 22}")
    elif numero >= 100:
        print(f"Result is {numero + 11}")
elif valinta == 2:
    print("Using multiple independent if-statements structure.")
    if numero >= 400:
        numero = numero + 44
    if numero >= 200:
        numero = numero + 22
    if numero >= 100:
        numero = numero + 11
    print(f"Result is {numero}")
elif valinta == 0:
    print("Exiting...")
else:
    print("Unknown option.")
# Program ending.
print("\nProgram ending.")