import svgwrite
from svgwrite import Drawing
from template import askChoice

MAIN_MENU_OPTIONS = [
    "1 - Draw square",
    "2 - Draw circle",
    "3 - Save svg",
    "0 - Exit"
]

def drawSquare(PDwg: Drawing) -> None:
    print("Insert square")
    x = float(input("- Left edge position: "))
    y = float(input("- Top edge position: "))
    side = float(input("- Side length: "))
    fill = input("- Fill color: ").strip()
    stroke = input("- Stroke color: ").strip()
    PDwg.add(PDwg.rect(insert=(x, y), size=(side, side),
                        fill=fill, stroke=stroke))
    return None

def drawCircle(PDwg: Drawing) -> None:
    print("Insert circle")
    cx = float(input("- Center X coord: "))
    cy = float(input("- Center Y coord: "))
    r = float(input("- Radius: "))
    fill = input("- Fill color: ").strip()
    stroke = input("- Stroke color: ").strip()
    PDwg.add(PDwg.circle(center=(cx, cy), r=r, fill=fill, stroke=stroke))
    return None

def saveSvg(PDwg: Drawing) -> None:
    filename = input("Insert filename: ").strip()
    print(f'Saving file to "{filename}"')
    proceed = input("Proceed (y/n)?: ").strip().lower()
    if proceed == "y":
        PDwg.save(pretty=True, indent=2)
        print("Vector saved successfully!")
    return None

def showMenu(options: list[str]):
    print("\nOptions:")
    for option in options:
        print(option)

def main() -> None:
    print("Program starting.")
    Dwg = svgwrite.Drawing()  
    while True:
        showMenu(MAIN_MENU_OPTIONS)
        choice = askChoice([0, 1, 2, 3])
        if choice == 0:
            print("Exiting program.")
            break
        elif choice == 1:
            drawSquare(Dwg)
        elif choice == 2:
            drawCircle(Dwg)
        elif choice == 3:
            saveSvg(Dwg)
    print("\nProgram ending.")

if __name__ == "__main__":
    main()
