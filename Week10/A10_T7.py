########################################################
# Task A10_T7
# Developer Linda Salmi
# Date 2025-12-02
########################################################
#Tässä jotain aloittelua, mutta jälleen kerran liian monimutkainen.

import random
random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int):
    return None

def calculateNearbys(PMineField: list[list[int]]) -> None:
    return None

def generateMinefield(PMineField: list[list[int]], PRows: int, PCols: int, PMines: int) -> None:
    return None

def main() -> None:
    print("Program starting.")
    while True:
        print("\nOptions:")
        print("1 - Generate minesweeper board")
        print("2 - Show generated board")
        print("3 - Save board")
        print("0 - Exit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            rows = input("Insert rows: ").strip()
            cols = input("Insert columns: ").strip()
            mines = input("Insert mines: ").strip()
            print(f"Board generated with {rows} rows, {cols} columns, {mines} mines. (simulated)")

        elif choice == "2":
            print("Showing board... (simulated)")

        elif choice == "3":
            filename = input("Insert filename: ").strip()
            print(f"Board saved to {filename}. (simulated)")

        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

    print("Program ending.")

if __name__ == "__main__":
    main()
