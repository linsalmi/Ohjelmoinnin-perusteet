

def main():
    print("Program starting.")
    print("This program can copy a file.")

    sourcefile = input("Insert source filename: ")
    destinationfile = input("Insert destination filename: ")

    print(f"Reading file '{sourcefile}' content.")
    file = open(sourcefile, "r")
    content = file.read()
    file.close()
    print("File content ready in memory.")

    print(f"Writing content into file '{destinationfile}'.")
    file = open(destinationfile, "w")
    file.write(content)
    file.close()
    print("Copying operation complete.")
    
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()