import random
import string
from words import words


def get_valid_word(words):
    word = random.choice(words)  # chooses a random word from the list
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    # userinput

    while len(word_letters) > 0:

        # letter used
        print("You have used these letters: ", " ".join(used_letters))

        # current word dashes
        word_list = [
            letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You have already used that letter. Please try another one.")

        else:
            print("Invalid letter. Try again.")


hangman()
