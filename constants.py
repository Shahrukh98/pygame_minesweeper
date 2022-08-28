WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

# import pygame


# pygame.init()
# screen: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
# font = pygame.font.SysFont('arialblack',40)

# click = False
# on_menu = True
# pause=False
# RUN = [True]

# m = (0,0)
# MAIN_MENU_STATE = ["MAIN"]

# while RUN[0]:

#     screen.fill((58,78,91))
    
#     if click:
#         print(m)
#         print(m[0])
#         print(m[1])

#     click=False
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             RUN[0] = False

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 1:
#                 click = True

#         if event.type == pygame.MOUSEMOTION:
#             m = pygame.mouse.get_pos() 

#         if event.type == pygame.QUIT:
#             RUN[0] = False

#     pygame.display.update()