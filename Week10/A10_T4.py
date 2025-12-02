########################################################
# Task A10_T4
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
                    PValues.append(int(line))
    except FileNotFoundError:
        print(f"Couldn't read file '{PFilename}'. File not found.")
        raise
    return None

def displayValues(PValues: list[int]) -> None:
    print(", ".join(str(v) for v in PValues))
    return None

def merge(PLeft: list[int], PRight: list[int], PMerge: list[int], PAsc: bool = True) -> None:
    i = j = 0
    while i < len(PLeft) and j < len(PRight):
        if (PAsc and PLeft[i] <= PRight[j]) or (not PAsc and PLeft[i] >= PRight[j]):
            PMerge.append(PLeft[i])
            i += 1
        else:
            PMerge.append(PRight[j])
            j += 1
    PMerge.extend(PLeft[i:])
    PMerge.extend(PRight[j:])
    return None

def mergeSort(PValues: list[int], PAsc: bool = True) -> None:
    if len(PValues) <= 1:
        return None
    mid = len(PValues) // 2
    left = PValues[:mid]
    right = PValues[mid:]
    mergeSort(left, PAsc)
    mergeSort(right, PAsc)
    merged = []
    merge(left, right, merged, PAsc)
    PValues.clear()
    PValues.extend(merged)
    return None

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

    mergeSort(Values, True)
    print(f"Ascending '{Filename}' -> ", end="")
    displayValues(Values)

    mergeSort(Values, False)
    print(f"Descending '{Filename}' -> ", end="")
    displayValues(Values)

    Values.clear()
    print("Program ending.")

if __name__ == "__main__":
    main()
