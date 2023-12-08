ships_list = []


def user_carrier_check_dir(x, y):

    """
    function checks the allowable directions that the carrier can go based on a clicked cell
    :param x: x coordinate
    :param y: y coordinate
    :return: int corresponding to direction
    """

    # all directions are initialized True
    up = True
    down = True
    left = True
    right = True

    # checks left/right walls
    if x < 4:
        left = False
    elif x > 5:
        right = False
    elif 4 <= x <= 5:
        right = False

    # checks top/bottom walls
    if y < 14:
        up = False
    elif y > 15:
        down = False
    elif 14 <= y <= 15:
        up = False

    # based on allowable directions a value is returned corresponding to that direction (1-4, clockwise)
    if up:
        return 1
    elif right:
        return 2
    elif down:
        return 3
    elif left:
        return 4
    

def user_battleship_check_dir(x, y, user_ships):
    """
    function checks the allowable directions that the battleship can go based on a clicked cell
    :param x: x coordinate
    :param y: y coordinate
    :param user_ships: list of coordinates for all other ships
    :return: int corresponding to direction
    """

    # all directions are initialized to True
    up = True
    down = True
    left = True
    right = True

    # checks left/right walls
    if x < 3:
        left = False
    elif x > 6:
        right = False
    elif 3 <= x <= 6:
        left = False

    # checks top/bottom walls
    if y < 13:
        up = False
    elif y > 16:
        down = False
    elif 13 <= y <= 16:
        up = False

    # checks for overlaps with existing ships and attempts to change orientation to avoid overlap
    for i in range(1, 4):
        if (x + i, y) in user_ships:
            right = False
        if (x - i, y) in user_ships:
            left = False
        if (x, y + i) in user_ships:
            down = False
        if (x, y - i) in user_ships:
            up = False

    # based on allowable directions a value is returned corresponding to that direction (1-4, clockwise)
    if up:
        return 1
    elif right:
        return 2
    elif down:
        return 3
    elif left:
        return 4
    

def user_destroyer_check_dir(x, y, user_ships):
    """
    function checks the allowable directions that the destroyer can go based on a clicked cell
    :param x: x coordinate
    :param y: y coordinate
    :param user_ships: list of coordinates for all other ships
    :return: int corresponding to direction
    """

    # initializes all directions to True
    up = True
    down = True
    left = True
    right = True

    # checks left/right walls
    if x < 2:
        left = False
    elif x > 7:
        right = False
    elif 2 <= x <= 7:
        left = False

    # checks top/bottom walls
    if y < 12:
        up = False
    elif y > 17:
        down = False
    elif 12 <= y <= 17:
        up = False

    # checks for overlaps with existing ships and attempts to change orientation to avoid overlap
    for i in range(1, 3):
        if (x + i, y) in user_ships:
            right = False
        if (x - i, y) in user_ships:
            left = False
        if (x, y + i) in user_ships:
            down = False
        if (x, y - i) in user_ships:
            up = False

    # based on allowable directions a value is returned corresponding to that direction (1-4, clockwise)
    if up:
        return 1
    elif right:
        return 2
    elif down:
        return 3
    elif left:
        return 4
    

def user_submarine_check_dir(x, y, user_ships):
    """
        function checks the allowable directions that the submarine can go based on a clicked cell
        :param x: x coordinate
        :param y: y coordinate
        :param user_ships: list of coordinates for all other ships
        :return: int corresponding to direction
        """

    # all values are initialized to True
    up = True
    down = True
    left = True
    right = True

    # checks left/right walls
    if x < 2:
        left = False
    elif x > 7:
        right = False
    elif 2 <= x <= 7:
        left = False

    # checks top/bottom walls
    if y < 12:
        up = False
    elif y > 17:
        down = False
    elif 12 <= y <= 17:
        up = False

    # checks for overlaps with existing ships and attempts to change orientation to avoid overlap
    for i in range(1, 3):
        if (x + i, y) in user_ships:
            right = False
        if (x - i, y) in user_ships:
            left = False
        if (x, y + i) in user_ships:
            down = False
        if (x, y - i) in user_ships:
            up = False

    # based on allowable directions a value is returned corresponding to that direction (1-4, clockwise)
    if up:
        return 1
    elif right:
        return 2
    elif down:
        return 3
    elif left:
        return 4
    

def user_patrol_check_dir(x, y, user_ships):
    """
        function checks the allowable directions that the patrol boat can go based on a clicked cell
        :param x: x coordinate
        :param y: y coordinate
        :param user_ships: list of coordinates for all other ships
        :return: int corresponding to direction
        """

    # initializes all directions to True
    up = True
    down = True
    left = True
    right = True

    # checks left/right walls
    if x < 1:
        left = False
    elif x > 1:
        right = False
    elif 1 <= x <= 8:
        left = False

    # checks top/bottom walls
    if y < 11:
        up = False
    elif y > 18:
        down = False
    elif 11 <= y <= 18:
        up = False

    # checks for overlaps with existing ships and attempts to change orientation to avoid overlap
    for i in range(1, 2):
        if (x + i, y) in user_ships:
            right = False
        if (x - i, y) in user_ships:
            left = False
        if (x, y + i) in user_ships:
            down = False
        if (x, y - i) in user_ships:
            up = False

    # based on allowable directions a value is returned corresponding to that direction (1-4, clockwise)
    if up:
        return 1
    elif right:
        return 2
    elif down:
        return 3
    elif left:
        return 4
