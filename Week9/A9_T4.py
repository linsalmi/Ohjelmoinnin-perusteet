########################################################
# Task A9_T4
# Developer Linda Salmi
# Date 2025-12-02
########################################################

TEMP_MIN = -273.15
TEMP_MAX = 10000

def collectCelsius() -> float:
    feed = input("Insert Celsius: ")
    try:
        celsius = float(feed)
        if celsius < TEMP_MIN or celsius > TEMP_MAX:
            raise Exception(f"{celsius} temperature out of range.")
        return celsius
    except ValueError:
        raise ValueError(f"could not convert string to float: '{feed}'")

def main() -> None:
    print("Program starting.")
    try:
        celsius = collectCelsius()
        print(f"You inserted {celsius} °C")
    except Exception as e:
        print(e)
    print("Program ending.")

if __name__ == "__main__":
    main()
