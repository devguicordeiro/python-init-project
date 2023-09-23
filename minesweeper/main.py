import random


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size

        self.num_bombs = num_bombs

        self.board = self.make_new.board()

        self.assign_values_to_board()

        self.dug = set()

    def make_new_board(self):
        board = [[None for _ in range(self.dim_size)]
                 for _ in range(self.dim_size)]

        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == "*":
                continue

            board[row][col] = "*"
            bombs_planted += 1

        return board

    def assign_values_to_board(self):

        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == "*":
                    continue
                self.board[r][c] = self.get_num_neighboring_bombs(r, c)

    def get_num_neighboring_bombs(self, row, col):

        num_neighboring_bombs = 0
        for r in range(row-1, (row+1) + 1):
            


def play(dim_size=10, num_bombs=10):
    pass
