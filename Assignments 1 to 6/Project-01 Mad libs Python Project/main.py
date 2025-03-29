def mad_libs():
    print("\n🎉 Welcome to Mad Libs! 🎉\n")
    
    while True:
        adjective = input("Enter an adjective: ")
        noun = input("Enter a noun: ")
        verb = input("Enter a verb: ")
        place = input("Enter a place: ")

        story = f"\nOne day, a {adjective} {noun} decided to {verb} at the {place}. It was an unforgettable experience!\n"

        print("\nHere is your Mad Libs story:\n")
        print(story)

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("\nThanks for playing Mad Libs! Goodbye! 👋\n")
            break

mad_libs()
