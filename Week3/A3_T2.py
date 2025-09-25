# Make Python program which does the following steps:

# Prompt user to insert
# 1. A word
# 2. A character
# Find if the character exists in the word. Possible prints below.
# 1. Word "{WordFirst}" contains character "{Character}"
# 2. Word "{WordFirst}" doesn't contain character "{Character}"
# Prompt user to insert one more word
# Compare the first word to the second word. Examples below:
# 1. The first word "{WordFirst}" is before the second word "{WordSecond}" alphabetically.
# 2. The second word "{WordSecond}" is before the first word "{WordFirst}" alphabetically.
# 3. Both inserted words are the same alphabetically, "{WordFirst}"
# Example program run


# Program starting.
print("Program starting.")
# String comparisons
print("String comparisons")
# Insert first word: beans
sana1 = input("Insert first word: ")
# Insert a character: n
kirjain = input("Insert a character: ")
# Word "beans" contains character "n"
if kirjain in sana1:
    print(f"Word \"{sana1}\" contains character \"{kirjain}\"")
if kirjain not in sana1:
    print(f"Word \"{sana1}\" doesn't contain character \"{kirjain}\"")
# Insert second word: banana
sana2 = input("Insert second word: ")
# The second word "banana" is before the first word "beans" alphabetically.
if sana2 < sana1:
    print(f'The second word "{sana2}" is before the first word "{sana1}" alphabetically.')
if sana2 > sana1:
    print(f'The first word "{sana1}" is before the second word "{sana2}" alphabetically.')
if sana2 == sana1:
    print(f'Both inserted words are the same aphabetically, "{sana1}"')
# Program ending.
print("Program ending.")