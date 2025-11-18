LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def shiftCharacter(char, alphabet):
    if char in alphabet:
        index = alphabet.index(char)
        return alphabet[(index + 13) % 26]
    return char


def rot13(text):
    result = ""
    for char in text:
        if char in LOWER_ALPHABETS:
            result += shiftCharacter(char, LOWER_ALPHABETS)
        elif char in UPPER_ALPHABETS:
            result += shiftCharacter(char, UPPER_ALPHABETS)
        else:
            result += char
    return result


def writeFile(filename, content):
    with open(filename, "w", encoding="UTF-8") as f:
        f.write(content)


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
        # Muodosta yksi merkkijono, koska writeFile odottaa stringiä
        content = "\n".join(ciphered) + "\n"
        writeFile(filename, content)
        print("Ciphered text saved!")

    print("Program ending.")


if __name__ == "__main__":
    main()