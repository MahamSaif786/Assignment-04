# Problem1: List 

def list():
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    print("Length of the fruit list:", len(fruit_list))
    
    fruit_list.append('mango')
    
    print("Updated fruit list:", fruit_list)

# Problem 2: Index Game

def access_element(my_list, index):
    if 0 <= index < len(my_list):
        return my_list[index]  
    else:
        return "Invalid index!"  
def modify_element(my_list, index, new_value):
    if 0 <= index < len(my_list):
        my_list[index] = new_value  
        return "List updated successfully!"
    else:
        return "Invalid index!"  
def slice_list(my_list, start, end):
    if 0 <= start < len(my_list) and 0 <= end <= len(my_list) and start < end:
        return my_list[start:end]  
    else:
        return "Invalid start or end index!"  

def index_game():
    my_list = ['red', 'blue', 'green', 'yellow', 'black']
    
    while True:
        print("\nCurrent list:", my_list)
        print("Choose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':  # Access an element
            index = int(input("Enter index to access: "))
            print("Result:", access_element(my_list, index))
        
        elif choice == '2':  # Modify an element
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print("Result:", modify_element(my_list, index, new_value))
        
        elif choice == '3':  # Slice the list
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(my_list, start, end))
        
        elif choice == '4':  # Exit the game
            print("Exiting the game. Goodbye!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

def main():
    list()  
    index_game()  

if __name__ == "__main__":
    main()
