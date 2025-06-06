
import random
import string
from word import words  
def get_valid_word(words):
    word = random.choice(words).upper()  
    while '-' in word or ' ' in word:
        word = random.choice(words).upper()
    return word

def hangman():
    word = get_valid_word(words)  
    word_letters = set(word)  
    alphabet = set(string.ascii_uppercase)  
    used_letters = set()  
    lives = 10  

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} lives left. Used letters: {' '.join(used_letters)}")

        word_display = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_display))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1 
                print("Wrong guess!")

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        
        else:
            print('Invalid character. Please try again.')

    if lives == 0:
        print(f"Game over! The word was {word}.")
    else:
        print(f"Congratulations! You guessed the word {word} correctly!")

hangman()
