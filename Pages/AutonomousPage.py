import pygame
import Components
import MainPage
from Pages import Page


class AutonomousPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([150, 50], 150, "Autonomous Mode", ["red", "black"]),

            Components.Container.Container(225, 0, 1280, 1000, [
                Components.Button.Button([500, 950], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
                Components.Label.Label([25, 250], 30, "", ["gray", "black"], file="TextDocs/AutonomousMode.txt")
            ], "grey"),
        ]
