def double_until_hundred():
    curr_value = int(input("Enter a number: "))
    
    while curr_value < 100:
        curr_value *= 2  
        print(curr_value, end=" ")  
    print()  

def main():
    double_until_hundred()

if __name__ == "__main__":
    main()
