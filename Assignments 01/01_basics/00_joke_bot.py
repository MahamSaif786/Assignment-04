PROMPT = "What do you want? "
JOKE = "Here is a joke for you!\nWhy do programmers prefer dark mode?\nBecause light attracts bugs!"
SORRY = "Sorry I only tell jokes"

def joke_bot():
    user_input = input(PROMPT)
    
    if user_input == "Joke":
        print(JOKE)  
    else:
        print(SORRY)  

def main():
    joke_bot()

if __name__ == "__main__":
    main()