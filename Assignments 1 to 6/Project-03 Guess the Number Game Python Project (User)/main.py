import random

def user_guess(x=100):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            if guess < 1 or guess > x:
                print(f'Please enter a number between 1 and {x}.')
                continue
            if guess < random_number:
                print('Sorry, guess again. Too low.')
            elif guess > random_number:
                print('Sorry, guess again. Too high.')
        except ValueError:
            print('Invalid input! Please enter a number.')
    
    print(f'Yay, congratulations! You have guessed the number {random_number} correctly!')

user_guess(100)