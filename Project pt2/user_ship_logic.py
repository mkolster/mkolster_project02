ships_list = []
#
#
# def user_carrier(x, y):
#
#     """
#     function sets rules to allow user to place their carrier, ensuring that it does not extend beyond the sides.
#     :param x: x coordinate
#     :param y: y coordinate
#     :return:
#     """
#
#     ship = []
#
#     up = True
#     down = True
#     left = True
#     right = True
#
#     if x < 4:
#         left = False
#     elif x > 5:
#         right = False
#     elif 4 <= x <= 5:
#         right = False
#
#     if y < 4:
#         up = False
#     elif y > 5:
#         down = False
#     elif 4 <= y <= 5:
#         down = False
#
#     if up:
#         y2 = y - 1
#         y3 = y2 - 1
#         y4 = y3 - 1
#         y5 = y4 - 1
#
#         ship = [(x, y), (x, y2), (x, y3), (x, y4), (x, y5)]
#     elif right:
#         x2 = x + 1
#         x3 = x2 + 1
#         x4 = x3 + 1
#         x5 = x4 + 1
#
#         ship = [(x, y), (x2, y), (x3, y), (x4, y), (x5, y)]
#     elif down:
#         y2 = y + 1
#         y3 = y2 + 1
#         y4 = y3 + 1
#         y5 = y4 + 1
#         ship = [(x, y), (x, y2), (x, y3), (x, y4), (x, y5)]
#
#     elif left:
#         x2 = x - 1
#         x3 = x2 - 1
#         x4 = x3 - 1
#         x5 = x4 - 1
#
#         ship = [(x, y), (x2, y), (x3, y), (x4, y), (x5, y)]
#
#     ships_list.append(ship)
#     return ship
#
#
#
# def user_battleship(x, y):
#     ship = []
#
#     up = True
#     down = True
#     left = True
#     right = True
#
#     if x < 3:
#         left = False
#     elif x > 6:
#         right = False
#     elif 3 <= x <= 6:
#         left = False
#
#     if y < 3:
#         up = False
#     elif y > 6:
#         down = False
#     elif 3 <= y <= 6:
#         up = False
#
#     if up:
#         y2 = y - 1
#         y3 = y2 - 1
#         y4 = y3 - 1
#
#         ship = [(x, y), (x, y2), (x, y3), (x, y4)]
#     elif right:
#         x2 = x + 1
#         x3 = x2 + 1
#         x4 = x3 + 1
#
#         ship = [(x, y), (x2, y), (x3, y), (x4, y)]
#     elif down:
#         y2 = y + 1
#         y3 = y2 + 1
#         y4 = y3 + 1
#         ship = [(x, y), (x, y2), (x, y3), (x, y4)]
#
#     elif left:
#         x2 = x - 1
#         x3 = x2 - 1
#         x4 = x3 - 1
#
#         ship = [(x, y), (x2, y), (x3, y), (x4, y)]
#
#     for i in ship:
#         for x in ships_list:
#             if i in x:
#                 print('overlap battleship')
#
#     print(ship, ships_list)
#     ships_list.append(ship)
#     return ship
#
#
# def user_destroyer(x, y):
#     ship = []
#
#     up = True
#     down = True
#     left = True
#     right = True
#
#     if x < 2:
#         left = False
#     elif x > 7:
#         right = False
#     elif 2 <= x <= 7:
#         left = False
#
#     if y < 2:
#         up = False
#     elif y > 7:
#         down = False
#     elif 2 <= y <= 7:
#         up = False
#
#     if up:
#         y2 = y - 1
#         y3 = y2 - 1
#
#         ship = [(x, y), (x, y2), (x, y3)]
#     elif right:
#         x2 = x + 1
#         x3 = x2 + 1
#
#         ship = [(x, y), (x2, y), (x3, y)]
#     elif down:
#         y2 = y + 1
#         y3 = y2 + 1
#         ship = [(x, y), (x, y2), (x, y3)]
#
#     elif left:
#         x2 = x - 1
#         x3 = x2 - 1
#
#         ship = [(x, y), (x2, y), (x3, y)]
#
#     for i in ship:
#         for x in ships_list:
#             if i in x:
#                 print('overlap destroyer')
#
#     ships_list.append(ship)
#     print(ship, ships_list)
#
#     return ship
#
#
# def user_submarine(x, y):
#     ship = []
#
#     up = True
#     down = True
#     left = True
#     right = True
#
#     if x < 2:
#         left = False
#     elif x > 7:
#         right = False
#     elif 2 <= x <= 7:
#         left = False
#
#     if y < 2:
#         up = False
#     elif y > 7:
#         down = False
#     elif 2 <= y <= 7:
#         up = False
#
#     if up:
#         y2 = y - 1
#         y3 = y2 - 1
#
#         ship = [(x, y), (x, y2), (x, y3)]
#     elif right:
#         x2 = x + 1
#         x3 = x2 + 1
#
#         ship = [(x, y), (x2, y), (x3, y)]
#     elif down:
#         y2 = y + 1
#         y3 = y2 + 1
#         ship = [(x, y), (x, y2), (x, y3)]
#
#     elif left:
#         x2 = x - 1
#         x3 = x2 - 1
#
#         ship = [(x, y), (x2, y), (x3, y)]
#
#     for i in ship:
#         for x in ships_list:
#             if i in x:
#                 print('overlap destroyer')
#
#     ships_list.append(ship)
#     print(ship, ships_list)
#     return ship
#
#
# def user_patrol(x, y):
#     ship = []
#
#     up = True
#     down = True
#     left = True
#     right = True
#
#     if x < 1:
#         left = False
#     elif x > 1:
#         right = False
#     elif 1 <= x <= 8:
#         left = False
#
#     if y < 1:
#         up = False
#     elif y > 8:
#         down = False
#     elif 1 <= y <= 8:
#         up = False
#
#     if up:
#         y2 = y - 1
#
#         ship = [(x, y), (x, y2)]
#     elif right:
#         x2 = x + 1
#
#         ship = [(x, y), (x2, y)]
#     elif down:
#         y2 = y + 1
#
#         ship = [(x, y), (x, y2)]
#
#     elif left:
#         x2 = x - 1
#
#         ship = [(x, y), (x2, y)]
#
#     for i in ship:
#         for x in ships_list:
#             if i in x:
#                 print('overlap patrol')
#
#     ships_list.append(ship)
#     print(ship, ships_list)
#     return ship


def user_carrier_check_dir(x, y):

    up = True
    down = True
    left = True
    right = True

    if x < 4:
        left = False
    elif x > 5:
        right = False
    elif 4 <= x <= 5:
        right = False

    if y < 14:
        up = False
    elif y > 15:
        down = False
    elif 14 <= y <= 15:
        up = False

    if up:
        return 1
    elif right:
        return 2
    elif down:
        return 3
    elif left:
        return 4
    

def user_battleship_check_dir(x, y, user_ships):
    up = True
    down = True
    left = True
    right = True

    if x < 3:
        left = False
    elif x > 6:
        right = False
    elif 3 <= x <= 6:
        left = False

    if y < 13:
        up = False
    elif y > 16:
        down = False
    elif 13 <= y <= 16:
        up = False

    for i in range(1, 4):
        if (x + i, y) in user_ships:
            right = False
        if (x - i, y) in user_ships:
            left = False
        if (x, y + i) in user_ships:
            down = False
        if (x, y - i) in user_ships:
            up = False


    if up:
        return 1
    elif right:
        return 2
    elif down:
        return 3
    elif left:
        return 4
    

def user_destroyer_check_dir(x, y, user_ships):
    up = True
    down = True
    left = True
    right = True

    if x < 2:
        left = False
    elif x > 7:
        right = False
    elif 2 <= x <= 7:
        left = False

    if y < 12:
        up = False
    elif y > 17:
        down = False
    elif 12 <= y <= 17:
        up = False

    for i in range(1, 3):
        if (x + i, y) in user_ships:
            right = False
        if (x - i, y) in user_ships:
            left = False
        if (x, y + i) in user_ships:
            down = False
        if (x, y - i) in user_ships:
            up = False

    if up:
        return 1
    elif right:
        return 2
    elif down:
        return 3
    elif left:
        return 4
    

def user_submarine_check_dir(x, y, user_ships):
    up = True
    down = True
    left = True
    right = True

    if x < 2:
        left = False
    elif x > 7:
        right = False
    elif 2 <= x <= 7:
        left = False

    if y < 12:
        up = False
    elif y > 17:
        down = False
    elif 12 <= y <= 17:
        up = False

    for i in range(1, 3):
        if (x + i, y) in user_ships:
            right = False
        if (x - i, y) in user_ships:
            left = False
        if (x, y + i) in user_ships:
            down = False
        if (x, y - i) in user_ships:
            up = False

    if up:
        return 1
    elif right:
        return 2
    elif down:
        return 3
    elif left:
        return 4
    

def user_patrol_check_dir(x, y, user_ships):
    up = True
    down = True
    left = True
    right = True

    if x < 1:
        left = False
    elif x > 1:
        right = False
    elif 1 <= x <= 8:
        left = False

    if y < 11:
        up = False
    elif y > 18:
        down = False
    elif 11 <= y <= 18:
        up = False

    for i in range(1, 2):
        if (x + i, y) in user_ships:
            right = False
        if (x - i, y) in user_ships:
            left = False
        if (x, y + i) in user_ships:
            down = False
        if (x, y - i) in user_ships:
            up = False

    if up:
        return 1
    elif right:
        return 2
    elif down:
        return 3
    elif left:
        return 4