

def print_intro():
    '''
    Print welcome screen
        @return None
    '''
    print('\nBattleship Game\n')
    print(' __________         __    __  .__                .__    .__')
    print(' \______   \_____ _/  |__/  |_|  |   ____   _____|  |__ |__|_____')  
    print('  |    |  _/\__  \\   __\   __\   | _/ __ \ /  ___/  |  \|  \____ \ ') 
    print('  |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   Y  \  |  |_> >')
    print('  |______  /(____  /__|  |__| |____/\___  >____  >___|  /__|   __/ ')
    print('         \/      \/                     \/     \/     \/   |__|    ')
    print('\n')


def init_board():
    '''
    Initialize the board
        @return list 10x10 grid as the initial board
    '''
    board = []
    for x in range(10):
        board.append(['~'] * 10)
    return board


def print_board(board):
    '''
    Print the board
        @return None
    '''
    print('\n')
    h = 0
    print(' '*5, '   '.join(ALLOWED_NUMBERS), ' ', sep='')
    for row in board:
        print(' '*3 + '-'*41)
        print(' ' + ALLOWED_LETTERS[h] + ' | ' + ' | '.join(row) + ' |')
        h += 1
    print(' '*3 + '-'*41 + '\n')


def print_outro():
    '''
    Exit the game.
    '''
    exit()