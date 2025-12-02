
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

def displayValues(PValues: list[int]) -> None:
    print(", ".join(str(v) for v in PValues))

def bubbleSort(PValues: list[int], PAsc: bool = True) -> None:
    n = len(PValues)
    for i in range(n):
        for j in range(0, n - i - 1):
            if PAsc:
                if PValues[j] > PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
            else:
                if PValues[j] < PValues[j + 1]:
                    PValues[j], PValues[j + 1] = PValues[j + 1], PValues[j]
