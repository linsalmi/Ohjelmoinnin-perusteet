########################################################
# Task A10_T2
# Developer Linda Salmi
# Date 2025-12-02
########################################################


import sys

def readValues(PFilename: str, PValues: list[int]) -> None:
    try:
        with open(PFilename, "r") as file:
            for line in file:
                line = line.strip()
                if line: 
                    try:
                        PValues.append(int(line))
                    except ValueError:
                        print(f"Error: Invalid integer '{line}' in file.")
                        sys.exit(1)
    except FileNotFoundError:
        print(f"Error: File '{PFilename}' not found.")
        sys.exit(1)
    return None

def sumOfValues(PValues: list[int]) -> int:
    return sum(PValues)

def productOfValues(PValues: list[int]) -> int:
    product = 1
    for num in PValues:
        product *= num
    return product

def main() -> None:
    Values: list[int] = []
    print("Program starting.")
    filename = input("Insert filename: ").strip()

    readValues(filename, Values)

    Sum = sumOfValues(Values)
    Product = productOfValues(Values)

    print("# --- Sum of numbers --- #")
    print(Sum)
    print("# --- Sum of numbers --- #")

    print("# --- Product of numbers --- #")
    print(Product)
    print("# --- Product of numbers --- #")

    Values.clear()
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()
