import random

def print_random_numbers():
    for _ in range(10):  
        print(random.randint(1, 100), end=" ")  
    print()  

def main():
    print_random_numbers()

if __name__ == "__main__":
    main()
