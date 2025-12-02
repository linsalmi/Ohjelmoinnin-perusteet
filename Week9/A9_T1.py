########################################################
# Task A9_T1
# Developer Linda Salmi
# Date 2025-12-02
########################################################


def main() -> None:
    print("Program starting.\n")
    total = 0.0

    while True:
        try:
            value_str = input("Insert a floating-point value (0 to stop): ")
            value = float(value_str)

            if value == 0:
                break

            total += value

        except ValueError:
            print(f"Error! '{value_str}' couldn't be converted to float.")

    print(f"\nFinal sum is {total:.2f}")
    print("Program ending.")


if __name__ == "__main__":
    main()
