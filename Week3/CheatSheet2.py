# print("Welcome to the temp app!")
# Temp = int(input("What is the temperature of CPU? "))

# if(Temp > 80):
#     print("Warning, temperature too high!")
# else:
#     print("All cool, keep on going!")


# print("Program starting.")
# nro1 = int(input("Anna numero: "))
# Vastaus = nro1 % 2
# if Vastaus == 0:
#     print(f"parillinen: {Vastaus}")
# else:
#     print(f"pariton: {Vastaus}")


# if(Temp > 80):
#     if(Temp > 90):
#         print("You are toast")
#     else:
#         print("Warning")
# else:
#     print("You are ok")

# if(Temp > 90):
#     print("You are toast")
# elif(Temp > 80):
#     print("Warning!")
# else:
#     print("You are ok")


# Town = "Lahti"
# Street = "Mukkulankatu"
# Building = 19

# if((Town == "Lahti" or "Lahtis") and Street == "Mukkulankatu" and Building == 19):
#     print("You are at LAB")
# elif(Town == "Lahti" and (Street != "Mukkulankatu" or Building != 19)):
#     print("You are in the correct town, but check the street address again")
# elif not(Town == "Lahti" or "Lahtis" and Street == "Mukkulankatu" and Building == 19):
#     print("You are completely lost...")


# import random

# print (random.random())
# print(random.randint(1, 6))

# Tee yksinkertainen kivi-sakset-paperi -peli random-metodia käyttäen.
import random
pelaaja = int(input("Pelataan Kivi Paperi Sakset.\n Anna valintasi:\n1 - Kivi\n2 - Paperi\n3 - Sakset\n"))
vastustaja = random.randint(1,3)
print(f"Pelasit {pelaaja}, vastustajasi pelasi {vastustaja}:")
if pelaaja == vastustaja:
    print("Tasapeli")
elif (pelaaja == 1 and vastustaja == 3) or (pelaaja == 2 and vastustaja == 1) or (pelaaja == 3 and vastustaja == 2):
    print("Sinä voitit!")
else:
    print("Vastustaja voitti.")