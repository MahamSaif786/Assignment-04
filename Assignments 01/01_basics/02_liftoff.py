def countdown_to_liftoff():
    for i in range(10, 0, -1):  # Start from 10, stop at 1, decrement by 1
        print(i, end=" ")  
    
    print("Liftoff!")

def main():
    # Call the countdown function
    countdown_to_liftoff()

if __name__ == "__main__":
    main()
