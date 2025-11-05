DELIMITER = ","

def collectWords():
    collectedWords = ""
    while True:
        word = input("Insert word(empty stops): ")
        if word == "":
            break
        if collectedWords != "":
            collectedWords += DELIMITER
        collectedWords += word
    return collectedWords

def analyseWords(words):
    if not words:
        print("- 0 Words")
        print("- 0 Characters")
        print("- 0.00 Average word length")
        return

    word_list = words.split(DELIMITER)
    word_count = len(word_list)
    char_count = sum(len(w) for w in word_list)
    avg_length = char_count / word_count
    
    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print("- {:.2f} Average word length".format(avg_length))

def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")

main()
