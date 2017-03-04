import pygame
import IndependentProjectsPage
import RobotMechanicsPage
import SoftwarePage
import MainPage
import BayStateBrawlPage
import Components
from Pages import Page


class ClassesPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([200, 100], 150, "2017", ["red", "black"]),
            Components.Label.Label([100, 220], 150, "Classes", ["red", "black"]),
            Components.Container.Container(512, 0, 1280, 512, [
                Components.Button.Button([100, 550], 390, 60, "First Aid", ["black", "white"],
                                         textHeight=68,
                                         function=RobotMechanicsPage.RobotMechanicsPage),

                Components.Button.Button([1280-(385 + 100), 550], 385, 60, "Software", ["black", "white"],
                                         textHeight=68, function=SoftwarePage.SoftwarePage),

                Components.Button.Button([100, 850], 500, 60, "Anatomy of a Robot", ["black", "white"],
                                         textHeight=68,
                                         function=IndependentProjectsPage.IndependentProjectsPage),

                Components.Button.Button([100, 700], 185, 60, "Project Management", ["black", "white"],
                                         textHeight=68, function=''),

                Components.Button.Button([1280-(375 + 100), 850], 375, 60, "Mechanical Design", ["black", "white"],
                                         textHeight=68, function=BayStateBrawlPage.BayStateBrawlPage),

                Components.Button.Button([1280 - (235 + 100), 700], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68, function=MainPage.MainPage),
            ], "grey")
        ]
