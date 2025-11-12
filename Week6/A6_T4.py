def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    filename = input("Insert filename to read: ")
    print(f'Reading names from "{filename}".')

    file = open(filename, "r")
    names = []
    for line in file:
        name = line.strip()
        if name != "":
            names.append(name)
    file.close()

    print("Analysing names...")

    
    count = len(names)
    shortest = len(min(names, key=len)) if count > 0 else 0
    longest = len(max(names, key=len)) if count > 0 else 0
    avg_length = sum(len(name) for name in names) / count if count > 0 else 0

    print("Analysis complete!")
    print("#### REPORT BEGIN ####")
    print(f"Name count - {count}")
    print(f"Shortest name - {shortest} chars")
    print(f"Longest name - {longest} chars")
    print(f"Average name - {avg_length:.2f} chars")
    print("#### REPORT END ####")

    print("Program ending.")
    return None



if __name__ == "__main__":
    main()