# Order and Chaos Python Program


# Importing all necessary libraries
import numpy as np
import random


# Creates an empty game board (Done)
def create_board(size):
    return np.array([['~'] * size for i in range(size)])


# Prints the game board with iteration number (Done)
def print_board(board, counter):
    if counter < 2:
        print("Board after", str(counter), "move")
    else:
        print("Board after", str(counter), "moves")

    size = len(board)
    print("-" * (4 * size + 1))
    for i, row in enumerate(board):
        print(("|" + " {} |" * size).format(*
              [x if x != '~' else ' ' for x in row]))
        if i != size - 1:
            print("|" + "---+" * (size - 1) + "---|")
    print("-" * (4 * size + 1))
    print()


# Checks and returns all empty places on board (Done)
def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '~':
                l.append((i, j))
    return(l)


# Checks whether Order has SIZE marks in a horizontal row
def row_win(board):
    return row_win_helper(board, 'X') or row_win_helper(board, 'O')

# Helper function for row_win
# TODO: checks whether Order has size - 1 marks in a horizontal row


def row_win_helper(board, mark):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[x, y] != mark:
                win = False
                break
        if win:
            return(win)
    return(win)


# Checks whether Order has SIZE marks in a vertical column
def col_win(board):
    return col_win_helper(board, 'X') or col_win_helper(board, 'O')

# Helper function for col_win
# TODO: checks whether Order has size - 1 marks in a vertical column


def col_win_helper(board, mark):
    for x in range(len(board)):
        win = True
        for y in range(len(board)):
            if board[y][x] != mark:
                win = False
                break
        if win:
            return(win)
    return(win)


# Checks whether Order has SIZE marks on a diagonal
def diag_win(board):
    return diag_win_helper(board, 'X') or diag_win_helper(board, 'O')

# Helper function for diag_win
# TODO: checks whether Order has size - 1 marks on a diagonal


def diag_win_helper(board, mark):
    win = True
    y = 0
    for x in range(len(board)):
        if board[x, x] != mark:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(board)):
            y = len(board) - 1 - x
            if board[x, y] != mark:
                win = False
    return win


# Evaluates whether Order or Chaos wins, or the game goes on
# Returns "Order" or "Chaos" if they win or None if no one wins (Done)
def evaluate(board):
    winner = None
    if (row_win(board) or col_win(board) or diag_win(board)):
        winner = 'Order'
    elif len(possibilities(board)) == 0:
        winner = 'Chaos'
    return winner


# Place a ramdom mark on an empty spot (Done)
def random_move(board):
    selection = possibilities(board)
    current_loc = random.choice(selection)
    board[current_loc] = random.choice(['X', 'O'])
    return(board)


# Main function to start the game
def play_game(size):
    board, winner, counter = create_board(size), None, 0
    print_board(board, counter)
    for i in range(size ** 2):
        board = random_move(board)
        counter += 1
        print_board(board, counter)
        winner = evaluate(board)
        if winner != None:
            print(winner, "WINS!")
            break


# Driver Code
play_game(6)
