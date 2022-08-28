

from dataclasses import dataclass
from enum import Enum
from types import FunctionType
import pygame
from typing import Any, List

from ui.button import Button


@dataclass
class MainMenu:
        
    class MenuStates(Enum):
        MAIN = "MAIN"
        OPTIONS = "OPTIONS"
        SCORES = "SCORES"

    play_function: FunctionType
    quit_function: FunctionType
    menu_state: MenuStates = MenuStates.MAIN
        
    def on_play_click(self):
        self.play_function()

    def on_options_click(self):
        self.menu_state = self.MenuStates.OPTIONS

    def on_scores_click(self):
        self.menu_state = self.MenuStates.SCORES

    def on_quit_click(self):
        self.quit_function()


    play_button = Button(on_click = on_play_click,left=75,top=150,title ="Play")
    options_button = Button(on_click = on_options_click,left=75,top=250,title ="Options")
    scores_button = Button(on_click = on_scores_click,left=75,top=350,title ="Scores")
    quit_button = Button(on_click = on_quit_click,left=75,top=450,title ="Quit")

    face1_image = pygame.image.load('assets/face.png')
    face2_image = pygame.image.load('assets/face2.png')
    bomb_image = pygame.image.load('assets/minesweep.png')

    main_menu_objects: List[Any] = [
        play_button, options_button,scores_button, quit_button
    ]


    def music_toggle(self):
        pass

    music_toggle_button = quit_button = Button(on_click = music_toggle,left=75,top=150,title ="Toggle Music")

    options_objects: List[Any] = [
        music_toggle_button
    ]



    def pass_collision_deets(self,mx,my, clicked, objects):
        for object in objects:
            if isinstance(object) == Button:
                object.collidepoint(mx,my,clicked) 

    def object_draw(self,objects,screen):
        for object in objects:
            object.draw(screen)

    def print_main_menu_picture(self,screen,mx,my):
        screen.blit(self.bomb_image,(350,70))
        bomb_image_rect = self.bomb_image.get_rect()
        if bomb_image_rect.collidepoint(mx,my):
            screen.blit(self.face1_image,(400,150))
        else:
            screen.blit(self.face2_image,(400,150))

    def render(self,screen, mouse_coordinates,clicked):
        if self.menu_state == self.MenuStates.MAIN:
            self.pass_collision_deets(mouse_coordinates[0],mouse_coordinates[1],clicked,self.main_menu_objects)
            self.object_draw(self.main_menu_objects,screen)
            self.print_main_menu_picture(screen,mouse_coordinates[0],mouse_coordinates[1])
        if self.menu_state == self.MenuStates.OPTIONS:
            self.pass_collision_deets(mouse_coordinates[0],mouse_coordinates[1],clicked,self.options_objects)
            self.object_draw(self.options_objects,screen)
        if self.menu_state == self.MenuStates.SCORES:
            pass



