import requests
from bs4 import BeautifulSoup
import random


def hangman():
    """
    Hangman game with visual progress display.
    """
    words = ['python', 'hangman', 'programming', 'developer', 'algorithm', 'function', 'variable']
    target_word = random.choice(words).lower()
    guessed_letters = set()
    remaining_lives = 6
    
    hangman_states = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   \\|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   \\|/
           |    |
           |   / \\
        --------
        """
    ]
    
    print("\n" + "="*40)
    print("WELCOME TO HANGMAN!")
    print("="*40)
    print(f"Word length: {len(target_word)} letters\n")
    
    while remaining_lives > 0:
        # Display current state
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in target_word])
        print(hangman_states[6 - remaining_lives])
        print(f"Word: {' '.join(display_word)}")
        print(f"Guessed: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        print(f"Lives remaining: {remaining_lives}\n")
        
        # Check win condition
        if display_word == target_word:
            print("🎉 YOU WON! 🎉")
            print(f"The word was: {target_word}")
            return
        
        # Get user input
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.\n")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter!\n")
            continue
        
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in target_word:
            print(f"✓ Correct! '{guess}' is in the word.\n")
        else:
            remaining_lives -= 1
            print(f"✗ Wrong! '{guess}' is not in the word.\n")
    
    # Game over
    print(hangman_states[6])
    print(f"💀 GAME OVER! 💀")
    print(f"The word was: {target_word}")


# ==================== MAIN ====================

if __name__ == "__main__":
    # Example: Play Hangman
    hangman()
    
    # Example: Scrape a website (uncomment to use)
    # url = "https://example.com"
    # web_scraper(url)
