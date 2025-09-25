# Create a temperature unit conversion program.
# Start the program by listing options for the user:
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Exit
# Prompt user to insert choice. 
# After the decision to convert, ask the amount of current temperature (use the floating point datatype). 
# Lastly show the converted value to the user.

# For the unit conversions, use the formula Celsius = (Fahrenheit - 32) / 1.8

# Data representation examples:

# 50.0 °F
# 10.0 °C

# Use 1 decimal precision to round the converted value.

# Example program runs

# Program starting.
print("Program starting.\n")
# Options:
print("Options:")
# 1 - Celsius to Fahrenheit
print("1 - Celsius to Fahrenheit")
# 2 - Fahrenheit to Celsius
print("2 - Fahrenheit to Celsius")
# 0 - Exit
print("0 - Exit")
# Your choice: 
valinta = int(input("Your choise: "))
# Insert the amount of Celsius: 23
# Insert the amount of Fahrenheit: 100
if valinta == 1:
    cel = float(input('Insert the amount of Celsius: '))
    print(f"{cel} °C equals to {cel * 1.8 + 32} °F")
elif valinta == 2:
    fah = float(input('Insert the amount of Fahrenheit: '))
    print(f"{fah} °F equals to {round((fah - 32) / 1.8, 1)} °C")
elif valinta == 0:
    print("Exiting...")
else:
    print("Unknown option.")
# 23.0 °C equals to 73.4 °F

# Program ending.
print("\nProgram ending.")

# Note! version 2.0.1 allows both Celsius and Celcius. The syntax in the grading tool is covered with [cs] regex pattern.