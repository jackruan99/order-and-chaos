# Plays Order and Chaos Game


# Importing all necessary libraries
from board import Board
import copy


# Plays a game by placing random marks at random locations
def play_game_randomly(size):
    board = Board(size)
    for _ in range(size ** 2):
        board.print_board()
        board.random_move()
        board.evaluate(size=True)
        if board.get_winner() != None:
            board.print_board()
            print(board.get_winner(), "WINS!")
            break


# Implementing the Minimax Algorithm
def minimax(board):
    if board.get_round() == board.size ** 2:
        board.evaluate(size=True)
        return board.get_winner()
    else:
        loc = board.get_empty_loc()[0]
        new_board_x = copy.deepcopy(board)
        new_board_x.place_mark(loc, 'X')
        new_board_o = copy.deepcopy(board)
        new_board_o.place_mark(loc, 'O')
        winner1 = minimax(new_board_x)
        winner2 = minimax(new_board_o)
        if winner1 == winner2:
            return winner1
        else:
            return 'Order' if board.round % 2 == 0 else 'Chaos'


# Driver Code
print(minimax(Board(4)))
