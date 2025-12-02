########################################################
# Task A9_T3
# Developer Linda Salmi
# Date 2025-12-02
########################################################

import sys

def main() -> None:
    print("Program starting.")
    filename = input("Insert filename: ")

    try:
        with open(filename, "r", encoding="UTF-8") as f:
            print(f"## {filename} ##")
            print(f.read().strip())
            print(f"## {filename} ##")
    except FileNotFoundError:
        print(f"Couldn't read file \"{filename}\".")
        sys.exit(1)

    print("Program ending.")


if __name__ == "__main__":
    main()

