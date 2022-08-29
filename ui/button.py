from __future__ import annotations
from types import FunctionType
from typing import Tuple
import pygame


class Button(pygame.Rect):
    def __init__(
        self,
        on_click: FunctionType,
        left: int,
        top: int,
        width: int = 200,
        height: int = 80,
        background_color: tuple = (0, 0, 0),
        text_color: tuple = (255, 255, 255),
        tag: str = "Default",
        title: str = "Default",
    ):
        pygame.font.init()
        self.background_color = background_color
        self.text_color = text_color
        self.tag = tag
        self.on_click = on_click
        self.title = title
        self.font = pygame.font.SysFont("arialunicode", 50)
        super().__init__(left, top, width, height)

    def collidepoint(self, mx, my, clicked: bool):
        hovered = super().collidepoint(mx, my)
        if hovered:
            self.background_color = (255, 255, 255)
            self.text_color = (0, 0, 0)
            print(f"{self.title} button hovered!")
            if clicked:
                self.on_click()
                self.background_color = (0, 255, 0)
        else:
            self.text_color = (255, 255, 255)
            self.background_color = (0, 0, 0)

    def draw(self, surface):
        text_img = self.font.render(
            self.title, True, self.text_color, self.background_color
        )
        pygame.draw.rect(surface, self.background_color, self, border_radius=10)
        surface.blit(
            text_img, (self.left + (self.width // 10), self.top + (self.height // 3))
        )
