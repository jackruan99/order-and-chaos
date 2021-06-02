# Order and Chaos Python Program


# Importing all necessary libraries
import numpy as np
import random


# Creates an empty game board
# Returns a size x size board where '~' denotes a spot is empty (Done)
def create_board(size):
    return np.array([['~'] * size for i in range(size)])


# Prints the game board with iteration number
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


# Checks and returns all empty places on board
def possibilities(board):
    l = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '~':
                l.append((i, j))
    return(l)


# Checks whether Order has size - 1 marks in a horizontal row
def row_win(board):
    return row_win_helper(board, 'X') or row_win_helper(board, 'O')


# Helper function for row_win
def row_win_helper(board, mark):
    for x in range(len(board)):
        first = board[x][0] == mark
        last = board[x][len(board)-1] == mark
        middle = True
        for y in range(1, len(board)-1):
            if board[x][y] != mark:
                middle = False
                break
        if (first or last) and middle:
            return True
    return False


# Checks whether Order has size - 1 marks in a vertical column
def col_win(board):
    return col_win_helper(board, 'X') or col_win_helper(board, 'O')


# Helper function for col_win
def col_win_helper(board, mark):
    for y in range(len(board)):
        first = board[0][y] == mark
        last = board[len(board)-1][y] == mark
        middle = True
        for x in range(1, len(board)-1):
            if board[x][y] != mark:
                middle = False
                break
        if (first or last) and middle:
            return True
    return False


# Checks whether Order has size - 1 marks on a diagonal
def diag_win(board):
    return diag_win_helper(board, 'X') or diag_win_helper(board, 'O')


# Helper function for diag_win
def diag_win_helper(board, mark):
    top_left_starts = [(0,0), (0,1), (1,0), (1,1)] # This is hard coded
    for start in top_left_starts:
        x,y = start
        i = 0
        win = True
        while i < (len(board)-1):
            if board[x][y] != mark:
                win = False
                break
            x += 1
            y += 1
            i += 1
        if win:
            return True

    top_right_starts = [(0, len(board)-1), (0,len(board)-2), (1,len(board)-1), (1,len(board)-2)] # This is hard coded
    for start in top_right_starts:
        x,y = start
        i = 0
        win = True
        while i < (len(board)-1):
            if board[x][y] != mark:
                win = False
                break
            x += 1
            y -= 1
            i += 1
        if win:
            return True
    
    return False


# Evaluates whether Order or Chaos wins, or the game goes on
# Returns "Order", "Chaos" or None (Done)
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

    for i in range(size ** 2):  # plays randomly
        board = random_move(board)
        counter += 1
        print_board(board, counter)
        winner = evaluate(board)
        if winner != None:
            print(winner, "WINS!")
            break


# Driver Code
play_game(6)
