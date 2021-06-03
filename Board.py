# Order and Chaos Board Class


# Importing all necessary libraries
import numpy as np
import random


class Board:
    def __init__(self, size):
        self.size = size
        self.round = 0
        self.board = np.array([[' '] * size for _ in range(size)])
        self.empty_loc = [(i, j) for i in range(self.size)
                          for j in range(self.size)]
        self.winner = None

    # Helper functions for evaluate (logic for evaluting a winner)
    def row_win_size(self):
        return self.row_win_size_helper('X') or self.row_win_size_helper('O')

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

    def row_win(self):
        return self.row_win_helper('X') or self.row_win_helper('O')

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

    def col_win_size(self):
        return self.col_win_size_helper('X') or self.col_win_size_helper('O')

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

    def col_win(self):
        return self.col_win_helper('X') or self.col_win_helper('O')

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

    def diag_win_size(self):
        return self.diag_win_size_helper('X') or self.diag_win_size_helper('O')

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

    def diag_win(self):
        return self.diag_win_helper('X') or self.diag_win_helper('O')

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

    # WRAPER FUNCTIONS
    def get_size(self):
        return self.size

    def get_round(self):
        return self.round

    def get_board(self):
        return self.board

    def get_empty_loc(self):
        return self.empty_loc

    def get_winner(self):
        return self.winner

    # Prints the game board with round number
    def print_board(self):
        print('Round:', self.round)
        print("-" * (4 * self.size + 1))
        for i, row in enumerate(self.board):
            print(("|" + " {} |" * self.size).format(*[x for x in row]))
            if i != self.size - 1:
                print("|" + "---+" * (self.size - 1) + "---|")
        print("-" * (4 * self.size + 1))
        print()

    # Place a mark on an empty spot
    def random_move(self, mark=None):
        loc = random.choice(self.empty_loc)
        if mark == None:
            self.board[loc] = random.choice(['X', 'O'])
        else:
            self.board[loc] = mark
        self.empty_loc.remove(loc)
        self.round += 1

    # Place a mark at a specific location
    def place_mark(self, loc, mark, overwrite=False):
        self.board[loc] = mark
        if not overwrite:
            self.empty_loc.remove(loc)
            self.round += 1

    # Evaluates the winner with size or size - 1 in a row, or game continues
    # Returns "Order", "Chaos" or None
    def evaluate(self, size=False):
        if size:
            if (self.row_win_size() or self.col_win_size() or self.diag_win_size()):
                self.winner = 'Order'
            elif len(self.empty_loc) == 0:
                self.winner = 'Chaos'
        else:
            if (self.row_win() or self.col_win() or self.diag_win()):
                self.winner = 'Order'
            elif len(self.empty_loc) == 0:
                self.winner = 'Chaos'
