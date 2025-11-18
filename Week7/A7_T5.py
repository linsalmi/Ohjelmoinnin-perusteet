from dataclasses import dataclass

# Constants
DELIMITER = ";"
WEEKDAYS = (
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturnday", "Sunday"
)

@dataclass
class Timestamp:
    weekday: str
    hour: str
    consumption: float
    price: float

    def total_cost(self) -> float:
        return self.consumption * self.price


@dataclass
class DayUsage:
    weekday: str
    total_consumption: float = 0.0
    total_cost: float = 0.0


def readFile(filename: str, timestamps: list[Timestamp]) -> None:
    print(f'Reading file "{filename}".')
    timestamps.clear()

    try:
        with open(filename, "r", encoding="UTF-8") as f:
            next(f)  # Skip header row
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


def analyseUsage(timestamps: list[Timestamp], day_usages: list[DayUsage]) -> None:
    print("Analysing timestamps.")
    day_usages.clear()

    # Luo DayUsage-objektit jokaiselle viikonpäivälle
    for day in WEEKDAYS:
        day_usages.append(DayUsage(weekday=day))

    # Käy läpi kaikki timestampit ja lisää arvot oikealle päivälle
    for ts in timestamps:
        for day_usage in day_usages:
            if ts.weekday == day_usage.weekday:
                day_usage.total_consumption += ts.consumption
                day_usage.total_cost += ts.total_cost()


def displayResults(day_usages: list[DayUsage]) -> None:
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for day_usage in day_usages:
        print(f" - {day_usage.weekday} usage {day_usage.total_consumption:.2f} kWh, "
              f"cost {day_usage.total_cost:.2f} €")
    print("### Electricity consumption summary ###")


def main() -> None:
    print("Program starting.")

    timestamps: list[Timestamp] = []
    day_usages: list[DayUsage] = []

    filename = input("Insert filename: ").strip()

    readFile(filename, timestamps)
    if timestamps:
        analyseUsage(timestamps, day_usages)
        displayResults(day_usages)

    print("Program ending.")


if __name__ == "__main__":
    main()