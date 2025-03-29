import random  
DONE_LIKELIHOOD = 0.3  
def done():
    """Returns True with a probability of DONE_LIKELIHOOD"""
    return random.random() < DONE_LIKELIHOOD  

def chaotic_counting():
    """
    1 se 10 tak counting karega, lekin kisi bhi number pe ruk sakta hai 
    agar done() function True return kare.
    """
    for i in range(1, 11):  
        if done():  
            return  
        print(i, end=" ")  
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")  

if __name__ == "__main__":
    main()
