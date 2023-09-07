import random


def play():
    user = input("'R' for rock, 'P' for papper and 'S' for scissors.").lower()
    computer = random.choice(['R', 'P', 'S']).lower()

    if user == computer:
        return "tie"
