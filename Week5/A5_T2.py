def frameWord(PWord):
    print("*" * (len(PWord)+4))
    print(f"* {PWord} *")
    print("*" * (len(PWord)+4))
    return None

def main():
    print("Program starting.")
    word = input("Insert word: ")
    print("")
    frameWord(word)
    print("\nProgram ending.")
    return None



main()