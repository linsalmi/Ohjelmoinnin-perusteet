from dataclasses import dataclass

DELIMITER = ";"

@dataclass
class Timestamp:
    weekday: str
    hour: str
    consumption: float
    price: float

    def total_cost(self) -> float:
        return self.consumption * self.price

    def formatted_hour(self) -> str:
        return f"{self.hour}:00"


def readFile(filename: str, timestamps: list[Timestamp]) -> None:
    print(f'Reading file "{filename}".')
    timestamps.clear()

    try:
        with open(filename, "r", encoding="UTF-8") as f:
            next(f)
            for line in f:
                if line.strip():
                    columns = line.strip().split(DELIMITER)
                    ts = Timestamp(
                        weekday=columns[0],
                        hour=columns[1],
                        consumption=float(columns[2]),
                        price=float(columns[3])
                    )
                    timestamps.append(ts)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")


def displayUsage(timestamps: list[Timestamp]) -> None:
    print("Electricity usage:")
    for ts in timestamps:
        print(f" - {ts.weekday} {ts.formatted_hour()}, price {ts.price:.2f}, "
              f"consumption {ts.consumption:.2f} kWh, total {ts.total_cost():.2f} €")


def main() -> None:
    print("Program starting.")

    timestamps: list[Timestamp] = []

    filename = input("Insert filename: ").strip()

    readFile(filename, timestamps)

    if timestamps:
        displayUsage(timestamps)

    print("Program ending.")


if __name__ == "__main__":
    main()