# Create menu program with submenus. 
# Mainly for unit conversions. 
# Use the values from the following table for unit conversions 
# https://www.isa.org/getmedia/192f7bda-c77c-480a-8925-1a39787ed098/CCST-Conversions-document.pdf

# Menu options:

# 1. Length
#   1. Meters to kilometers
#   2. Kilometers to meters
# 2. Weight
#   1. Grams to pounds
#   2. Pounds to grams
# 3. Exit
#   1. “Exiting...”

# Handle all the data in floating point datatype. 
# Remember to round every value in 1 digit precision right before displaying.

# Other possible prints:

# “Unknown option.”

# Example run - weight conversion 1



print("Program starting.")
print("Welcome to the unit converter program!")
print("Follow the menu instructions below.")

print("\nOptions:")
print("1 - Length")
print("2 - Weight")
print("0 - Exit")
valinta = int(input("Your choice: "))

if valinta == 1:
    print("\nLength options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")

    valinta1 = int(input("Your choice: "))
    if valinta1 == 1:
        metrit = float(input("Insert meters: "))
        kilsat = metrit / 1000
        print(f"{round(metrit, 1)} m is {round(kilsat, 1)} km")
        print("\nProgram ending.")
    elif valinta1 == 2:
        km = float(input("Insert kilometers: "))
        metr = km * 1000
        print(f"{round(km, 1)} km is {round(metr, 1)} m")
        print("\nProgram ending.")
    elif valinta1 == 0:
        print("Exiting...")
        print("\nProgram ending.")
    else:
        print("Unknown option.")
        print("\nProgram ending.")

elif valinta == 2:
    print("\nWeight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    valinta2 = int(input("Your choice: "))
    if valinta2 == 1:
        gram = float(input("Insert grams: "))
        pounds = gram * 0.00220462
        print(f"{round(gram, 1)} g is {round(pounds, 1)} lb")
        print("\nProgram ending.")
    elif valinta2 == 2:
        pounds = float(input("Insert pounds: "))
        gram = pounds / 0.00220462
        print(f"{round(pounds, 1)} lb is {round(gram, 1)} g")
        print("\nProgram ending.")
    elif valinta2 == 0:
        print("Exiting...")
        print("\nProgram ending.")
    else:
        print("Unknown option.")
        print("\nProgram ending.")

elif valinta == 0:
    print("Exiting...")
    print("\nProgram ending.")

else:
    print("Unknown option.")