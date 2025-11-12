LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot13(text):
    result = ""
    for char in text:
        if char in LOWER_ALPHABETS:
            index = LOWER_ALPHABETS.index(char)
            result += LOWER_ALPHABETS[(index + 13) % 26]
        elif char in UPPER_ALPHABETS:
            index = UPPER_ALPHABETS.index(char)
            result += UPPER_ALPHABETS[(index + 13) % 26]
        else:
            result += char
    return result

def main():
    print("Program starting.\n")
    print("Collecting plain text rows for ciphering.")
    
    lines = []
    while True:
        row = input("Insert row(empty stops): ")
        if row == "":
            break
        lines.append(row)

    ciphered = [rot13(line) for line in lines]

    print("\n#### Ciphered text ####")
    for line in ciphered:
        print(line)

    print("\n#### Ciphered text ####")
    filename = input("Insert filename to save: ")
    if filename == "":
        print("File name not defined.")
        print("Aborting save operation.")
    else:
        f = open(filename, "w")
        for line in ciphered:
            f.write(line + "\n")
        f.close()
        print("Ciphered text saved!")

    print("Program ending.")

if __name__ == "__main__":
    main()