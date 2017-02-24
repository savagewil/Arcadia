import pygame
import Components
from Pages import Page


class RobotMechanicsPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([100, 220], 150, "Robot Mechanics", ["red", "black"]),
            Components.Container.Container(480, 0, 1280, 480, [
                Components.Button.Button([100, 600], 370, 60, "Robot Features", ["black", "white"],
                                         textHeight=68,
                                         function=''),

                Components.Button.Button([100, 750], 160, 60, "Wiring", ["black", "white"], textHeight=68,
                                         function=''),
            ], "grey")
        ]
        self.mouseSpeed = 4
