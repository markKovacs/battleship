

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
        touching.extend([[coord[0], coord[1] - 1], [coord[0], coord[1] + 1], [coord[0] - 1, coord[1]], [coord[0] + 1, coord[1]]])
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
    shootTo.append(True)
    for ship in range(len(ships)):
        for coords in range(len(ships[ship])):
            if shootTo in ships[ship] and ships[ship][coords][0] == shootTo[0] and ships[ship][coords][1] == shootTo[1]:
                ships[ship][coords][2] = False
                return True
    return False


def check_sunk(ships, shootTo):
    '''
    Check if a ship is sunk (all default True coords of the ship have become False)
        @param ships list List of ships
        @param shootTo list List of shoot coords
        @return bool True if the ship sunk, otherwise False
    '''
    shootTo[2] = False
    for ship in range(len(ships)):
        for coords in range(len(ships[ship])):
            if shootTo in ships[ship] and ships[ship][coords][2] == True:
                return False
    return True


def check_all_sunk(ships):
    '''
    Check if all ships are sunk (all default True coords of the ships have become False)
        @param ships list List of ships
        @return bool True if all sunk, otherwise False
    '''
    for ship in range(len(ships)):
        for coords in range(len(ships[ship])):
            if ships[ship][coords][2] == True:
                return False
    return True

