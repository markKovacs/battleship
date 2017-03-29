

def user_guess():
    '''
    Ask user to make a guess, ask for (x,y) coords
        @return list Row and Column coordinates to shoot to, provided by user
    '''
    user_guess = []
    while True:
        try:
            user_guess_coord = input("Enter coords for your shot: ") # A1 -> 00, J10 -> 99
            if user_guess_coord == 'exit' or user_guess_coord == 'quit':
                break
            elif user_guess_coord[:1].upper() not in ALLOWED_LETTERS or int(user_guess_coord[1:3]) not in ALLOWED_NUMBERS or len(user_guess_coord) > 3:
                print('Invalid format! A-J and 1-10 are allowed. Example: A1, C3, F10')
                raise ValueError
            else:
                row = convert_letter(user_guess_coord[:1].upper()) # A-J -> 0-9(int)
                col = int(user_guess_coord[1:3]) - 1 # 1-10 -> 0-9(int)
                user_guess.append(row)
                user_guess.append(col)
                return user_guess
        except ValueError:
            print('Please enter the coordinates again.')
        except:
            print('An error occured. You can enter exit or quit to end the game.')
        finally:
            if turns == 'exit' or turns == 'quit':
                exit()

##
# Evaluate user guess (hit or miss or else)
#
# @param shootTo        list   Shooting coords provided by user
# @param board          list   Player Board
# @param ship           list   List of ships' coords on the map
#
# return bool False if game ends, True else
##
def evaluate_guess(shootTo, board, ship):
    if shootTo[0] not in range(10) or shootTo[1] not in range(10):    # check if shot is on the board
            print('That\'s out of range.')
    elif board[shootTo[0]][shootTo[1]] == 'M' or board[shootTo[0]][shootTo[1]] == 'H':    # check if guess was already made before
        print('You guessed that already. Pay attention next turn!')
    else:
        if check_hit(ship, shootTo):     # target hit
            print('Target hit!')
            board[shootTo[0]][shootTo[1]] = 'H'
            if check_sunk(ship, shootTo):             # check if ship is sunk
                print('Target sunk!')
            if check_all_sunk(ship):         # check if all ships are sunk
                print('You win! You\'ve just sunk all my ships!')
                print('Game Over')
                return True
        else:                            # missed shot
            print('You missed it!')
            board[shootTo[0]][shootTo[1]] = 'M'
    if turn == turns - 1:                # check game end
        print('Game Over.')
        return True
    print_board(board)
    return False


##
# User places ship
#
# @param size int Size of the ship to be created
# @param ship_name string Nice name of the ship
# @param player int 1 for Player 1, 2 for Player 2
#
# @return list Return ship with x, y coords and a True as part of the list
##
def place_ship_xy(size, ship_name, player):
    ship_xy = []
    for coords in range(size):
        while True:
            try:
                if coords > 0:
                # Put together a list that contains the next allowed coordinates
                    # Get neighbour coords of last coord
                    neighbour_coords = []
                    previous_coords = []
                    previous_coords = [ship_xy[coords - 1][0], ship_xy[coords - 1][1]]
                    neighbour_coords = get_touching_coords(previous_coords)
                    # Remove elements from the neighbour coords that are not in the allowed_list_p1 or allowed_list_p2 (depending on the user)
                    if player == 1:     # player 1
                        neighbour_coords_mod = []   # .remove() and del does not do the job, we nedd to add the elements to a new list :( 
                        for f in neighbour_coords:
                            if f in allowed_coords_p1:
                                neighbour_coords_mod.append(f)
                        if len(neighbour_coords_mod) == 0:      # if there are no allowed spaces)...
                            # print you cannot place this ship, delete ship, start placing this ship again
                            print('Unfortunately you cannot place this ship, please start again!')
                            # readd removed coords to allowed_coords!!!
                            if len(ship_xy) > 0:
                                for z in ship_xy:
                                    if z not in allowed_coords_p1:
                                        allowed_coords_p1.append(z)    
                            return 'again'
                        else:
                            print('\nYour next coordinate must be touching the previous one horizantally or vertically, so you can choose from the following coordinates:')
                            # we need to convert the coords back to letters
                            choose_coords = []
                            for c in neighbour_coords_mod:
                                choose_coords.append(convert_coords(c[0]) + str(c[1] + 1))
                            print(', '.join(choose_coords))
                            print('\n')
                    else:   ### player 2
                        neighbour_coords_mod = []   # .remove() and del does not do the job, we nedd to add the elements to a new list :( 
                        for f in neighbour_coords:
                            if f in allowed_coords_p2:
                                neighbour_coords_mod.append(f)
                        if len(neighbour_coords_mod) == 0:      # if there are no allowed spaces)...
                            # print you cannot place this ship, delete ship, start placing this ship again
                            print('Unfortunately you cannot place this ship, please start again!')
                            # readd removed coords to allowed_coords!!!
                            if len(ship_xy) > 0:
                                for z in ship_xy:
                                    if z not in allowed_coords_p2:
                                        allowed_coords_p2.append(z)    
                            return 'again'
                        else:
                            print('\nYour next coordinate must be touching the previous one horizantally or vertically, so you can choose from the following coordinates:')
                            # we need to convert the coords back to letters
                            choose_coords = []
                            for c in neighbour_coords_mod:
                                choose_coords.append(convert_coords(c[0]) + str(c[1]+1))
                            print(', '.join(choose_coords))
                            print('\n')
                ship_answer = input('Enter #' + str(coords + 1) + ' coordinates for your ' + ship_name + ' (size ' + str(size) + '): ')
                if ship_answer == 'exit' or ship_answer == 'quit':
                    break
                elif ship_answer[:1].upper() not in ALLOWED_LETTERS or int(ship_answer[1:3]) not in ALLOWED_NUMBERS or len(ship_answer) > 3:
                    print('Invalid format! A-J and 1-10 are allowed. Example: A1, C3, F10')
                    raise ValueError
                else:
                    if player == 1:     # player 1
                        if coords == 0:
                            if [convert_letter(ship_answer[:1].upper()), int(ship_answer[1:3]) - 1] in allowed_coords_p1:
                                allowed_coords_p1.remove([convert_letter(ship_answer[:1].upper()), int(ship_answer[1:3]) - 1])
                                ship_xy.append([convert_letter(ship_answer[:1].upper()), int(ship_answer[1:3]) - 1, True])
                                break
                            else:
                                print('This coordinate is already occupied!')
                                raise ValueError
                        else:   # from 2nd coords till last coord
                            if [convert_letter(ship_answer[:1].upper()), int(ship_answer[1:3]) - 1] in neighbour_coords_mod:
                                allowed_coords_p1.remove([convert_letter(ship_answer[:1].upper()), int(ship_answer[1:3]) - 1])
                                ship_xy.append([convert_letter(ship_answer[:1].upper()), int(ship_answer[1:3]) - 1, True])
                                break
                            else:
                                print('This coordinate is not among the allowed coordinates!')
                                raise ValueError
                    else:               # player 2
                        if coords == 0:
                            if [convert_letter(ship_answer[:1].upper()), int(ship_answer[1:3]) - 1] in allowed_coords_p2:
                                allowed_coords_p2.remove([convert_letter(ship_answer[:1].upper()), int(ship_answer[1:3]) - 1])
                                ship_xy.append([convert_letter(ship_answer[:1].upper()), int(ship_answer[1:3]) - 1, True])
                                break
                            else:
                                print('This coordinate is already occupied!')
                                raise ValueError
                        else:   # from 2nd coords till last coord
                            if [convert_letter(ship_answer[:1].upper()), int(ship_answer[1:3]) - 1] in neighbour_coords_mod:
                                allowed_coords_p2.remove([convert_letter(ship_answer[:1].upper()), int(ship_answer[1:3]) - 1])
                                ship_xy.append([convert_letter(ship_answer[:1].upper()), int(ship_answer[1:3]) - 1, True])
                                break
                            else:
                                print('This coordinate is not among the allowed coordinates!')
                                raise ValueError
            except ValueError:
                print('Please enter the coordinates again.')
            except:
                print('\nAn error occured. You can enter exit or quit to end the game.')
            finally:
                if ship_answer == 'exit' or ship_answer == 'quit':
                    exit()
    return ship_xy



def create_ships(player):
    '''
    Create all ships for one player
        @param player int Player 1 or Player 2
        @return list List of lists of all ships that belong to one player
    '''
    ships = []
    loop = 0
    for sh_size in [5, 4, 3, 3, 2]:
        # set ship names
        if loop == 0:
            ship_name = 'Carrier'
        elif loop == 1:
            ship_name = 'Battleship'
        elif loop == 2:
            ship_name = 'Cruiser'
        elif loop == 3:
            ship_name = 'Submarine'
        else:
            ship_name = 'Destroyer'
        print('\n')
        ship_to_be = 'again'
        while  ship_to_be == 'again':
            ship_to_be = place_ship_xy(sh_size, ship_name, player)
            if ship_to_be != 'again':
                ships.append(ship_to_be)
        loop += 1
    return ships



