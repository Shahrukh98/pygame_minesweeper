from dataclasses import dataclass, field
from enum import Enum
from time import sleep
from typing import List
import pygame
from constants import WINDOW_HEIGHT, WINDOW_WIDTH
from main_menu import MainMenu
from ui.button import Button

pygame.init()
@dataclass
class Minesweeper:

    # ONLY FOR INITIATION  #
    pygameee = pygame.init()
    ########################
    screen: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    font: pygame.font.Font = pygame.font.SysFont('arialblack',40)

    run: bool = True 
    on_menu: bool = True
    pause: bool = False
    click: bool = True
    mouse_coordinates: tuple = (0,0)

    pygame.mixer.init()
    pygame.mixer.music.load('assets/rituel.mp3')
    pygame.mixer.music.play(loops=0)

    def play_button_func(self):
        pass

    def quit_button_func(self):
        self.run = False

    main_menu = MainMenu(play_function=play_button_func, quit_function=quit_button_func)

    def play(self):
        self.screen.fill((60,80,100))
        while self.run:
            if not self.on_menu and not self.pause:
                pass
            
            if self.on_menu:
                status = self.main_menu.render(self.screen, self.mouse_coordinates, self.click)
                if status == 0:
                    self.run = False
                if status == 1:
                    self.on_menu = False

            if self.pause:
                pass
            

            self.click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.click = True

                if event.type == pygame.MOUSEMOTION:
                    self.mouse_coordinates = pygame.mouse.get_pos() 

                if event.type == pygame.QUIT:
                    self.run = False

            pygame.display.update()


game = Minesweeper()
game.play()