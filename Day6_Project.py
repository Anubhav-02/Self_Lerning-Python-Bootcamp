# Day 4 Project - Hangman Game Project

import random

words_list = [
    "algorithm", "photosynthesis", "quantum", "neptune", "symphony", "photoshop",
    "metaphor", "oxidation", "democracy", "genome", "choreography", "ecosystem",
    "encryption", "logarithm", "renaissance", "covalent", "plateau", "parliament",
    "antibiotic", "cryptography"
]
# Creating Function to select random word
def select_word():
  return random.choice(words_list)

# Hangman game function
def play_hangman():
    print("Welcome to Hangman!")
    
    # Select a random word
    chosen_word = select_word()
    word_length = len(chosen_word)
    
    # Initialize variables
    display = ["_"] * word_length  # Display blanks for each letter
    guessed_letters = []           # Store guessed letters
    lives = 6                      # Number of wrong guesses allowed

    # Game loop
    while lives > 0 and "_" in display:
        print(f"Lives left: {lives}")
        print("Current word: " + " ".join(display))
        
        # Get the player's guess
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try again!")
            continue

        # Add the guessed letter to the list of guesses
        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in chosen_word:
            # Replace blanks with the guessed letter
            for index in range(word_length):
                if chosen_word[index] == guess:
                    display[index] = guess
            print(f"Good guess! '{guess}' is in the word.")
        else:
            lives -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    # Check the game outcome
    if "_" not in display:
        print(f"Congratulations! You guessed the word: {chosen_word}")
    else:
        print(f"You ran out of lives! The word was: {chosen_word}")

# Play the game
play_hangman()



