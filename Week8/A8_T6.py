
from svgwrite import Drawing
from svgwrite.shapes import Rect, Circle

def drawSquare(PDwg: Drawing, left, top, sideLength, color, strokeColor) -> None:
    PDwg.add(Rect(insert=(left, top), size=(sideLength, sideLength),
                  fill=color, stroke=strokeColor))
    return None

def drawCircle(PDwg: Drawing, centerX, centerY, radius, color, stroke) -> None:
    PDwg.add(Circle(center=(centerX, centerY), r=radius,
                    fill=color, stroke=stroke))
    return None

def saveSvg(PDwg: Drawing, file) -> None:
    PDwg.saveas(file)
    return None

def main() -> None:
    print("Program starting.")
    Dwg = Drawing()
    while True:
        print("Options:")
        print("1 - Draw square")
        print("2 - Draw circle")
        print("3 - Save svg")
        print("0 - Exit")
        choice = input("Your choice: ").strip()

        if choice == "1":
            print("Insert square")
            left = int(input("- Left edge position: "))
            top = int(input("- Top edge position: "))
            side = int(input("- Side length: "))
            fill = input("- Fill color: ")
            stroke = input("- Stroke color: ")
            drawSquare(Dwg, left, top, side, fill, stroke)

        elif choice == "2":
            print("Insert circle")
            cx = int(input("- Center X coord: "))
            cy = int(input("- Center Y coord: "))
            r = int(input("- Radius: "))
            fill = input("- Fill color: ")
            stroke = input("- Stroke color: ")
            drawCircle(Dwg, cx, cy, r, fill, stroke)

        elif choice == "3":
            filename = input("Insert filename: ").strip()
            print(f"Saving file to \"{filename}\"")
            confirm = input("Proceed (y/n)?: ").strip().lower()
            if confirm == "y":
                saveSvg(Dwg, filename)
                print("Vector saved successfully!")
            else:
                print("Save cancelled.")

        elif choice == "0":
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")
    print("Program ending.")

if __name__ == "__main__":
    main()
