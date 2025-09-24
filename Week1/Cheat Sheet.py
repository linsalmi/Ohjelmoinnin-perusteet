print("Hello World!")
print("Here we are")

print("He said: \"Hello\", and kept walking")
print("He said hello \n \r \b \t and kept walking") #escape characters: \n new line, \r return (enter), \t tab, \b backspace etc.

# stringejä (str) voi yhdistää + -merkillä, tai toistaa * -merkillä
word1 = "Co"
word2 = "ral"
print(word1 + word2)
print((word1 + "-") * 3 + word1 + word2)

# len antaa stringin pituuden 
s = "Helkkarinpitkäsanamontakirjainta"
print(len(s)) #tai 
pituus = len(s)
print(f"Sanan pituus on {pituus} kirjainta.")
print(s[0]) # ensimmäinen merkki
print(s[-1]) # ensimmäinen merkki loppupäästä

# sep="..." muuttaa erottelijan
print(1,2,3,4,5, sep="-")
# end="..." muuttaa lopun joksikin muuksi kuin rivinvaihdoksi
print("Hei", end="")
print("pparallaa.")

text = " Hello, World! "
print(text.upper()) # " HELLO, WORLD! "
print(text.lower()) # " hello, world! "
print(text.strip()) # "Hello, World!"
print(text.strip().split()) # ['Hello,',World!']
print(text.replace("World","Python")) # " Hello, Python! "

exampleString = "Text and numb3rs"
exampleInt = 12 # integer = kokonaisluku
exampleFloat = 12.12 # desimaaliluku 
# float voidaan pyöristää: 
# number = 234.5647292340234
# print(round(number)) # 235
# print(round(number,3)) # 234.565 (kolme desimaalia)
exampleBoolean = False # True tai False

Firstname = input("What is your firstname: ")
Lastname = input("What is your lastname: ")
print("Hello ", Firstname, Lastname)
print(f"Hello {Firstname}") # f-string, muuttujat aaltosulkuihin

Sentence = "Finding substring"
print(Sentence)
print(Sentence[0]) # antaa lauseen ensimmäisen merkin
print(Sentence[-2]) # loppupäästä toiseksiviimeinen
print(Sentence[2:9]) # merkit 2-9, ysi ensimmäinen jota ei näytetä
print(Sentence[:9]) # merkit ysiin asti
print(Sentence[-9:-2]) # loppupäästä -9 -> -2
print(Sentence[2:9:3]) # askeleita, alkaa kakkosesta ysiin asti ja etenee kolmen välein
print(Sentence[::3]) # alusta loppuun kolmen askeleen välein
print(Sentence[::-1]) # yhden askeleen välein lopusta alkuun

# ctrl + * tekee kaikista valituista kommentteja, takaisin sama komento

name = "Linda"
age = 37

#print(name + " " + str(age))

num1 = input("Anna luku 1 ")
num2 = input("Anna luku 2 ")

# inputista tulee aina stringiä ulos, siksi allaolevat pitää muuttaa integereiksi

num3 = int(num1) + int(num2)
print(num3)

