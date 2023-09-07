import random


def play():
    user = input(
        "What's your choice? 'R' for rock, 'P' for papper and 'S' for scissors.").lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    if isWin(user, computer):
        return "You won!"

    return "You lost!"


def isWin(player, opponent):

    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") \
            or (player == "p" and opponent == "r"):
        return True


print(play())
