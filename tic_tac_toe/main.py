class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # list to represent board
        self.current_winner = None  # track of the winner

    def print_board(self):
        # settings the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]
        # moves = []
        # for (i, spot) in enumerate(self.board):
        #     # ["x", "x", "o"] --> [(0, "x"), (1, "x"), (2, "o")]
        #     if spot == " ":
        #         moves.append(i)

        # return moves
