

from dataclasses import dataclass
from enum import Enum
from types import FunctionType
import pygame
from typing import Any, List
from constants import BUTTON_LEFT_OFFSET,TOP_OFFSET,WINDOW_HEIGHT,WINDOW_WIDTH
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
    music: bool = True
    running: int = 2
    

    def play_fun(self):
        self.running = 1

    def options_fun(self):
        self.menu_state = MainMenu.MenuStates.OPTIONS

    def scores_fun(self):
        self.menu_state = MainMenu.MenuStates.SCORES

    def quit_fun(self):
        self.running = 0
 
    logo1_image = pygame.transform.scale(pygame.transform.chop(pygame.image.load('assets/logo1.png'),(100,100,0,0)),(0.3*WINDOW_WIDTH,0.3*WINDOW_HEIGHT))
    # logo2_image = pygame.transform.chop(pygame.image.load('assets/logo2.png'),( 0.3*WINDOW_WIDTH, 0.5* WINDOW_HEIGHT))

    main_menu_objects = [
     Button(on_click=v['func'],left=BUTTON_LEFT_OFFSET,top=TOP_OFFSET*(k+1),title=v['title'] ) for k,v in enumerate([{
        'title': 'Play',
        'func' : play_fun,
    },{
        'title': 'Options',
        'func' : options_fun,
    },{
        'title': 'Scores',
        'func' : scores_fun,
    },{
        'title': 'Quit',
        'func' : quit_fun,
    }]
)
    ]


    def music_toggle(self):
        if self.music:
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()
        self.music = not self.music

    def restart_music(self):
        pygame.mixer.music.load('assets/rituel.mp3')
        pygame.mixer.music.play(loops=0)

    def back_function(self):
        self.menu_state = MainMenu.MenuStates.MAIN

    music_toggle_button = quit_button = Button(on_click = music_toggle,left=BUTTON_LEFT_OFFSET,top=150,title ="Toggle Music")
    restart_music_button = quit_button = Button(on_click = restart_music,left=BUTTON_LEFT_OFFSET,top=350,title ="Restart Music")
    back_button = Button(on_click = back_function,left=BUTTON_LEFT_OFFSET,top=550,title ="Back")

    options_objects = [
        music_toggle_button,restart_music_button,back_button
    ]

    scores_objects = [
        back_button
    ]


    def pass_collision_deets(self,mx,my, clicked, objects):
        for object in objects:
            if isinstance(object,Button):
                object.collidepoint(mx,my,clicked,self) 

    def object_draw(self,objects,screen):
        for object in objects:
            object.draw(screen)

    def print_main_menu_picture(self,screen,mx,my):
        
        
        screen.blit(self.logo1_image,(0.3*WINDOW_WIDTH,0.3*WINDOW_HEIGHT))

    def render(self,screen, mouse_coordinates,clicked) -> int:
        screen.fill((60,80,100))
        if self.menu_state == self.MenuStates.MAIN:
            
            self.pass_collision_deets(mouse_coordinates[0],mouse_coordinates[1],clicked,self.main_menu_objects)
            self.object_draw(self.main_menu_objects,screen)
            self.print_main_menu_picture(screen,mouse_coordinates[0],mouse_coordinates[1])
            
        if self.menu_state == self.MenuStates.OPTIONS:
            self.pass_collision_deets(mouse_coordinates[0],mouse_coordinates[1],clicked,self.options_objects)
            self.object_draw(self.options_objects,screen)
        if self.menu_state == self.MenuStates.SCORES:
            self.pass_collision_deets(mouse_coordinates[0],mouse_coordinates[1],clicked,self.scores_objects)
            self.object_draw(self.scores_objects,screen)
        
        return self.running
        
        



