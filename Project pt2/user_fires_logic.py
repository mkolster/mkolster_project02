import random

check = False


def cell_check(x, y):

    """
    cell_check calls individual functions that check for hits on specific ships
    :param x: x coordinate
    :param y: y coordinate
    :return: True if hit, False if not
    """
    if check_patrol(x, y):
        return True

    elif check_submarine(x, y):
        return True

    elif check_battleship(x, y):
        return True

    elif check_carrier(x, y):
        return True

    elif check_destroyer(x, y):
        return True
    else:
        return False


def check_patrol(x, y):

    """
    checks clicked cell against cells in patrol boat
    :param x: x coordinate
    :param y: y coordinate
    :return: True if hit, False if not
    """

    for i in range(len(patrol_boat)):
        if patrol_boat[i] == (x, y):
            return True
        elif i < 2:
            i += 1
        else:
            return False


def check_submarine(x, y):

    """
    checks clicked cell against cells in submarine
    :param x: x coordinate
    :param y: y coordinate
    :return: True if hit, False if not
    """

    for i in range(len(submarine)):
        if submarine[i] == (x, y):
            return True
        elif i < 3:
            i += 1
        else:
            return False


def check_destroyer(x, y):

    """
    checks clicked cell against cells in destroyer
    :param x: x coordinate
    :param y: y coordinate
    :return: True if hit, False if not
    """

    for i in range(len(destroyer)):
        if destroyer[i] == (x, y):
            return True
        elif i < 3:
            i += 1
        else:
            return False


def check_battleship(x, y):

    """
    checks clicked cell against cells in battleship
    :param x: x coordinate
    :param y: y coordinate
    :return: True if hit, False if not
    """

    for i in range(len(battleship)):
        if battleship[i] == (x, y):
            return True
        elif i < 4:
            i += 1
        else:
            return False


def check_carrier(x, y):
    """
    checks clicked cell against cells in carrier
    :param x: x coordinate
    :param y: y coordinate
    :return: True if hit, False if not
    """

    for i in range(len(carrier)):
        if carrier[i] == (x, y):
            return True
        elif i < 5:
            i += 1
        else:
            return False


def place_carrier(ships_list):

    """
    function randomly selects a point, then checks which direction to point the ship, and places the carrier
    in the top half of the board for the user to fire at
    :param ships_list: emtpy list
    :return: ships_list with carrier coordinates appended to it
    """

    # random x,y coordinates chosen
    x1 = random.randint(0, 9)
    y1 = random.randint(0, 9)

    ship = []

    # all four directions initialized as true
    up = True
    down = True
    left = True
    right = True

    # checks for left/right walls
    if x1 < 4:
        left = False
    elif x1 > 5:
        right = False
    elif 4 <= x1 <= 5:
        right = False

    # checks for top/bottom walls
    if y1 < 4:
        up = False
    elif y1 > 5:
        down = False
    elif 4 <= y1 <= 5:
        down = False

    # based on allowable directions, corresponding points are added to the ship list
    if up:
        y2 = y1 - 1
        y3 = y2 - 1
        y4 = y3 - 1
        y5 = y4 - 1

        ship = [(x1, y1), (x1, y2), (x1, y3), (x1, y4), (x1, y5)]
    elif right:
        x2 = x1 + 1
        x3 = x2 + 1
        x4 = x3 + 1
        x5 = x4 + 1

        ship = [(x1, y1), (x2, y1), (x3, y1), (x4, y1), (x5, y1)]
    elif down:
        y2 = y1 + 1
        y3 = y2 + 1
        y4 = y3 + 1
        y5 = y4 + 1
        ship = [(x1, y1), (x1, y2), (x1, y3), (x1, y4), (x1, y5)]

    elif left:
        x2 = x1 - 1
        x3 = x2 - 1
        x4 = x3 - 1
        x5 = x4 - 1

        ship = [(x1, y1), (x2, y1), (x3, y1), (x4, y1), (x5, y1)]

    ships_list.append(ship) # coordinates of the carrier in ship are appended to larger ships_list

    return ships_list


def place_battleship(ships_list):

    """
    function randomly selects a point, then checks which direction to point the ship, and places the battleship
    in the top half of the board for the user to fire at
    :param ships_list: list containing list of carrier coordinates
    :return: ships_list with battleship coordinates appended to it
    """

    # random x,y coordinates chosen
    x1 = random.randint(0, 9)
    y1 = random.randint(0, 9)
    ship = []

    # all directions are initialized True
    up = True
    down = True
    left = True
    right = True

    # checks left/right walls
    if x1 < 3:
        left = False
    elif x1 > 6:
        right = False
    elif 3 <= x1 <= 6:
        left = False

    # checks top/bottom walls
    if y1 < 3:
        up = False
    elif y1 > 6:
        down = False
    elif 3 <= y1 <= 6:
        up = False

    # based on allowable directions, corresponding points are added to the ship list
    if up:
        y2 = y1 - 1
        y3 = y2 - 1
        y4 = y3 - 1

        ship = [(x1, y1), (x1, y2), (x1, y3), (x1, y4)]
    elif right:
        x2 = x1 + 1
        x3 = x2 + 1
        x4 = x3 + 1

        ship = [(x1, y1), (x2, y1), (x3, y1), (x4, y1)]
    elif down:
        y2 = y1 + 1
        y3 = y2 + 1
        y4 = y3 + 1
        ship = [(x1, y1), (x1, y2), (x1, y3), (x1, y4)]

    elif left:
        x2 = x1 - 1
        x3 = x2 - 1
        x4 = x3 - 1

        ship = [(x1, y1), (x2, y1), (x3, y1), (x4, y1)]

    # overlap with already placed ships is checked
    for i in ship:
        for x in ships_list:
            if i in x:
                return place_battleship(ships_list) # if overlaps individual ship is replaced until successful

    ships_list.append(ship) # list of battleship coordinates are appended to larger ships_list
    return ships_list


def place_destroyer(ships_list):

    """
    function randomly selects a point, then checks which direction to point the ship, and places the destroyer
    in the top half of the board for the user to fire at
    :param ships_list: list containing lists of carrier and battleship coordinates
    :return: ships_list with carrier and battleship coordinates appended to it
    """

    # random x,y coordinates chosen
    x1 = random.randint(0, 9)
    y1 = random.randint(0, 9)
    ship = []

    # all directions initialized as True
    up = True
    down = True
    left = True
    right = True

    # checks left/right walls
    if x1 < 2:
        left = False
    elif x1 > 7:
        right = False
    elif 2 <= x1 <= 7:
        left = False

    # checks top/bottom walls
    if y1 < 2:
        up = False
    elif y1 > 7:
        down = False
    elif 2 <= y1 <= 7:
        up = False

    # based on allowable directions, corresponding points are added to the ship list
    if up:
        y2 = y1 - 1
        y3 = y2 - 1

        ship = [(x1, y1), (x1, y2), (x1, y3)]
    elif right:
        x2 = x1 + 1
        x3 = x2 + 1

        ship = [(x1, y1), (x2, y1), (x3, y1)]
    elif down:
        y2 = y1 + 1
        y3 = y2 + 1
        ship = [(x1, y1), (x1, y2), (x1, y3)]

    elif left:
        x2 = x1 - 1
        x3 = x2 - 1

        ship = [(x1, y1), (x2, y1), (x3, y1)]

    # checks for overlaps with existing ships
    for i in ship:
        for x in ships_list:
            if i in x:
                return place_destroyer(ships_list) # if overlaps individual ship is reset until successful

    ships_list.append(ship) # list of destroyer coordinates is appended to larger ships_list
    return ships_list


def place_submarine(ships_list):

    """
    function randomly selects a point, then checks which direction to point the ship, and places the submarine
    in the top half of the board for the user to fire at
    :param ships_list: list containing lists of carrier, battleship, and destroyer coordinates
    :return: ships_list with submarine coordinates appended to it
    """

    # random x,y coordinates are chosen
    x1 = random.randint(0, 9)
    y1 = random.randint(0, 9)
    ship = []

    # all directions are initialized as True
    up = True
    down = True
    left = True
    right = True

    # checks left/right walls
    if x1 < 2:
        left = False
    elif x1 > 7:
        right = False
    elif 2 <= x1 <= 7:
        left = False

    # checks top/bottom walls
    if y1 < 2:
        up = False
    elif y1 > 7:
        down = False
    elif 2 <= y1 <= 7:
        up = False

    # based on allowable directions, corresponding points are added to the ship list
    if up:
        y2 = y1 - 1
        y3 = y2 - 1

        ship = [(x1, y1), (x1, y2), (x1, y3)]
    elif right:
        x2 = x1 + 1
        x3 = x2 + 1

        ship = [(x1, y1), (x2, y1), (x3, y1)]
    elif down:
        y2 = y1 + 1
        y3 = y2 + 1
        ship = [(x1, y1), (x1, y2), (x1, y3)]

    elif left:
        x2 = x1 - 1
        x3 = x2 - 1

        ship = [(x1, y1), (x2, y1), (x3, y1)]

    # checks for overlaps with existing ships
    for i in ship:
        for x in ships_list:
            if i in x:
                return place_submarine(ships_list) # if overlaps individual ship is replaced until successful

    ships_list.append(ship) # list of submarine coordinates is appended to larger ships_list
    return ships_list


def place_patrol(ships_list):

    """
    function randomly selects a point, then checks which direction to point the ship, and places the patrol boat
    in the top half of the board for the user to fire at
    :param ships_list: list containing list of carrier, battleship, destroyer, and submarine coordinates
    :return: ships_list with patrol boat coordinates appended to it
    """

    # random x,y coordinates chosen
    x1 = random.randint(0, 9)
    y1 = random.randint(0, 9)
    ship = []

    # all directions initialized as True
    up = True
    down = True
    left = True
    right = True

    # checks left/right walls
    if x1 < 1:
        left = False
    elif x1 > 1:
        right = False
    elif 1 <= x1 <= 8:
        left = False

    # checks top/bottom walls
    if y1 < 1:
        up = False
    elif y1 > 8:
        down = False
    elif 1 <= y1 <= 8:
        up = False

    # based on allowable directions, corresponding points are added to the ship list
    if up:
        y2 = y1 - 1

        ship = [(x1, y1), (x1, y2)]
    elif right:
        x2 = x1 + 1


        ship = [(x1, y1), (x2, y1)]
    elif down:
        y2 = y1 + 1

        ship = [(x1, y1), (x1, y2)]

    elif left:
        x2 = x1 - 1

        ship = [(x1, y1), (x2, y1)]

    # checks for overlap with existing ships
    for i in ship:
        for x in ships_list:
            if i in x:
                return place_patrol(ships_list) # if overlaps individual ship is replaced until successful

    ships_list.append(ship) # list of coordinates for patrol boat are appended to larger ships_list
    return ships_list


# clicked = [] # holds coordinates of all cells clicked
#
#
# def clicked_cell(x, y):
#
#     """
#     appends coordinates to
#     :param x:
#     :param y:
#     :return:
#     """
#
#     for i in range(len(clicked)):
#         if i == (x, y):
#             return True
#         elif i < len(clicked):
#             i += 1
#         else:
#             clicked.append((x, y))
#             return False


def ship_board_check(x, y):
    if 10 <= y <= 19:
        return True
    else:
        return False


def computer_shot(hit_list, miss_list):

    """
    function chooses two random integers in range of bottom half of board and sends them as the computer's shot
    :param hit_list: list of coordinates that are hits
    :param miss_list: list of coordinates that are misses
    :return: x,y value of cell in bottom half of board
    """

    # x and y values chosen in range of bottom half of board
    x1 = random.randint(0, 9)
    y1 = random.randint(10, 19)

    if (x1, y1) not in hit_list and (x1, y1) not in miss_list: # random cell checked against already guessed cells
        shot = (x1, y1)
    else: # if shot is at already guessed cell, new coordinates are chosen until successful
        shot = computer_shot(hit_list, miss_list)
    return shot


all_ships = [] # creates empty list to add ship coords to

# calls functions to randomly place ships in top half of board for the user to fire at
list1 = place_carrier(all_ships)
list2 = place_battleship(list1)
list3 = place_destroyer(list2)
list4 = place_submarine(list3)
final_list = place_patrol(list4) # list containing 5 lists, each with coordinates for the ships

# specifies which list within final_list corresponds to which ship
carrier = final_list[0]
battleship = final_list[1]
destroyer = final_list[2]
submarine = final_list[3]
patrol_boat = final_list[4]