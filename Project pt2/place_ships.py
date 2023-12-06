# import pygame
# import grid2
# import user_ship_logic
# import control_fires
# import testing
# import sys
#
# class UserShips:
#     def __init__(self):
#         self.clicked = False
#
# def user_ships_grid():
#     pygame.mixer.init()
#
#     hit_sound = pygame.mixer.Sound("hit_sound.mp3")
#     miss_sound = pygame.mixer.Sound("miss_sound.mp3")
#
#     grid_width = 30
#     player_board = [[UserShips() for _ in range(grid_width)] for _ in range(0, 600)]
#
#     pygame.init()
#     window = pygame.display.set_mode((600, 600))
#
#     clock = pygame.time.Clock()
#
#     run = True
#     ship_counter = 0
#     while run:
#
#         clock.tick(100)
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:
#
#                     if 0 <= event.pos[1] <= 600:
#                         row = event.pos[1] // 60
#                         col = event.pos[0] // 60
#                         player_board[row][col].clicked = True
#                         grid2.print_cell(col, row)
#                         ship_counter += 1
#
#
#         window.fill(0)
#
#         for iy, rowOfCells in enumerate(player_board):
#             for ix, cell in enumerate(rowOfCells):
#                 if not cell.clicked:
#                     color = 'gray'
#                 elif cell.clicked:
#                     color = (50, 50, 50)
#
#                 pygame.draw.rect(window, color, (ix * 60 + 1.5, iy * 60 + 1.5, 54, 54))
#
#         pygame.display.flip()
#
#     pygame.quit()
#     exit()
#
#
#
#
#     #create list with all points selected by user and return them to gridsquare function in control_fires.py
#     #make sure that y values have 9 added to them in order to place them in the correct place on the grid otherwise
#     # it won't highlight