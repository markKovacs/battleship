
# Global variables
ALLOWED_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
ALLOWED_NUMBERS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def get_touching_coords(coord):
    '''
    Get horizantally or vertically neighbour coordinates of a coordinate
        @param list coord The coordinate of which neighbours will be returned
        @return list The neighbour coordinates
    '''
    touching = []
    # corner case
    if coord == [0, 0]:
        touching.extend([[0, 1], [1, 0]])
    elif coord == [0, 9]:
        touching.extend([[0, 8], [1, 9]])
    elif coord == [9, 0]:
        touching.extend([[9, 1], [8, 0]])
    elif coord == [9, 9]:
        touching.extend([[8, 9], [9, 8]])
    # top, bottom row and first, last column excluding corners
    elif coord[0] == 0 and coord[1] > 0 and coord[1] < 9:
        touching.extend([[0, coord[1] - 1], [0, coord[1] + 1], [1, coord[1]]])
    elif coord[0] == 9 and coord[1] > 0 and coord[1] < 9:
        touching.extend([[9, coord[1] - 1], [9, coord[1] + 1], [8, coord[1]]])
    elif coord[1] == 0 and coord[0] > 0 and coord[0] < 9:
        touching.extend([[coord[0] - 1, 0], [coord[0] + 1, 0], [coord[0], 1]])
    elif coord[1] == 9 and coord[0] > 0 and coord[0] < 9:
        touching.extend([[coord[0] - 1, 9], [coord[0] + 1, 9], [coord[0], 8]])
    # inside the board
    else:
        touching.extend([[coord[0], coord[1] - 1], [coord[0], coord[1] + 1],
                        [coord[0] - 1, coord[1]], [coord[0] + 1, coord[1]]])
    return touching


def convert_coords(coord):
    '''
    Converts a coord to a letter based on global dictionary
        @param coord int The character to be converted
        @return str The letter for the given int value
    '''
    inv_letters = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J'}
    return str(inv_letters[coord])


def convert_letter(letter):
    '''
    Converts a letter to a number based on global dictionary
        @param letter string The character to be converted
        @return int The number value for the string key
    '''
    letters = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}
    return int(letters[letter])


def check_hit(ships, shootTo):
    '''
    Check if ship was hit
        @param ships list List of ships
        @param shootTo list List of shoot coords
        @return bool True if hit, otherwise False
    '''
    result = []
    shootTo.append(True)
    hit_status = False
    for ship in range(len(ships)):
        for coords in range(len(ships[ship])):
            if shootTo in ships[ship] and ships[ship][coords][0] == shootTo[0] and ships[ship][coords][1] == shootTo[1]:
                ships[ship][coords][2] = False
                hit_status = True
    result.extend([hit_status, ships])
    return result


def check_sunk(ships, shootTo):
    '''
    Check if a ship is sunk (all default True coords of the ship have become False)
        @param ships list List of ships
        @param shootTo list List of shoot coords
        @return bool True if the ship sunk, otherwise False
    '''
    shootTo[2] = False
    status = True
    for ship in range(len(ships)):
        for coords in range(len(ships[ship])):
            if shootTo in ships[ship] and ships[ship][coords][2] is True:
                status = False
    return status


def check_all_sunk(ships):
    '''
    Check if all ships are sunk (all default True coords of the ships have become False)
        @param ships list List of ships
        @return bool True if all sunk, otherwise False
    '''
    status = True
    for ship in range(len(ships)):
        for coords in range(len(ships[ship])):
            if ships[ship][coords][2] is True:
                status = False
    return status


def place_ship_xy(size, ship_name, allowed_coords):
    '''
    User places ship
        @param size        int       Size of the ship to be created
        @param ship_name   string    Nice name of the ship
        @return            list      Return ship with x, y coords and a True as part of the list
    '''
    ship_xy = []
    result = []
    break_coords_input = True
    for coords in range(size):
        answer_coord = True
        while answer_coord:
            # Put together a list that contains the next allowed coordinates
            if coords > 0:
                # Get neighbour coords of last coord
                previous_coords = [ship_xy[coords - 1][0], ship_xy[coords - 1][1]]
                neighbour_coords = get_touching_coords(previous_coords)
                # Remove elements from the neighbour coords that are not in the allowed_coords
                neighbour_coords_mod = [coord for coord in neighbour_coords if coord in allowed_coords]
                # if there is no allowed space...
                if len(neighbour_coords_mod) == 0:
                    print('Unfortunately you cannot place this ship, please start again!')
                    # return with 'again'
                    ship_xy = 'again'
                    break_coords_input = False
                    answer_coord = False
                    break
                else:
                    print('\nYour next coordinate must be touching the previous one horizantally or vertically,',
                          'so you can choose from the following coordinates:')
                    # we need to convert the coords back to letters
                    choose_coords = [convert_coords(coord[0]) + str(coord[1] + 1) for coord in neighbour_coords_mod]
                    print(', '.join(choose_coords), '\n')

            ship_answer = input('Enter #' + str(coords + 1) +
                                ' coordinates for your ' + ship_name + ' (size ' + str(size) + '): ')
            is_valid_ship_answer = validate_ship_answer(ship_answer)
            if is_valid_ship_answer[0]:
                valid_coords = [convert_letter(ship_answer[:1].upper()), int(ship_answer[1:3]) - 1]
                if coords == 0:
                    if valid_coords in allowed_coords:
                        allowed_coords.remove(valid_coords)
                        valid_coords.append(True)
                        ship_xy.append(valid_coords)
                        break
                    else:
                        print('This coordinate is already occupied or not allowed!')
                else:
                    if valid_coords in neighbour_coords_mod:
                        allowed_coords.remove(valid_coords)
                        valid_coords.append(True)
                        ship_xy.append(valid_coords)
                        break
                    else:
                        print('This coordinate is not among the allowed coordinates!')
            else:
                [print(error) for error in is_valid_ship_answer[1]]
        # finish placing coords because ship can't be placed
        if break_coords_input is False:
            break
    if break_coords_input is True:
        print('\nShip {} completed!\n\n'.format(ship_name))

    result.extend([ship_xy, allowed_coords])
    return result


def validate_ship_answer(ship_answer):
    is_valid = False
    errors = []
    result = []

    if ship_answer == 'exit' or ship_answer == 'quit':
        outro.print_outro()

    try:
        ship_y = int(ship_answer[1:3])
    except ValueError:
        errors.append('Invalid format. Please try again.')
    except:
        error.append('Unexpected error. Try again or enter exit or quit to finish the game.')
    else:
        if (ship_answer[:1].upper() not in ALLOWED_LETTERS or
                int(ship_answer[1:3]) not in ALLOWED_NUMBERS or len(ship_answer) > 3):
            errors.append('Invalid format! A-J and 1-10 are allowed. Example: A1, C3, F10')
        else:
            is_valid = True

    result.extend([is_valid, errors])
    return result


def create_allowed_coords():
    '''
    Creates a list with default values for the allowed coordinates, used in placement phase
        @return list List of list of x, y values
    '''
    return [[i, j] for i in range(10) for j in range(10)]


def create_ships():
    '''
    Create all ships for one player
        @param player int Player 1 or Player 2
        @return list List of lists of all ships that belong to one player
    '''
    ships = []
    allowed_coords = create_allowed_coords()

    for count, ship_size in enumerate([5, 4, 3, 3, 2]):
        # set ship names
        if count == 0:
            ship_name = 'Carrier'
        elif count == 1:
            ship_name = 'Battleship'
        elif count == 2:
            ship_name = 'Cruiser'
        elif count == 3:
            ship_name = 'Submarine'
        else:
            ship_name = 'Destroyer'

        ship_to_be = ['again']
        while ship_to_be[0] == 'again':
            ship_to_be = place_ship_xy(ship_size, ship_name, allowed_coords)
            allowed_coords = ship_to_be[1]
            if ship_to_be[0] != 'again':
                ships.append(ship_to_be[0])

    return ships


def user_guess():
    '''
    Ask user to make a guess, ask for (x,y) coords
        @return   list   Row and Column coordinates to shoot to, provided by user
    '''
    user_guess = []
    answer_shootTo = True
    while answer_shootTo:
        user_guess_coord = input("Enter coords for your shot: ")
        valid_user_guess = validate_user_guess(user_guess_coord)
        if valid_user_guess[0]:
            user_guess.extend([convert_letter(user_guess_coord[:1].upper()), int(user_guess_coord[1:3]) - 1])
            answer_shootTo = False
        else:
            [print(error) for error in valid_user_input[1]]
    return user_guess


def validate_user_guess(user_guess_coord):

    is_valid = False
    errors = []
    result = []

    if user_guess_coord == 'exit' or user_guess_coord == 'quit':
        outro.print_outro()
    elif (user_guess_coord[:1].upper() not in ALLOWED_LETTERS or
          int(user_guess_coord[1:3]) not in ALLOWED_NUMBERS or
          len(user_guess_coord) > 3):
        errors.append('Invalid format! A-J and 1-10 are allowed. Example: A1, C3, F10')
    else:
        is_valid = True

    result.extend([is_valid, errors])
    return result


def get_sunk_ship(shootTo, ships):
    for index, ship in enumerate(ships):
        if shootTo in ship:
            return index


def evaluate_guess(shootTo, board, ship):
    '''
    Evaluate user guess (hit or miss or else)
        @param shootTo    list   Shooting coords provided by user
        @param board      list   Player Board
        @param ship       list   List of ships' coords on the map
        @return           bool   False if game ends, otherwise True
    '''
    target_shot = board[shootTo[0]][shootTo[1]]
    result = []
    status = False
    if shootTo[0] not in range(10) or shootTo[1] not in range(10):    # check if shot is on the board
            print('That\'s out of range.')
    elif (target_shot == 'M' or
          target_shot == 'H' or
          target_shot == 'S'):    # check if guess was already made before
        print('You guessed that already. Pay attention next turn!')
    else:
        ship_hit = check_hit(ship, shootTo)
        print(ship_hit)
        ship = ship_hit[1]
        if ship_hit[0]:
            print('Target hit!')
            board[shootTo[0]][shootTo[1]] = 'H'
            if check_sunk(ship, shootTo):
                print('Target sunk!')
                sunk_ship = get_sunk_ship(shootTo, ship)
                for x, y in ship[sunk_ship]:
                    board[x][y] = color_sunk + 'S' + color_sea
            if check_all_sunk(ship):
                print('You win! You\'ve just sunk all my ships!')
                print('Game Over')
                status = True
        else:                            # missed shot
            print('You missed it!')
            board[shootTo[0]][shootTo[1]] = 'M'

    result.extend([status, board])
    return result
