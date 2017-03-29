
##
# Print the board
#
# return void
##
def print_board(board):
    allowed_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    print("value of board_p1 from graphics", board)
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
def init_board():
    board = []
    for x in range(10):
        board.append(['O'] * 10)

    return board


def print_intro():
    print('\nBattleship Game\n')
    print(' __________         __    __  .__                .__    .__')
    print(' \______   \_____ _/  |__/  |_|  |   ____   _____|  |__ |__|_____')  
    print('  |    |  _/\__  \\   __\   __\   | _/ __ \ /  ___/  |  \|  \____ \ ') 
    print('  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   Y  \  |  |_> >')
    print('  |______  /(____  /__|  |__| |____/\___  >____  >___|  /__|   __/ ')
    print('         \/      \/                     \/     \/     \/   |__|    ')
    print('\n')