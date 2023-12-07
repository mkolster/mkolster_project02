import random

# patrol_correct = []
# sub_correct = []
# carrier_correct = []
# destroyer_correct = []
# battleship_correct = []
# incorrect = []

check = False


def cell_check(x, y):
    if check_patrol(x, y):
        # patrol_correct.append((x, y))
        return True

    elif check_submarine(x, y):
        # sub_correct.append((x, y))
        return True

    elif check_battleship(x, y):
        # battleship_correct.append((x,y))
        return True

    elif check_carrier(x, y):
        # carrier_correct.append((x, y))
        return True

    elif check_destroyer(x, y):
        # destroyer_correct.append((x, y))
        return True
    else:
        # incorrect.append((x, y))
        return False


def check_patrol(x, y):
    for i in range(len(patrol_boat)):
        if patrol_boat[i] == (x, y):
            if clicked_cell(x, y):
                return False
            else:
                return True
        elif i < 2:
            i += 1
        else:
            return False


def check_submarine(x, y):
    for i in range(len(submarine)):
        if submarine[i] == (x, y):
            return True
        elif i < 3:
            i += 1
        else:
            return False


def check_carrier(x, y):
    for i in range(len(carrier)):
        if carrier[i] == (x, y):
            return True
        elif i < 5:
            i += 1
        else:
            return False


def check_destroyer(x, y):
    for i in range(len(destroyer)):
        if destroyer[i] == (x, y):
            return True
        elif i < 3:
            i += 1
        else:
            return False


def check_battleship(x, y):
    for i in range(len(battleship)):
        if battleship[i] == (x, y):
            return True
        elif i < 4:
            i += 1
        else:
            return False


def place_carrier(ships_list):
    x1 = random.randint(0, 9)
    y1 = random.randint(0, 9)
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

    ships_list.append(ship)

    return ships_list


def place_battleship(ships_list):
    x1 = random.randint(0, 9)
    y1 = random.randint(0, 9)
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
                return place_battleship(ships_list)

    ships_list.append(ship)
    return ships_list


def place_destroyer(ships_list):
    x1 = random.randint(0, 9)
    y1 = random.randint(0, 9)
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
                return place_destroyer(ships_list)

    ships_list.append(ship)
    return ships_list


def place_submarine(ships_list):
    x1 = random.randint(0, 9)
    y1 = random.randint(0, 9)
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
                print('overlap sub')
                return place_submarine(ships_list)

    ships_list.append(ship)
    return ships_list


def place_patrol(ships_list):
    x1 = random.randint(0, 9)
    y1 = random.randint(0, 9)
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
                return place_patrol(ships_list)

    ships_list.append(ship)
    return ships_list


clicked = []


def clicked_cell(x, y):
    for i in range(len(clicked)):
        if i == (x, y):
            return True
        elif i < len(clicked):
            i += 1
        else:
            clicked.append((x, y))
            return False


def ship_board_check(x, y):
    if 10 <= y <= 19:
        return True
    else:
        return False


def computer_shot(hit_list, miss_list):
    x1 = random.randint(0, 9)
    y1 = random.randint(10, 19)

    if (x1, y1) not in hit_list and (x1, y1) not in miss_list:
        shot = (x1, y1)
    else:
        shot = computer_shot(hit_list, miss_list)
        print('no shot')
    return shot


all_ships = []
list1 = place_carrier(all_ships)
list2 = place_battleship(list1)
list3 = place_destroyer(list2)
list4 = place_submarine(list3)
final_list = place_patrol(list4)
print(final_list)

carrier = final_list[0]
battleship = final_list[1]
destroyer = final_list[2]
submarine = final_list[3]
patrol_boat = final_list[4]