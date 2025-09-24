# Make Python program, which prompts user to insert two words. 
# Print the length of each word and then compound them together. 
# Put single quotes around the compound word.

# Example program run:

# Program starting.
print("Program starting.")
# Insert first word: fire
FirstWord = input("Insert first word: ")
# Insert second word: fighter
SecondWord = input("Insert second word: ")
# 1st word is 4 characters long.
print(f"1st word is {len(FirstWord)} characters long.")
# 2nd word is 7 characters long.
print(f"2nd word is {len(SecondWord)} characters long.")
# Words together makes one closed compound 'firefighter'.
print(f"Words together makes one closed compound '{FirstWord + SecondWord}'.")
# Program ending.
print("Program ending.")