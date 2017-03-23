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

                Components.Button.Button([500, 750], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey"),
        ]