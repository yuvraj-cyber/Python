import random

def word_guessing_game():
    # List of predefined words
    word_list = ["apple", "banana", "orange", "grape", "melon", "strawberry", "kiwi", "pineapple", "peach", "mango"]

    # Select a random word from the list
    selected_word = random.choice(word_list)

    while True:
        # Get user input for word guess
        user_guess = input("Guess the word: ")

        # Check if the guess is correct
        if user_guess.lower() == selected_word:
            print("Congratulations! You guessed the right word.")
            break
        else:
            print("Wrong guess. Try again!")

# Run the word guessing game
word_guessing_game()
