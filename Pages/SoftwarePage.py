import pygame
import CameraPage
import DriveTrainPage
import AutonomousPage

import RemotePage
import PixiePage
import MainPage
import Components
from Pages import Page


class SoftwarePage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([200, 100], 150, "Software Design", ["red", "black"]),
            Components.Container.Container(300, 0, 1280, 824, [
                Components.Button.Button([50, 350], 130, 60, "Pixie", ["black", "white"], textHeight=68,
                                         function=PixiePage.PixiePage),

                Components.Button.Button([50, 850], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),

                Components.Button.Button([50, 475], 315, 60, "X-Box Remote", ["black", "white"],
                                         textHeight=68,
                                         function=RemotePage.RemotePage),

                Components.Button.Button([50, 725], 415, 60, "Autonomous Mode", ["black", "white"], textHeight=68,
                                         function=AutonomousPage.AutonomousPage),

                Components.Button.Button([50, 600], 440, 60, "Swerve Drive Train", ["black", "white"],
                                         textHeight=68,
                                         function=DriveTrainPage.DriveTrainPage),
                Components.Label.Label([550, 350], 40, "", ["gray", "black"], file="TextDocs/Software.txt")


            ], "grey")
        ]
