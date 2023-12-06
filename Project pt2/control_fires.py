import pygame

import user_fires_logic
import menu_result_display
import sys

import user_ship_logic


class Cell1:
    def __init__(self):
        self.clicked = False


def gridsquare(player_name):
    pygame.mixer.init()

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
    counter1 = 0
    counter2 = 0
    mouse_click = 0
    computer_hit = []
    computer_miss = []
    while run:
        clock.tick(100)
        comp_shot = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT or counter1 == 17 or len(computer_hit) == 17:
                if counter1 == 17:
                    kill_count = count_red_squares(player_board)
                    return menu_result_display.ending_screen(kill_count, player_name, 'won!')
                if len(computer_hit) == 17:
                    kill_count = count_red_squares(player_board)
                    return menu_result_display.ending_screen(kill_count, player_name, 'lost')
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:


                    if 0 <= event.pos[1] <= 300 and mouse_click >= 5:
                        row = event.pos[1] // 30
                        col = event.pos[0] // 30
                        player_board[row][col].clicked = True
                        user_fires_logic.print_cell(col, row)

                        if user_fires_logic.cell_check(col, row) and (col, row) not in clicker_check:
                            hit_sound.play()
                            counter1 += 1
                            comp_shot = user_fires_logic.computer_shot(computer_hit, computer_miss)
                            x = comp_shot[0]
                            y = comp_shot[1]
                            if (x, y) in user_ships:
                                computer_hit.append((x, y))
                                print(computer_hit)
                            else:
                                computer_miss.append((x, y))
                                print(computer_miss)

                        elif not user_fires_logic.cell_check(col, row) and (col, row) not in clicker_check:
                            miss_sound.play()

                            comp_shot = user_fires_logic.computer_shot(computer_hit, computer_miss)
                            x = comp_shot[0]
                            y = comp_shot[1]
                            if (x, y) in user_ships:
                                computer_hit.append((x, y))
                                print(computer_hit)
                            else:
                                computer_miss.append((x, y))
                                print(computer_miss)



                    if 300 <= event.pos[1] <= 600 and mouse_click <= 5:
                        mouse_click += 1
                        row = event.pos[1] // 30
                        col = event.pos[0] // 30
                        if mouse_click <= 5:
                            player_board[row][col].clicked = True
                        else:
                            player_board[row][col].clicked = False
                        if mouse_click == 1:
                            direction = user_ship_logic.user_carrier_check_dir(col, row)
                            ship_set.play()
                            if direction == 1:
                                player_board[row - 1][col].clicked = True
                                player_board[row - 2][col].clicked = True
                                player_board[row - 3][col].clicked = True
                                player_board[row - 4][col].clicked = True
                            elif direction == 2:
                                player_board[row][col + 1].clicked = True
                                player_board[row][col + 2].clicked = True
                                player_board[row][col + 3].clicked = True
                                player_board[row][col + 4].clicked = True
                            elif direction == 3:
                                player_board[row + 1][col].clicked = True
                                player_board[row + 2][col].clicked = True
                                player_board[row + 3][col].clicked = True
                                player_board[row + 4][col].clicked = True
                            elif direction == 4:
                                player_board[row][col - 1].clicked = True
                                player_board[row][col - 2].clicked = True
                                player_board[row][col - 3].clicked = True
                                player_board[row][col - 4].clicked = True
                        elif mouse_click == 2:
                            direction = user_ship_logic.user_battleship_check_dir(col, row, user_ships)
                            ship_set.play()
                            if direction == 1:
                                player_board[row - 1][col].clicked = True
                                player_board[row - 2][col].clicked = True
                                player_board[row - 3][col].clicked = True

                            elif direction == 2:
                                player_board[row][col + 1].clicked = True
                                player_board[row][col + 2].clicked = True
                                player_board[row][col + 3].clicked = True

                            elif direction == 3:
                                player_board[row + 1][col].clicked = True
                                player_board[row + 2][col].clicked = True
                                player_board[row + 3][col].clicked = True

                            elif direction == 4:
                                player_board[row][col - 1].clicked = True
                                player_board[row][col - 2].clicked = True
                                player_board[row][col - 3].clicked = True
                            else:
                                player_board[row][col].clicked = False
                                mouse_click -= 1

                        elif mouse_click == 3:
                            direction = user_ship_logic.user_destroyer_check_dir(col, row, user_ships)
                            ship_set.play()
                            if direction == 1:
                                player_board[row - 1][col].clicked = True
                                player_board[row - 2][col].clicked = True

                            elif direction == 2:
                                player_board[row][col + 1].clicked = True
                                player_board[row][col + 2].clicked = True

                            elif direction == 3:
                                player_board[row + 1][col].clicked = True
                                player_board[row + 2][col].clicked = True

                            elif direction == 4:
                                player_board[row][col - 1].clicked = True
                                player_board[row][col - 2].clicked = True
                            else:
                                player_board[row][col].clicked = False
                                mouse_click -= 1

                        elif mouse_click == 4:
                            direction = user_ship_logic.user_submarine_check_dir(col, row, user_ships)
                            ship_set.play()
                            if direction == 1:
                                player_board[row - 1][col].clicked = True
                                player_board[row - 2][col].clicked = True

                            elif direction == 2:
                                player_board[row][col + 1].clicked = True
                                player_board[row][col + 2].clicked = True

                            elif direction == 3:
                                player_board[row + 1][col].clicked = True
                                player_board[row + 2][col].clicked = True

                            elif direction == 4:
                                player_board[row][col - 1].clicked = True
                                player_board[row][col - 2].clicked = True
                            else:
                                player_board[row][col].clicked = False
                                mouse_click -= 1

                        elif mouse_click == 5:
                            direction = user_ship_logic.user_patrol_check_dir(col, row, user_ships)
                            ship_set.play()
                            if direction == 1:
                                player_board[row - 1][col].clicked = True

                            elif direction == 2:
                                player_board[row][col + 1].clicked = True

                            elif direction == 3:
                                player_board[row + 1][col].clicked = True

                            elif direction == 4:
                                player_board[row][col - 1].clicked = True
                            else:
                                player_board[row][col].clicked = False
                                mouse_click -= 1

                        user_fires_logic.print_cell(col, row)



        clicker_check = []
        user_ships = []




        window.fill(0)

        for iy, rowOfCells in enumerate(player_board):
            for ix, cell in enumerate(rowOfCells):
                if (ix, iy) not in clicker_check:
                    if cell.clicked and user_fires_logic.cell_check(ix, iy) and not user_fires_logic.ship_board_check(ix, iy):
                        clicker_check.append((ix, iy))
                        color = 'red'
                    elif cell.clicked and not user_fires_logic.cell_check(ix, iy) and not user_fires_logic.ship_board_check(ix, iy):
                        clicker_check.append((ix, iy))
                        color = 'white'
                if not cell.clicked and not user_fires_logic.ship_board_check(ix, iy):
                    color = (0, 71, 171)

                if (ix, iy) in computer_hit:
                    color = 'red'
                elif (ix, iy) in computer_miss:
                    color = 'white'

                elif cell.clicked and user_fires_logic.ship_board_check(ix, iy):
                    color = (50, 50, 50)
                    user_ships.append((ix, iy))

                elif not cell.clicked and user_fires_logic.ship_board_check(ix, iy):
                    color = 'gray'

                # if (ix, iy) in user_ships and (ix, iy) not in computer_hit and computer_miss and user_fires_logic.ship_board_check(ix, iy):
                # if not cell.clicked and comp_shot and not comp_hit_check(ix, iy, user_ships):
                #     color = 'white'
                # elif cell.clicked and comp_shot and comp_hit_check(ix, iy, user_ships):
                #     color = 'red'
                #     cell.clicked = False
                # elif not cell.clicked and not comp_shot and user_fires_logic.ship_board_check(ix, iy):
                #     color = 'gray'

                pygame.draw.rect(window, color, (ix*30+1.5, iy*30+1.5, 27, 27))




        pygame.display.flip()

    pygame.quit()
    exit()



def count_red_squares(player_board):
    red_count = 0
    patrol_kill = 0
    battleship_kill = 0
    destroyer_kill = 0
    carrier_kill = 0
    sub_kill = 0
    boat_kills = ['', '', '', '', '']
    for row in player_board:
        for cell in row:
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
    if (x, y) in user_ships:
        return True
    else:
        return False

