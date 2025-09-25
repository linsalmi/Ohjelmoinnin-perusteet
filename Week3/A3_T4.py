# Extend the previous menu program by adding three more options to the menu.

# Options:

# 2. Print the name backwards
#   Your name backwards is "{NameBackwards}"
# 3. Print the first character
#   The first character in name "{Name}" is "{FirstChar}"
# 4. Show the amount of characters in the name
#   There are {NameLength} characters in the name "{Name}"

# Program starting.
print("Program starting.")
# This is a program with simple menu, where you can choose which operation the program performs.
print("This is a program with simple menu, where you can choose which operation the program performs.")
# Before the menu, please insert your name: John
name = input("Before the menu, please insert your name: ")
maara = len(name)
# Options:
print("\nOptions:")
# 1 - Print welcome message
print("1 - Print welcome message")
# 2 - Print the name backwards
print("2 - Print the name backwards")
# 3 - Print the first character
print("3 - Print the first character")
# 4 - Show the amount of characters in the name
print("4 - Show the amount of characters in the name")
# 0 - Exit
print("0 - Exit")
# Your choice: 1
valinta = int(input("Your choice: "))
# Welcome John!
if valinta == 1:
    print(f"Welcome {name}!")
elif valinta == 2:
    print(f'Your name backwards is "{name[::-1]}"')
elif valinta == 3:
    print(f'The first character in name "{name}" is "{name[0]}"')
elif valinta == 4:
    print(f'There are {maara} characters in the name "{name}"')
elif valinta == 0:
    print("Exiting...")
else:
    print("Unknown option.")
# Program ending.
print("\nProgram ending.")