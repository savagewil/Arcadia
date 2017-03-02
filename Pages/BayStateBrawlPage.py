import pygame
import MainPage
import Components
from Pages import Page


class BayStateBrawl(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([200, 100], 150, "Bay State Brawl", ["red", "black"]),
            Components.Container.Container(300, 0, 1280, 824, [

                Components.Button.Button([100, 475], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),


            ], "grey")
        ]
        self.mouseSpeed = 4
