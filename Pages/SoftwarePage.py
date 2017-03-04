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
                Components.Button.Button([100, 350], 130, 60, "Pixie", ["black", "white"], textHeight=68,
                                         function=PixiePage.PixiePage),

                Components.Button.Button([100, 475], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),

                Components.Button.Button([100, 600], 315, 60, "X-Box Remote", ["black", "white"],
                                         textHeight=68,
                                         function=RemotePage.RemotePage),

                Components.Button.Button([100, 725], 415, 60, "Autonomous Mode", ["black", "white"], textHeight=68,
                                         function=AutonomousPage.AutonomousPage),

                Components.Button.Button([100, 850], 425, 60, "Swivel Drive Train", ["black", "white"],
                                         textHeight=68,
                                         function=DriveTrainPage.DriveTrainPage),


            ], "grey")
        ]
