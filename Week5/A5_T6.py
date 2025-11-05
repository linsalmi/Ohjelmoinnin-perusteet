def showOptions() -> None:
    print("Options:")
    print("1 - Show count")
    print("2 - Increase count")
    print("3 - Reset count")
    print("0 - Exit")
    return None

def askChoice() -> int:
    choice = input("Your choice: ")
    if choice.isnumeric():
        return int(choice)
    else:
        return -1

def main() -> None:
    print("Program starting.")
    counter = 0
    while True:
        showOptions()
        choice = askChoice()
        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            print(f"Current count - {counter}")
        elif choice == 2:
            print("Count increased!")
            counter = counter + 1
        elif choice == 3:
            print("Cleared count!")
            counter = 0
        else:
            print("Unknown option!")
    print("\nProgram ending.")
    return None

main()