from random import randint
import math


##
# Print the board
#
# return void
##
def print_board(board):
    print('\n')
    h = 0
    print('     1   2   3   4   5   6   7   8   9   10 ')
    for row in board:
        print('   ' + '-' * 41)
        print(' ' + allowed_letters[h] + ' | ' + ' | '.join(row) + ' |')
        h += 1
    print('   ' + '-' * 41 + '\n')


##
# AI places ship randomly - column coordinate
#
# return int Column coordinate
##
def init_board(board):
    for x in range(10):
        board.append(['O'] * 10)

