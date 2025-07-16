import random

# List of words to choose from
words = ['python', 'programming', 'javascript', 'computer', 'keyword']

# ASCII hangman stages
hangman_stages = [
    """
     -----
     |   |
         |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
    """
     -----
     |   |
    [O   |
    /|\\  |
    / \\  |
         |
    =========
    """,
    """
     -----
     |   |
    [O]  |
    /|\\  |
    / \\  |
         |
    =========
    """
]

def choose_word():
    return random.choice(words)

def get_hangman_stage(attempts_left):
    return hangman_stages[8 - attempts_left]

def color_attempts(attempts):
    if attempts >= 6:
        return "green"
    elif attempts >= 3:
        return "orange"
    else:
        return "red"

def update_word_display(chosen_word, guessed_letters):
    return [letter if letter in guessed_letters else '_' for letter in chosen_word]
