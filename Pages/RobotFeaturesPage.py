import pygame
import CameraPage
import DriveTrainPage
import ClimberPage
import HopperPage
import PixyPage
import MainPage
import GearMechanismPage
import Components
from Pages import Page


class RobotFeaturesPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([200, 100], 150, "Robot Features", ["red", "black"]),
            Components.Container.Container(512, 0, 1280, 512, [
                Components.Button.Button([400, 850], 440, 60, "Swerve Drive Train", ["black", "white"],
                                         textHeight=68,
                                         function=DriveTrainPage.DriveTrainPage),

                Components.Button.Button([100, 550], 180, 60, "Hopper", ["black", "white"],
                                         textHeight=68,
                                         function=HopperPage.HopperPage),

                Components.Button.Button([100, 700], 185, 60, "Climber", ["black", "white"], textHeight=68,
                                         function=ClimberPage.ClimberPage),

                Components.Button.Button([1280-(150 + 100), 550], 150, 60, "Pixy", ["black", "white"], textHeight=68,
                                         function=PixyPage.PixiePage),

                Components.Button.Button([1280-(185 + 100), 700], 185, 60, "Camera", ["black", "white"],
                                         textHeight=68,
                                         function=CameraPage.CameraPage),

                Components.Button.Button([460, 550], 380, 60, "Gear Mechanism", ["black", "white"],
                                         textHeight=68,
                                         function=GearMechanismPage.GearMechanismPage),

                Components.Button.Button([510, 700], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey")
        ]
