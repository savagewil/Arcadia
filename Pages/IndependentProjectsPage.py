import pygame
import Components
import MainPage
import ArcadiaPage
import ScoutingPage
from Pages import Page


class IndependentProjectsPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([100, 100], 150, "Independent", ["red", "black"]),
            Components.Label.Label([190, 220], 150, "Projects", ["red", "black"]),

            #Components.PictureHolder.PictureHolder([700, 100], "Images/TeamCircle.jpg", scale=.12),
            Components.Container.Container(400, 0, 1280, 800, [
                Components.Button.Button([100, 625], 190, 60, "Arcadia", ["black", "white"],
                                         textHeight=68,
                                         function=ArcadiaPage.ArcadiaPage),

                Components.Button.Button([100, 775], 205, 60, "Scouting", ["black", "white"], textHeight=68,
                                         function=ScoutingPage.ScoutingPage),

                Components.Button.Button([100, 475], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey"),
            Components.Label.Label([500, 500], 40, "", ["gray", "black"], file="TextDocs/IndependentProjects.txt")
        ]