import pygame
import Components
import RobotFeaturesPage
from Pages import Page


class RobotMechanicsPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([100, 220], 150, "Robot Mechanics", ["red", "black"]),
            Components.Container.Container(480, 0, 1280, 480, [
                Components.Button.Button([1280-(370 + 100), 800], 370, 60, "Robot Features", ["black", "white"],
                                         textHeight=68,
                                         function=RobotFeaturesPage.RobotFeaturesPage),

                Components.Button.Button([1280-(160 + 100), 650], 160, 60, "Wiring", ["black", "white"], textHeight=68,
                                         function=''),
            ], "grey"),
            Components.Label.Label([100, 550], 40, "", ["gray", "black"], file="TextDocs/RobotMechanics.txt")
        ]
        self.mouseSpeed = 4
