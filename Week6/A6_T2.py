def writefile(pfilename, pcontent):
    filehandle = open(pfilename, 'w')
    filehandle.write(pcontent)
    filehandle.close()
    
    return None

def main():
    print("Program starting.")
    firstname = input("Insert first name: ")
    lastname = input("Insert last name: ")
    filename = input("Insert filename: ")
    content = "{}\n{}\n" .format(firstname,lastname)
    writefile(filename, content)
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()