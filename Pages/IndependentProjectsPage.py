import pygame
import Components
import MainPage
from Pages import Page


class IndependentProjectsPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([100, 100], 150, "Independent", ["red", "black"]),
            Components.Label.Label([190, 220], 150, "Projects", ["red", "black"]),
            #Components.PictureHolder.PictureHolder([700, 100], "Images/TeamCircle.jpg", scale=.12),
            Components.Container.Container(480, 0, 1280, 480, [
                Components.Button.Button([100, 550], 190, 60, "Arcadia", ["black", "white"],
                                         textHeight=68,
                                         function=''),

                Components.Button.Button([100, 700], 205, 60, "Scouting", ["black", "white"], textHeight=68,
                                         function=''),

                Components.Button.Button([100, 850], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage()),
            ], "grey")
        ]
        self.mouseSpeed = 4
