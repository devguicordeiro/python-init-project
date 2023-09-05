import random


def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0
    while guess != randomNumber:
        guess = input(f"Guess a number between 1 and {x}: ")
        print(guess)


guess(10)
