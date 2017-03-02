import pygame
import IndependentProjectsPage
import RobotMechanicsPage
import SoftwarePage
import MainPage
import BayStateBrawlPage
import Components
from Pages import Page


class Current2017Page(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([200, 100], 150, "2017", ["red", "black"]),
            Components.Label.Label([100, 220], 150, "RED SHIFT", ["red", "black"]),
            Components.PictureHolder.PictureHolder([700, 100], "Images/TeamCircle.jpg", scale=.12),
            Components.Container.Container(512, 0, 1280, 512, [
                Components.Button.Button([100, 550], 390, 60, "Robot Mechanics", ["black", "white"],
                                         textHeight=68,
                                         function=RobotMechanicsPage.RobotMechanicsPage),

                Components.Button.Button([1280-(385 + 100), 550], 385, 60, "Software Design", ["black", "white"],
                                         textHeight=68,
                                         function=SoftwarePage.SoftwarePage),

                Components.Button.Button([100, 850], 500, 60, "Independent Projects", ["black", "white"],
                                         textHeight=68,
                                         function=IndependentProjectsPage.IndependentProjectsPage),

                Components.Button.Button([100, 700], 185, 60, "Classes", ["black", "white"], textHeight=68,
                                         function=''),

                Components.Button.Button([1280-(375 + 100), 850], 375, 60, "Bay State Brawl", ["black", "white"],
                                         textHeight=68,
                                         function=BayStateBrawlPage.BayStateBrawlPage),

                Components.Button.Button([1280 - (235 + 100), 700], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey")
        ]
        self.mouseSpeed = 4
