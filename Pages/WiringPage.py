import pygame
import Components
import MainPage
from Pages import Page


class WiringPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([150, 50], 150, "Wiring", ["red", "black"]),

            Components.Container.Container(360, 0, 1280, 600, [
                Components.Label.Label([300, 550], 60, "Wiring Stuff", ["red", "black"]),

                Components.Button.Button([500, 750], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey"),
        ]
        self.mouseSpeed = 4
