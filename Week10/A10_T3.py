########################################################
# Task A10_T3
# Developer Linda Salmi
# Date 2025-12-02
########################################################


import sys
from A10_TLib import readValues, displayValues, bubbleSort

def main() -> None:
    Values: list[int] = []
    Filename = ""

    print("Program starting.")

    if len(sys.argv) == 2:
        Filename = sys.argv[1]
        print(f"The filename '{Filename}' was passed via CLI.")
    else:
        Filename = input("Insert filename: ").strip()

    try:
        readValues(Filename, Values)
    except FileNotFoundError:
        print("Program ending.")
        return

    print(f"Raw '{Filename}' -> ", end="")
    displayValues(Values)

    bubbleSort(Values, True)
    print(f"Ascending '{Filename}' -> ", end="")
    displayValues(Values)

    bubbleSort(Values, False)
    print(f"Descending '{Filename}' -> ", end="")
    displayValues(Values)

    Values.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()
