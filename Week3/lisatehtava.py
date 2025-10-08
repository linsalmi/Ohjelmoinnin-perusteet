# Tehtävä:
# Jos käyttäjätunnus = omaNimi ja ikä = >= 18 ja käyttäjä on admin -> avataan admin-sivu
# Jos käyttäjätunnus = omaNimi ja ikä >= 18 -> avataan käyttäjäsivu
# Jos ikä < 18 -> kerrotaan käyttäjälle: Ikä ei riitä
# Jos käyttäjätunnus != omaNimi -> Pääsy kielletty

# Admin-tunnuksilla valikko: 1. Lisää uusi käyttäjä, 2. Tarkista laitteen toiminta, 3. Exit
# Käyttäjäsivulla valikko: 1. Tarkista omat tiedot, 2. Exit

print("Tervetuloa ohjelmaan")
nimi = input("Anna nimesi: ")
ikä = int(input("Anna ikäsi: "))
admin = input("Oletko admin? (kyllä/ei): ")

if nimi == "Linda" and ikä >= 18 and admin == "kyllä":
    print("Avataan admin-sivu...")
    print("Valinnat: \n1 - Lisää uusi käyttäjä\n2 - Tarkista laitteen toiminta\n0 - Exit")
    valinta = int(input("Valintasi: "))
    if valinta == 1:
        uusikäyttäjä = input("Uusi käyttäjänimi: ")
        uudenikä = int(input("Uuden käyttäjän ikä: "))
        uusiadmin = input("Onko uusi käyttäjä admin? (kyllä/ei): ")
        print(f"Uusi käyttäjä {uusikäyttäjä} lisätty.")
        print("Ohjelma päättyy.")
    elif valinta == 2:
        print("Kaikki kunnossa.")
        print("Ohjelma päättyy.")
    elif valinta == 0:
        print("Poistutaan...")
        print("Ohjelma päättyy.")
    else:
        print("Tuntematon valinta.")
        print("Ohjelma päättyy.")
elif nimi == "Linda" and ikä >= 18 and admin != "kyllä":
    print("Avataan käyttäjäsivu...")
    print("Valinnat: \n1 - Tarkista omat tiedot\n0 - Exit")
    valinta = int(input("Valintasi: "))
    if valinta == 1:
        print(f"Käyttäjänimi: {nimi}, ikä: {ikä}")
        print("Ohjelma päättyy.")
    elif valinta == 0:
        print("Poistutaan...")
        print("Ohjelma päättyy.")
    else:
        print("Tuntematon valinta.")
        print("Ohjelma päättyy.")
elif ikä <= 18:
    print("Ikä ei riitä.")
    print("Ohjelma päättyy.")
elif nimi != "Linda":
    print("Pääsy kielletty.")
    print("Ohjelma päättyy.")
