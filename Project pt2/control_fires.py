import pygame

import user_fires_logic
import menu_result_display
import sys

import user_ship_logic


class Cell1:
    def __init__(self):
        self.clicked = False


def gridsquare(player_name):

    """
    Runs the main game window and calls outside functions from user_fires and user_ship_logic.
    :param player_name: name entered in welcome screen
    :return: calls ending_screen function
    """

    pygame.mixer.init()

    # Importing sounds for hits and misses and ships clicking into place
    hit_sound = pygame.mixer.Sound("hit_sound.mp3")
    miss_sound = pygame.mixer.Sound("miss_sound.wav")
    ship_set = pygame.mixer.Sound('ship_set.wav')

    pygame.display.set_caption('Battleship')

    grid_width = 15
    grid_height = 15
    player_board = [[Cell1() for _ in range(grid_width)] for _ in range(300, 600)]
    ship_board = [[Cell1() for _ in range(grid_width)] for _ in range(0, 300)]

    pygame.init()
    window = pygame.display.set_mode((300, 600))

    clock = pygame.time.Clock()



    run = True
    hit_counter = 0 # keeps track of how many hits the user has
    mouse_click = 0 # keeps track of the number of mouse clicks to ensure user clicks in correct field
    computer_hit = [] # keeps track of x, y coordinates of the computer's hits on user's ships
    computer_miss = [] # keeps track of x, y coordinates of the computer's misses on user's ships
    while run:
        clock.tick(100)
        comp_shot = None
        for event in pygame.event.get():
            # ends game if user or computer has hit all ships
            if event.type == pygame.QUIT or hit_counter == 17 or len(computer_hit) == 17:
                if hit_counter == 17: # result if user wins
                    kill_count = count_ship_hits(player_board)
                    return menu_result_display.ending_screen(kill_count, player_name, 'won!')
                if len(computer_hit) == 17: # result if user loses
                    kill_count = count_ship_hits(player_board)
                    return menu_result_display.ending_screen(kill_count, player_name, 'lost')
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    # if mouse click is in top half of board and user ships are set up after 5 clicks
                    if 0 <= event.pos[1] <= 300 and mouse_click >= 5:

                        row = event.pos[1] // 30
                        col = event.pos[0] // 30
                        player_board[row][col].clicked = True

                        # calls cell_check which checks if the clicked cell is a hit
                        # checks clicker_check list to make sure cell has not already been clicked
                        if user_fires_logic.cell_check(col, row) and (col, row) not in clicker_check:

                            hit_sound.play()
                            hit_counter += 1

                            # computer fires on bottom half of board at user's ships
                            comp_shot = user_fires_logic.computer_shot(computer_hit, computer_miss)
                            x = comp_shot[0]
                            y = comp_shot[1]

                            if (x, y) in user_ships: # computer's shot is checked against user's ships for hit or miss
                                computer_hit.append((x, y)) # cell is added to list of hits
                            else:
                                computer_miss.append((x, y)) # cell is added to list of misses

                        # calls cell_check which checks if the clicked cell is a miss
                        # checks clicker_check list to make sure cell has not already been clicked
                        elif not user_fires_logic.cell_check(col, row) and (col, row) not in clicker_check:
                            miss_sound.play()

                            # computer fires at bottom half of board at user's ships
                            comp_shot = user_fires_logic.computer_shot(computer_hit, computer_miss)
                            x = comp_shot[0]
                            y = comp_shot[1]
                            if (x, y) in user_ships: # computer shot is checked for hit or miss
                                computer_hit.append((x, y)) # cell is added to list of hits
                                print(computer_hit)
                            else:
                                computer_miss.append((x, y)) # cell is added to list of misses
                                print(computer_miss)

                    # checks for mouse clicks in the bottom half of the board
                    # limits clicks to 5 so users can't change ship positions or click in bottom half after setting up
                    # their ships and can only click in top half to take shots at computer's ships
                    if 300 <= event.pos[1] <= 600 and mouse_click <= 5:
                        mouse_click += 1
                        row = event.pos[1] // 30
                        col = event.pos[0] // 30
                        if mouse_click <= 5:
                            player_board[row][col].clicked = True
                        else:
                            player_board[row][col].clicked = False # sets cell.clicked to false if over 5 clicks

                        # first click sets up user's aircraft carrier (5 cells long)
                        if mouse_click == 1:

                            # direction checks which direction the ship can face without going outside the bounds
                            # of the grid
                            direction = user_ship_logic.user_carrier_check_dir(col, row)
                            ship_set.play() # plays satisfying click sound when ship is set

                            # depending on direction all cells in ship are set to clicked so color can be changed
                            if direction == 1: # if ship goes up
                                player_board[row - 1][col].clicked = True
                                player_board[row - 2][col].clicked = True
                                player_board[row - 3][col].clicked = True
                                player_board[row - 4][col].clicked = True
                            elif direction == 2: # if ship goes right
                                player_board[row][col + 1].clicked = True
                                player_board[row][col + 2].clicked = True
                                player_board[row][col + 3].clicked = True
                                player_board[row][col + 4].clicked = True
                            elif direction == 3: # if ship goes down
                                player_board[row + 1][col].clicked = True
                                player_board[row + 2][col].clicked = True
                                player_board[row + 3][col].clicked = True
                                player_board[row + 4][col].clicked = True
                            elif direction == 4: # if ship goes left
                                player_board[row][col - 1].clicked = True
                                player_board[row][col - 2].clicked = True
                                player_board[row][col - 3].clicked = True
                                player_board[row][col - 4].clicked = True

                        # second click sets up user's battleship (4 cells long)
                        elif mouse_click == 2:
                            # checks allowable direction without going outside grid and checks against already
                            # placed ships to prevent overlaps
                            direction = user_ship_logic.user_battleship_check_dir(col, row, user_ships)
                            ship_set.play()

                            # depending on direction all cells in ship are set to clicked so color can be changed
                            if direction == 1: # if ship goes up
                                player_board[row - 1][col].clicked = True
                                player_board[row - 2][col].clicked = True
                                player_board[row - 3][col].clicked = True

                            elif direction == 2: # if ship goes right
                                player_board[row][col + 1].clicked = True
                                player_board[row][col + 2].clicked = True
                                player_board[row][col + 3].clicked = True

                            elif direction == 3: # if ship goes down
                                player_board[row + 1][col].clicked = True
                                player_board[row + 2][col].clicked = True
                                player_board[row + 3][col].clicked = True

                            elif direction == 4: # if ship goes left
                                player_board[row][col - 1].clicked = True
                                player_board[row][col - 2].clicked = True
                                player_board[row][col - 3].clicked = True
                            else: # if ship cannot go any direction
                                player_board[row][col].clicked = False # cell is unmarked
                                mouse_click -= 1 # mouse_click is removed and user must click a new cell for battleship

                        # third click sets up user's destroyer (3 cells long)
                        elif mouse_click == 3:
                            # checks allowable direction without going outside grid and checks against already
                            # placed ships to prevent overlaps
                            direction = user_ship_logic.user_destroyer_check_dir(col, row, user_ships)
                            ship_set.play()

                            # depending on direction all cells in ship are set to clicked so color can be changed
                            if direction == 1: # if ship goes up
                                player_board[row - 1][col].clicked = True
                                player_board[row - 2][col].clicked = True

                            elif direction == 2: # if ship goes right
                                player_board[row][col + 1].clicked = True
                                player_board[row][col + 2].clicked = True

                            elif direction == 3: # if ship goes down
                                player_board[row + 1][col].clicked = True
                                player_board[row + 2][col].clicked = True

                            elif direction == 4: # if ship goes left
                                player_board[row][col - 1].clicked = True
                                player_board[row][col - 2].clicked = True
                            else: # if ship cannot be placed any direction
                                player_board[row][col].clicked = False # cell is unclicked
                                mouse_click -= 1 # mouse click removed to replace ship in acceptable location

                        # fourth click sets up user's submarine (3 cells long)
                        elif mouse_click == 4:
                            # checks allowable direction without going outside grid and checks against already
                            # placed ships to prevent overlaps
                            direction = user_ship_logic.user_submarine_check_dir(col, row, user_ships)
                            ship_set.play()

                            # depending on direction all cells in ship are set to clicked so color can be changed
                            if direction == 1: # if ship goes up
                                player_board[row - 1][col].clicked = True
                                player_board[row - 2][col].clicked = True

                            elif direction == 2: # if ship goes right
                                player_board[row][col + 1].clicked = True
                                player_board[row][col + 2].clicked = True

                            elif direction == 3: # if ship goes down
                                player_board[row + 1][col].clicked = True
                                player_board[row + 2][col].clicked = True

                            elif direction == 4: # if ship goes left
                                player_board[row][col - 1].clicked = True
                                player_board[row][col - 2].clicked = True
                            else: # if ship cannot be placed any direction
                                player_board[row][col].clicked = False # cell is unclicked
                                mouse_click -= 1 # mouse click is removed to replace ship in acceptable location

                        # fifth click sets up user's patrol boat (2 cells long); last ship
                        elif mouse_click == 5:
                            # checks allowable direction without going outside grid and checks against already
                            # placed ships to prevent overlaps
                            direction = user_ship_logic.user_patrol_check_dir(col, row, user_ships)
                            ship_set.play()

                            # depending on direction all cells in ship are set to clicked so color can be changed
                            if direction == 1: # if ship goes up
                                player_board[row - 1][col].clicked = True

                            elif direction == 2: # if ship goes right
                                player_board[row][col + 1].clicked = True

                            elif direction == 3: # if ship goes down
                                player_board[row + 1][col].clicked = True

                            elif direction == 4: # if ship goes left
                                player_board[row][col - 1].clicked = True
                            else: # if ship cannot be placed in any direction
                                player_board[row][col].clicked = False # cell is unclicked
                                mouse_click -= 1 # mouse click is removed to replace ship in acceptable location

        clicker_check = [] # holds all x,y coordinates for clicked cells in the top half of the board
        user_ships = [] # holds all x,y coordinates for the user's ships in the bottom half of the board

        window.fill(0)

        for iy, rowOfCells in enumerate(player_board):
            for ix, cell in enumerate(rowOfCells): # iterates through every cell in the entire grid

                if (ix, iy) not in clicker_check: # checks for cells that have already been clicked

                    # checks cell_check function to check for hits on ships and makes sure that the click was in the
                    # top half of the board to paint the cells the appropriate color
                    if cell.clicked and user_fires_logic.cell_check(ix, iy) and not user_fires_logic.ship_board_check(iy):
                        clicker_check.append((ix, iy)) # appends cell to clicker_check list so cannot be clicked again
                        color = 'red' # colors hits red
                    elif cell.clicked and not user_fires_logic.cell_check(ix, iy) and not user_fires_logic.ship_board_check(iy):
                        clicker_check.append((ix, iy)) # appends cell to clicker_check list so cannot be clicked again
                        color = 'white' # colors misses white
                if not cell.clicked and not user_fires_logic.ship_board_check(iy):
                    color = (0, 71, 171) # colors all non-clicked cells in top half blue

                if (ix, iy) in computer_hit: # if cell is in computer_hit list cells are colored red
                    color = 'red'
                elif (ix, iy) in computer_miss: # if cell is in computer_miss list cells are colored white
                    color = 'white'

                # sets color of initial ships placed by the user in the bottom half of the board to dark gray
                # and appends all clicked cells to the user_ships list
                elif cell.clicked and user_fires_logic.ship_board_check(iy):
                    color = (50, 50, 50)
                    user_ships.append((ix, iy))

                # all non-clicked cells that aren't hits or misses in bottom half are colored light gray
                elif not cell.clicked and user_fires_logic.ship_board_check(iy):
                    color = 'gray'

                pygame.draw.rect(window, color, (ix*30+1.5, iy*30+1.5, 27, 27)) # cells are drawn in

        pygame.display.flip()

    pygame.quit()
    exit()



def count_ship_hits(player_board):

    """
    count_ship_hits function takes a total of all hits and specifies which hits were on which ships.
    :param player_board: cells in top half of board
    :return: number of hits on each ship and sunk message if applicable
    """

    # initializes all kill counters to 0 and boat_kills list to be 5 empty strings
    patrol_kill = 0
    battleship_kill = 0
    destroyer_kill = 0
    carrier_kill = 0
    sub_kill = 0
    boat_kills = ['', '', '', '', '']

    for row in player_board:
        for cell in row:

            # checks through each ship and adds 1 to the individual ship's counter for every hit,
            # up to the length of the ship itself
            if cell.clicked and user_fires_logic.check_patrol(row.index(cell), player_board.index(row)):
                if patrol_kill < 2:
                    patrol_kill += 1

            if cell.clicked and user_fires_logic.check_battleship(row.index(cell), player_board.index(row)):
                if battleship_kill < 4:
                    battleship_kill += 1
            if cell.clicked and user_fires_logic.check_destroyer(row.index(cell), player_board.index(row)):
                if destroyer_kill < 3:
                    destroyer_kill += 1

            if cell.clicked and user_fires_logic.check_carrier(row.index(cell), player_board.index(row)):
                if carrier_kill < 5:
                    carrier_kill += 1

            if cell.clicked and user_fires_logic.check_submarine(row.index(cell), player_board.index(row)):
                if sub_kill < 3:
                    sub_kill += 1

        # if number of hits on each ship equals the length of that ship, "SUNK" is returned to the boat_kills list
        # otherwise an empty string is added

        if patrol_kill == 2:
            boat_kills[0] = "SUNK"
        else:
            boat_kills[0] = ""

        if sub_kill == 3:
            boat_kills[1] = "SUNK"
        else:
            boat_kills[1] = ""

        if destroyer_kill == 3:
            boat_kills[2] = "SUNK"
        else:
            boat_kills[2] = ""

        if battleship_kill == 4:
            boat_kills[3] = "SUNK"
        else:
            boat_kills[3] = ""

        if carrier_kill == 5:
            boat_kills[4] = "SUNK"
        else:
            boat_kills[4] = ""

    return patrol_kill, sub_kill, destroyer_kill, battleship_kill, carrier_kill, boat_kills


def comp_hit_check(x, y, user_ships):

    """
    function checks to see if the cell guessed by the computer hit the user's ships.
    :param x: x value
    :param y: y value
    :param user_ships: list of all points that make up the user's ships
    :return: True if x,y is part of a ship, else False
    """
    if (x, y) in user_ships:
        return True
    else:
        return False

