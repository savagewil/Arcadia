import pygame
import Components
import MainPage
from Pages import Page


class ArcadiaPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [

            Components.Label.Label([370, 100], 150, "The Arcadia", ["red", "black"]),
            Components.Label.Label([470, 220], 150, "Project", ["red", "black"]),

            Components.Container.Container(512, 0, 1280, 512, [
                Components.Label.Label([450, 550], 60, "You're looking at it", ["red", "black"]),

                Components.Button.Button([500, 750], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey"),
        ]
