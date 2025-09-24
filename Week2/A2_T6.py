# Write a Python program which asks user to insert hex color. 
# In this case hex color is expected to be the 7 character representation starting with # and followed by 6 0-F characters to represent RGB colors. 
# More about hex colors at https://en.wikipedia.org/wiki/Web_colors

# Slice the amount of red, green and blue from that inserted color and display each color as shown below.

# Example program run:

# Program starting.
print("Program starting.\n")
# Insert a hex color: #FFA500
color = input("Insert a hex color: ")

# Colors
print("\nColors")
# - Red FF
print(f"- Red {color[1:3]}")
# - Green A5
print(f"- Green {color[3:5]}")
# - Blue 00
print(f"- Blue {color[-2:]}")

# Program ending.
print("\nProgram ending.")