import math
import svgwrite
from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle, Polygon

def drawSquare(PDwg: Drawing) -> None:
    print("Insert square")
    x = int(input("- Left edge position: "))
    y = int(input("- Top edge position: "))
    side = int(input("- Side length: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Rect(insert=(x, y), size=(side, side), fill=fill, stroke=stroke))
    return None

def drawCircle(PDwg: Drawing) -> None:
    print("Insert circle")
    cx = int(input("- Center X: "))
    cy = int(input("- Center Y: "))
    radius = int(input("- Radius: "))
    fill = input("- Fill color: ")
    stroke = input("- Stroke color: ")
    PDwg.add(Circle(center=(cx, cy), r=radius, fill=fill, stroke=stroke))
    return None

def drawHexagon(PDwg: Drawing) -> None:
    print("Insert hexagon details:")
    cx = int(input("Middle point X: "))
    cy = int(input("Middle point Y: "))
    apothem = int(input("Apothem length: "))
    fill = input("Insert fill: ")
    stroke = input("Insert stroke: ")

    r = apothem / math.cos(math.radians(30))
    points = []

    
    for angle_deg in [330, 0, 30, 150, 180, 210]:
        angle_rad = math.radians(angle_deg)
        x = round(cx + r * math.cos(angle_rad))
        y = round(cy + r * math.sin(angle_rad))
        points.append((x, y))

    PDwg.add(Polygon(points=points, fill=fill, stroke=stroke))
    return None

def saveSvg(PDwg: Drawing) -> None:
    filename = input("Insert filename: ").strip()
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ").strip().lower()
    if proceed == "y":
        PDwg.save(pretty=True, indent=2)
        print("Vector saved successfully!")
    return None

def showMenu() -> None:
    print("\nOptions:")
    print("1 - Draw square")
    print("2 - Draw circle")
    print("3 - Draw hexagon")
    print("4 - Save svg")
    print("0 - Exit")

def askChoice(valid_choices: list[int]) -> int:
    while True:
        try:
            choice = int(input("Your choice: "))
            if choice in valid_choices:
                return choice
            print(f"Invalid choice. Please select one of: {valid_choices}")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except (KeyboardInterrupt, EOFError):
            print("\nUser interrupted. Exiting...")
            return 0

def main() -> None:
    print("Program starting.")
    Dwg = svgwrite.Drawing()

    while True:
        showMenu()
        choice = askChoice([0, 1, 2, 3, 4])

        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            drawSquare(Dwg)
        elif choice == 2:
            drawCircle(Dwg)
        elif choice == 3:
            drawHexagon(Dwg)
        elif choice == 4:
            saveSvg(Dwg)

    print("\nProgram ending.")

if __name__ == "__main__":
    main()
