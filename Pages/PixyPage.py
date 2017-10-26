import pygame
import Components
import MainPage
from Pages import Page


class PixiePage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([150, 100], 150, "Pixy", ["red", "black"]),

            Components.Container.Container(300, 0, 1280, 1000, [
                Components.Label.Label([50, 350], 60, "", ["gray", "black"], file="TextDocs/PixyInformation.txt"),

                Components.Button.Button([200, 920], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
                Components.Button.Button([800, 920], 120, 60, "Back", ["black", "white"],
                                         textHeight=68,
                                         function="b"),
            ], "grey"),
        ]