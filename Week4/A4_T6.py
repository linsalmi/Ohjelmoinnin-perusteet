# Tee muuttuja, joka laskee kierrokset
# Muuta annettu arvo integeriksi.
# Arvo muuttuu loopin aikana.
# Tee while -loop, joka looppaa niin kauan, kuin arvo ei ole 1
#     printtaa alkuperäinen arvo ja lisää loppuun ->
#     testaa onko arvo parillinen (jakojäännöslasku)
#         jaa arvo kahdella
#     muussa tapauksessa (else)
#         kerro arvo kolmella ja lisää yksi

#     Lisää kierroksiin +1
# printtaa loppuun 1
# printtaa kierrokset (sequence had 6 total steps tms.)
# program ending

# For even numbers, divide by 2
# For odd numbers, multiply by 3 and add 1

print("Program starting.")
number = int(input("Insert a positive integer: "))

steps = 0
sequence = str(number)

while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = number * 3 + 1
    sequence = sequence + " -> " + str(number)
    steps = steps + 1
    
print(sequence)
print(f"Sequence had {steps} total steps.")
print("\nProgram ending.")