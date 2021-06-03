# Importing all necessary libraries
import numpy as np
import random

# Order and Chaos Board Class


class Board:
    def __init__(self, size):
        self.size = size
        self.iteration = 0
        self.board = np.array([[' '] * size for _ in range(size)])
        self.empty_loc = [(i, j) for i in range(self.size)
                          for j in range(self.size)]
        self.winner = None

    # Checks whether Order has SIZE marks in a horizontal row
    def row_win_size(self):
        return self.row_win_size_helper('X') or self.row_win_size_helper('O')

    # Helper function for row_win_size
    def row_win_size_helper(self, mark):
        for x in range(self.size):
            win = True
            for y in range(self.size):
                if self.board[x][y] != mark:
                    win = False
                    break
            if win:
                return True
        return False

    # Checks whether Order has size - 1 marks in a horizontal row
    def row_win(self):
        return self.row_win_helper('X') or self.row_win_helper('O')

    # Helper function for row_win
    def row_win_helper(self, mark):
        for x in range(self.size):
            first = self.board[x][0] == mark
            last = self.board[x][self.size-1] == mark
            middle = True
            for y in range(1, self.size-1):
                if self.board[x][y] != mark:
                    middle = False
                    break
            if (first or last) and middle:
                return True
        return False

    # Checks whether Order has SIZE marks in a vertical column
    def col_win_size(self):
        return self.col_win_size_helper('X') or self.col_win_size_helper('O')

    # Helper function for col_win_size
    def col_win_size_helper(self, mark):
        for y in range(self.size):
            win = True
            for x in range(self.size):
                if self.board[x][y] != mark:
                    win = False
                    break
            if win:
                return True
        return False

    # Checks whether Order has size - 1 marks in a vertical column
    def col_win(self):
        return self.col_win_helper('X') or self.col_win_helper('O')

    # Helper function for col_win
    def col_win_helper(self, mark):
        for y in range(self.size):
            first = self.board[0][y] == mark
            last = self.board[self.size-1][y] == mark
            middle = True
            for x in range(1, self.size-1):
                if self.board[x][y] != mark:
                    middle = False
                    break
            if (first or last) and middle:
                return True
        return False

    # Checks whether Order has SIZE marks on a diagonal
    def diag_win_size(self):
        return self.diag_win_size_helper('X') or self.diag_win_size_helper('O')

    # Helper function for diag_win_size
    def diag_win_size_helper(self, mark):
        win = True
        for x in range(self.size):
            if self.board[x][x] != mark:
                win = False
                break
        if win:
            return True
        win = True
        for x in range(self.size):
            if self.board[x][self.size-x-1] != mark:
                win = False
                break
        if win:
            return True
        return False

    # Checks whether Order has size - 1 marks on a diagonal
    def diag_win(self):
        return self.diag_win_helper('X') or self.diag_win_helper('O')

    # Helper function for diag_win
    def diag_win_helper(self, mark):
        top_left_starts = [(0, 0), (0, 1), (1, 0), (1, 1)]
        for start in top_left_starts:
            x, y = start
            i = 0
            win = True
            while i < (self.size-1):
                if self.board[x][y] != mark:
                    win = False
                    break
                x += 1
                y += 1
                i += 1
            if win:
                return True
        top_right_starts = [(0, self.size-1), (0, self.size-2),
                            (1, self.size-1), (1, self.size-2)]
        for start in top_right_starts:
            x, y = start
            i = 0
            win = True
            while i < (self.size-1):
                if self.board[x][y] != mark:
                    win = False
                    break
                x += 1
                y -= 1
                i += 1
            if win:
                return True
        return False

    # Evaluates whether Order or Chaos wins with SIZE in a row, or the game goes on
    # Returns "Order", "Chaos" or None
    def evaluate_size(self):
        if (self.row_win_size() or self.col_win_size() or self.diag_win_size()):
            self.winner = 'Order'
        elif len(self.empty_loc) == 0:
            self.winner = 'Chaos'

    # Evaluates whether Order or Chaos wins, or the game goes on
    # Returns "Order", "Chaos" or None
    def evaluate(self):
        if (self.row_win() or self.col_win() or self.diag_win()):
            self.winner = 'Order'
        elif len(self.empty_loc) == 0:
            self.winner = 'Chaos'

    # Prints the game board with iteration number
    def print_board(self):
        print('Iteration:', self.iteration)
        print("-" * (4 * self.size + 1))
        for i, row in enumerate(self.board):
            print(("|" + " {} |" * self.size).format(*[x for x in row]))
            if i != self.size - 1:
                print("|" + "---+" * (self.size - 1) + "---|")
        print("-" * (4 * self.size + 1))
        print()

    # Place a ramdom mark on an empty spot
    def random_move(self):
        loc = random.choice(self.empty_loc)
        self.board[loc] = random.choice(['X', 'O'])
        self.empty_loc.remove(loc)
        self.iteration += 1

    def place_mark(self, i, j, mark):
        self.board[i][j] = mark
        self.empty_loc.remove((i, j))
        return self.board

    def get_size(self):
        return self.size

    def get_iteration(self):
        return self.iteration

    def get_board(self):
        return self.board

    def get_empty_lco(self):
        return self.empty_loc

    def get_winner(self):
        return self.winner


# Plays a game by placing random marks at random locations
def play_game_randomly(size):
    board = Board(size)
    # board.print_board()
    for _ in range(size ** 2):
        board.random_move()
        # board.print_board()
        board.evaluate_size()
        if board.get_winner() != None:
            # print(board.get_winner(), "WINS!")
            return board.get_winner()
    return board.get_winner()


def make_tree(size):
    for i in range(size):
        for j in range(size):
            for mark in ['X', 'O']:
                board = Board(2)
                board.place_mark(i, j, mark)


# Driver Code
play_game_randomly(4)
# make_tree(2)
