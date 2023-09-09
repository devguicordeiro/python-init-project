import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)  # chooses a random word from the list
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_wor(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print("You have already used that letter. Please try another one.")

    else:
        print("Invalid letter. Try again.")


user_input = input("Type a letter: ")
print(user_input)
