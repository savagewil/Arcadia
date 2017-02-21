import pygame
import ExamplePage
import Current2017Page
import Components
from Pages import Page


class MainPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([250, 50], 100, "RED SHIFT", ["red", "black"]),
            Components.Container.Container(300, 0, 800, 300, [
                Components.Button.Button([750-200, 350], 200, 60, "2017 Page", ["black", "white"], textHeight=68,
                                         function=Current2017Page.Current2017Page),
                Components.Button.Button([750 - 200, 420], 100, 60, "Exit", ["black", "white"], textHeight=68,
                                         function="x")
            ], "grey")
        ]
        self.mouseSpeed = 2
