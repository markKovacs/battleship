from random import randint

##
# AI places ship randomly - row coordinate
#
# return int Row coordinate
##
def ai_random_row(board):
    return randint(0, len(board) - 1)


##
# AI places ship randomly - column coordinate
#
# return int Column coordinate
##
def ai_random_col(board):
    return randint(0, len(board[0]) - 1)