########################################################
# Task A9_T5
# Developer Linda Salmi
# Date 2025-12-02
########################################################


def askIntByte(PPrompt: str) -> int:
    Feed = input(PPrompt)
    try:
        val_float = float(Feed)
        if not val_float.is_integer():
            print(f'"{Feed}" is non-numeric value.')
            raise ValueError("Not an integer")
        val_int = int(val_float)

        if val_int < 0 or val_int > 255:
            print(f'Value "{Feed}" is out of the range 0-255.')
            raise ValueError("Out of range")
        return val_int
    except ValueError:
        if not Feed.replace('.', '', 1).isdigit():
            print(f'"{Feed}" is non-numeric value.')
        raise

def createHex(PRed: int, PGreen: int, PBlue: int) -> str:
    return f"#{PRed:02x}{PGreen:02x}{PBlue:02x}"

def main():
    print("Program starting.")
    try:
        red = askIntByte("Insert red: ")
        green = askIntByte("Insert green: ")
        blue = askIntByte("Insert blue: ")

        hex_color = createHex(red, green, blue)

        print("RGB Details:")
        print(f"- Red {red}")
        print(f"- Green {green}")
        print(f"- Blue {blue}")
        print(f"- Hex {hex_color}")
        print(f"- R-byte(base-2): {red:08b}")
        print(f"- G-byte(base-2): {green:08b}")
        print(f"- B-byte(base-2): {blue:08b}")

    except Exception:
        print("Couldn't perform the designed task due to the invalid input values.")
    print("Program ending.")

if __name__ == "__main__":
    main()
