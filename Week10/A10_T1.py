########################################################
# Task A10_T1
# Developer Linda Salmi
# Date 2025-12-02
########################################################

def main():
    print("Program starting.")
    filename = input("Insert filename: ").strip()

    try:
        with open(filename, "r") as file:
            
            data = [line.strip() for line in file if line.strip()]

        
        print("# --- Vertically --- #")
        for value in data:
            print(value)
        print("# --- Vertically --- #")

        
        print("# --- Horizontally --- #")
        print(", ".join(data))
        print("# --- Horizontally --- #")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    print("Program ending.")


if __name__ == "__main__":
    main()
