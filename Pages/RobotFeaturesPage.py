import pygame
import CameraPage
import DriveTrainPage
import ClimberPage
import HopperPage
import PixiePage
import MainPage
import Components
from Pages import Page


class RobotFeaturesPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([200, 100], 150, "Robot Features", ["red", "black"]),
            Components.Container.Container(512, 0, 1280, 512, [
                Components.Button.Button([100, 850], 430, 60, "Swivel Drive Train", ["black", "white"],
                                         textHeight=68,
                                         function=DriveTrainPage.DriveTrainPage),

                Components.Button.Button([100, 550], 180, 60, "Hopper", ["black", "white"],
                                         textHeight=68,
                                         function=HopperPage.HopperPage),

                Components.Button.Button([100, 700], 185, 60, "Climber", ["black", "white"], textHeight=68,
                                         function=ClimberPage.ClimberPage),

                Components.Button.Button([1280-(150 + 100), 550], 150, 60, "Pixie", ["black", "white"], textHeight=68,
                                         function=PixiePage.PixiePage),

                Components.Button.Button([1280-(185 + 100), 700], 185, 60, "Camera", ["black", "white"],
                                         textHeight=68,
                                         function=CameraPage.CameraPage),

                Components.Button.Button([1280 - (235 + 100), 850], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey")
        ]
