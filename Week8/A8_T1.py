import time                                                       

def Options():                                                     
    print("\nOptions: ")
    print("1 - Set pause duration")                                
    print("2 - Activate pause")                                    
    print("0 - Exit")                                              

def getNumericInput(prompt, value_type=float):                   
    while True:                                                    
        try:                                                       
            value = value_type(input(prompt))                      
            return value                                           
        
        except ValueError:                                         
            print(f"Invalid input. Please enter a valid {value_type.__name__}.") 

        except (KeyboardInterrupt, EOFError):                      
            print("\nUser interrupted. Returning to menu.")       
            return None                                           

def main():                                                        
    print("Program starting.")                                     
    
    pause = None                                                   
    
    while True:                                                    
        Options()                                                  

        choice = input("Your choice: ").strip()                    

        if choice == "1":                                          
            result = getNumericInput("Insert pause duration (s): ", float)  

            if result is not None:
                pause = result
                print("")

        elif choice == "2":                                        
            if pause is None:                                      
                print("Pause is not set. \nSet pause first.\n") 

            else:                                                  
                print(f"Pausing for {pause} seconds.")             
                time.sleep(pause)                                  
                print("Unpaused.\n")                               

        elif choice == "0":                                        
            print("Exiting program.")                                    
            print("\nProgram ending.")                               
            break                                                  

        else:                                                      
            print("Unknown option!\n")        

if __name__ == "__main__":                                         
    main()                                                       