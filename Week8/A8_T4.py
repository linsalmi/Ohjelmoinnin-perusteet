import ts_lib as t1
from template import askChoice, showMenu

options = [
    "1 - Calculate amount of timestamps during year",
    "2 - Calculate amount of timestamps during month",
    "3 - Calculate amount of timestamps during weekday",
    "0 - Exit"
]

def processChoice(choice: int, timestamps):
    if choice == 0:
        print("Exiting program.")
        return False

    elif choice == 1:
        try:
            year = int(input("Insert year: "))
            count = t1.calculateYears(year, timestamps)
            print(f"Amount of timestamps during year '{year}' is {count}\n")
        except ValueError:
            print("Invalid input. Please insert a valid year.")
        except (KeyboardInterrupt, EOFError):
            print("User interrupted. Cancelling.")
            return False

    elif choice == 2:
        try:
            month = input("Insert month: ").strip()
            if month.capitalize() not in t1.MONTHS:
                print("Invalid month. Please insert a valid month name.")
                return True
            count = t1.calculateMonths(month, timestamps)
            print(f"Amount of timestamps during month '{month}' is {count}\n")
        except (KeyboardInterrupt, EOFError):
            print("User interrupted. Cancelling.")
            return False

    elif choice == 3:
        try:
            weekday = input("Insert weekday: ").strip()
            if weekday.capitalize() not in t1.WEEKDAYS:
                print("Invalid weekday. Please insert a valid weekday name.")
                return True
            count = t1.calculateWeekdays(weekday, timestamps)
            print(f"Amount of timestamps during weekday '{weekday}' is {count}\n")
        except (KeyboardInterrupt, EOFError):
            print("User interrupted. Cancelling.")
            return False

    return True

def main():
    print("Program starting.")

    filename = input("Insert filename: ").strip()
    timestamps = t1.readTimestamps(filename)

    while True:
        showMenu(options)
        choice = askChoice([0, 1, 2, 3])
        if not processChoice(choice, timestamps):
            break

    print("Program ending.")

if __name__ == "__main__":
    main()
