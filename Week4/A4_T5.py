print("Program starting.\n")

start = int(input("Insert starting point: "))
stop = int(input("Insert stopping point: "))
inspect = int(input("Insert inspection point: "))
print()

Run = True

if (start >= stop):
    print("Starting point value must be less than the stopping point value.")
    Run = False
if (start > inspect) or (inspect > stop):
    print("Inspection value must be within the range of start and stop.")
    Run = False

if(Run):
    print("First loop - inspection with break:")
    for i in range(start, stop):
        if(i == inspect):
            break
        else:
            print(i, end=" ")
    print("\nSecond loop - inspection with continue:")
    for i in range(start, stop):
        if(i == inspect):
            continue
        else:
            print(i, end=" ")
print()
print("\nProgram ending.")