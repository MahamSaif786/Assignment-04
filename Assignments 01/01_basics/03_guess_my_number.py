import random

def guess_number():
    num = random.randint(1, 99)  
    print("I am thinking of a number between 1 and 99...")
    
    while (guess := int(input("Enter a guess: "))) != num:
        print("Your guess is too low" if guess < num else "Your guess is too high")
    
    print(f"Congrats! The number was: {num}")

def main():
    guess_number()

if __name__ == "__main__":
    main()
