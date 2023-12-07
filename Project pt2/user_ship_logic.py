

ships_list = []

def user_carrier(x1, y1):
    ship = []

    up = True
    down = True
    left = True
    right = True

    if x1 < 4:
        left = False
    elif x1 > 5:
        right = False
    elif 4 <= x1 <= 5:
        right = False

    if y1 < 4:
        up = False
    elif y1 > 5:
        down = False
    elif 4 <= y1 <= 5:
        down = False

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
    print(ship)
    ships_list.append(ship)
    return ship

def user_battleship(x1, y1):
    ship = []

    up = True
    down = True
    left = True
    right = True

    if x1 < 3:
        left = False
    elif x1 > 6:
        right = False
    elif 3 <= x1 <= 6:
        left = False

    if y1 < 3:
        up = False
    elif y1 > 6:
        down = False
    elif 3 <= y1 <= 6:
        up = False

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

    for i in ship:
        for x in ships_list:
            if i in x:
                print('overlap battleship')

    print(ship, ships_list)
    ships_list.append(ship)
    return ship
def user_destroyer(x1, y1):
    ship = []

    up = True
    down = True
    left = True
    right = True

    if x1 < 2:
        left = False
    elif x1 > 7:
        right = False
    elif 2 <= x1 <= 7:
        left = False

    if y1 < 2:
        up = False
    elif y1 > 7:
        down = False
    elif 2 <= y1 <= 7:
        up = False

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

    for i in ship:
        for x in ships_list:
            if i in x:
                print('overlap destroyer')

    ships_list.append(ship)
    print(ship, ships_list)

    return ship

def user_submarine(x1, y1):
    ship = []

    up = True
    down = True
    left = True
    right = True

    if x1 < 2:
        left = False
    elif x1 > 7:
        right = False
    elif 2 <= x1 <= 7:
        left = False

    if y1 < 2:
        up = False
    elif y1 > 7:
        down = False
    elif 2 <= y1 <= 7:
        up = False

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

    for i in ship:
        for x in ships_list:
            if i in x:
                print('overlap destroyer')

    ships_list.append(ship)
    print(ship, ships_list)
    return ship

def user_patrol(x1, y1):
    ship = []

    up = True
    down = True
    left = True
    right = True

    if x1 < 1:
        left = False
    elif x1 > 1:
        right = False
    elif 1 <= x1 <= 8:
        left = False

    if y1 < 1:
        up = False
    elif y1 > 8:
        down = False
    elif 1 <= y1 <= 8:
        up = False

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

    for i in ship:
        for x in ships_list:
            if i in x:
                print('overlap patrol')

    ships_list.append(ship)
    print(ship, ships_list)
    return ship

def user_carrier_check_dir(x1, y1):

    up = True
    down = True
    left = True
    right = True

    if x1 < 4:
        left = False
    elif x1 > 5:
        right = False
    elif 4 <= x1 <= 5:
        right = False

    if y1 < 14:
        up = False
    elif y1 > 15:
        down = False
    elif 14 <= y1 <= 15:
        up = False

    if up:
        return 1
    elif right:
        return 2
    elif down:
        return 3
    elif left:
        return 4

def user_battleship_check_dir(x1, y1, user_ships):
    up = True
    down = True
    left = True
    right = True

    if x1 < 3:
        left = False
    elif x1 > 6:
        right = False
    elif 3 <= x1 <= 6:
        left = False

    if y1 < 13:
        up = False
    elif y1 > 16:
        down = False
    elif 13 <= y1 <= 16:
        up = False

    for i in range(1, 4):
        if (x1 + i, y1) in user_ships:
            right = False
        if (x1 - i, y1) in user_ships:
            left = False
        if (x1, y1 + i) in user_ships:
            down = False
        if (x1, y1 - i) in user_ships:
            up = False


    if up:
        return 1
    elif right:
        return 2
    elif down:
        return 3
    elif left:
        return 4

def user_destroyer_check_dir(x1, y1, user_ships):
    up = True
    down = True
    left = True
    right = True

    if x1 < 2:
        left = False
    elif x1 > 7:
        right = False
    elif 2 <= x1 <= 7:
        left = False

    if y1 < 12:
        up = False
    elif y1 > 17:
        down = False
    elif 12 <= y1 <= 17:
        up = False

    for i in range(1, 3):
        if (x1 + i, y1) in user_ships:
            right = False
        if (x1 - i, y1) in user_ships:
            left = False
        if (x1, y1 + i) in user_ships:
            down = False
        if (x1, y1 - i) in user_ships:
            up = False

    if up:
        return 1
    elif right:
        return 2
    elif down:
        return 3
    elif left:
        return 4

def user_submarine_check_dir(x1, y1, user_ships):
    up = True
    down = True
    left = True
    right = True

    if x1 < 2:
        left = False
    elif x1 > 7:
        right = False
    elif 2 <= x1 <= 7:
        left = False

    if y1 < 12:
        up = False
    elif y1 > 17:
        down = False
    elif 12 <= y1 <= 17:
        up = False

    for i in range(1, 3):
        if (x1 + i, y1) in user_ships:
            right = False
        if (x1 - i, y1) in user_ships:
            left = False
        if (x1, y1 + i) in user_ships:
            down = False
        if (x1, y1 - i) in user_ships:
            up = False

    if up:
        return 1
    elif right:
        return 2
    elif down:
        return 3
    elif left:
        return 4

def user_patrol_check_dir(x1, y1, user_ships):
    up = True
    down = True
    left = True
    right = True

    if x1 < 1:
        left = False
    elif x1 > 1:
        right = False
    elif 1 <= x1 <= 8:
        left = False

    if y1 < 11:
        up = False
    elif y1 > 18:
        down = False
    elif 11 <= y1 <= 18:
        up = False

    for i in range(1, 2):
        if (x1 + i, y1) in user_ships:
            right = False
        if (x1 - i, y1) in user_ships:
            left = False
        if (x1, y1 + i) in user_ships:
            down = False
        if (x1, y1 - i) in user_ships:
            up = False

    if up:
        return 1
    elif right:
        return 2
    elif down:
        return 3
    elif left:
        return 4