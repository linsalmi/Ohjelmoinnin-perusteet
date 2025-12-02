########################################################
# Task A10_T5
# Developer Linda Salmi
# Date 2025-12-02
########################################################


def recursiveFactorial(PNum: int) -> int:
    if PNum <= 1:
        return 1
    return PNum * recursiveFactorial(PNum - 1)

def main() -> None:
    print("Program starting.")
    try:
        num = int(input("Insert factorial: ").strip())
    except ValueError:
        print("Invalid input.")
        print("Program ending.")
        return

    print(f"Factorial {num}!")
    if num > 0:
        sequence = "*".join(str(i) for i in range(1, num + 1))
    else:
        sequence = "1"
    result = recursiveFactorial(num)
    print(f"{sequence} = {result}")

    print("Program ending.")

if __name__ == "__main__":
    main()
