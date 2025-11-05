def askName() -> str:
    name = input("Insert name: ")
    return name

def greetUser(PName) -> None:
    print(f"Hello {PName}!")
    return None

def main() -> None:
    print("Program starting.")
    name = askName()
    greetUser(name)
    print("Program ending.")
    return None

main()