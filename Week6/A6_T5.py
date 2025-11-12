SEPARATOR = ";"

def readValues(filename):
    values = ""
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    for i in range(len(lines)):
        number = lines[i].strip()
        values += number
        if i < len(lines) - 1:
            values += SEPARATOR
    return values


def analyseNumbers(values):
    numbers = [int(x) for x in values.split(SEPARATOR)]

    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count

    results = f"{count}{SEPARATOR}{total}{SEPARATOR}{greatest}{SEPARATOR}{average:.2f}"
    return results


def displayReport(filename, results):
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print("Count;Sum;Greatest;Average")
    print(results)
    print("\n#### Number analysis - END ####")


def main():
    print("Program starting.")
    filename = input("Insert filename: ")

    values = readValues(filename)
    results = analyseNumbers(values)
    displayReport(filename, results)

    print("Program ending.")


if __name__ == "__main__":
    main()