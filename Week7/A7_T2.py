def integers():                                             
    feed = input("Insert comma separated integers: ")      
    parts = feed.split(",")                                
    valid_num: list[int] = []

    for part in parts:  
        part = part.strip()

        try:
            num = int(part) 
            valid_num.append(num) 

        except ValueError: 
            print(f"Invalid value '{part}' detected.") 

    if not valid_num: 
        print("No values to analyse.")
        return  
    
    Sum = sum(valid_num) 
    count = len(valid_num)
    parity = "even" if Sum % 2 == 0 else "odd"  

    print(f"There are {count} integers in the list.")  
    print(f"Sum of the integers is {Sum} and it's {parity}") 

def main():    
    print("Program starting.")
    integers()
    print("Program ending.")

if __name__ == "__main__":
    main()