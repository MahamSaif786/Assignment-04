def main():
    """
    Asks the user for a number, doubles it repeatedly, 
    and prints the results until the value reaches 100 or more.
    """
    curr_value = int(input("Enter a number: "))  
     
    while curr_value < 100:  
        curr_value *= 2  
        print(curr_value, end=" ") 

if __name__ == '__main__':
    main()
