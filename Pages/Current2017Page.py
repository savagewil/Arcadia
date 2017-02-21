import pygame
import ExamplePage
import Components
from Pages import Page


class Current2017Page(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Container.Container(300, 0, 800, 300, [

            ], "grey")
        ]
        self.mouseSpeed = 2
