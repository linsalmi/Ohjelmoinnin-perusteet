SEPARATOR = ";"


def readValues(filename):
    values = ""
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    for i in range(len(lines)):
        number = lines[i].strip()  # Poistaa rivinvaihdon
        values += number
        if i < len(lines) - 1:
            values += SEPARATOR
    return values


def analyseValues(values):
    numbers = [int(x) for x in values.split(SEPARATOR)]

    count = len(numbers)
    total = sum(numbers)
    greatest = max(numbers)
    average = total / count

    header = "Count;Sum;Greatest;Average"
    data = f"{count}{SEPARATOR}{total}{SEPARATOR}{greatest}{SEPARATOR}{average:.2f}"
    return f"{header}\n{data}\n"


def displayReport(filename, results):
    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print(results)
    print("#### Number analysis - END ####")


def main():
    print("Program starting.")
    filename = input("Insert filename: ")

    values = readValues(filename)
    results = analyseValues(values)
    displayReport(filename, results)

    print("Program ending.")


if __name__ == "__main__":
    main()
