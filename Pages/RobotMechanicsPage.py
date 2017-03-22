import pygame
import Components
import RobotFeaturesPage
import WiringPage
import Current2017Page
from Pages import Page


class RobotMechanicsPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([100, 220], 150, "Robot Mechanics", ["red", "black"]),
            Components.Container.Container(512, 0, 1280, 512, [
                Components.Button.Button([1280 -(350 + 100), 800], 350, 60, "Robot Features", ["black", "white"],
                                         textHeight=68,
                                         function=RobotFeaturesPage.RobotFeaturesPage),

                Components.Button.Button([1280 -(250 + 100), 600], 250, 60, "Electrical", ["black", "white"], textHeight=68,
                                         function=WiringPage.WiringPage),

                Components.Button.Button([1280 - (235 + 100), 700], 235, 60, "2017 Page", ["black", "white"],
                                         textHeight=68,
                                         function=Current2017Page.Current2017Page),
            ], "grey"),
            Components.Label.Label([100, 550], 40, "", ["gray", "black"], file="TextDocs/RobotMechanics.txt")
        ]
