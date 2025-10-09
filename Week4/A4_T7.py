
print("Program starting.\n")
print("Check multiplicative persistence.")

number = int(input("Insert an integer: "))
steps = 0

while number != 0:
    if number < 10:
        break
    number_str = str(number)
    product = 1
    for i in range(len(number_str)):
        num = int(number_str[i])
        product = product * num

        if i < len(number_str) - 1:
            print(num, end=" * ")
        else:
            print(num, end="")
    
    print(" = " + str(product))
    steps += 1
    number = product

    if number == 0:
        break

print("No more steps.\n")
print(f"This program took {steps} step(s)")
print("\nProgram ending.")
