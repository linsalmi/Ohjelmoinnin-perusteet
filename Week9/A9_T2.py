########################################################
# Task A9_T2
# Developer Linda Salmi
# Date 2025-12-02
########################################################



import sys

def main() -> None:
    print("Program starting.")
    try:
        code_str = input("Insert exit code(0-255): ")
        code = int(code_str)

        if code < 0 or code > 255:
            print("Invalid exit code! Must be between 0 and 255.")
            sys.exit(1)

        if code == 0:
            print("Clean exit")
        else:
            print("Error code")

        sys.exit(code)

    except ValueError:
        print(f"Error! '{code_str}' couldn't be converted to integer.")
        sys.exit(1)


if __name__ == "__main__":
    main()

