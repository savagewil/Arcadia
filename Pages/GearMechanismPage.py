import pygame
import Components
import MainPage
from Pages import Page


class GearMechanismPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([100, 150], 150, "Gear", ["red", "black"]),
            Components.Label.Label([50, 270], 150, "Mechanism", ["red", "black"]),

            Components.Container.Container(512, 0, 1280, 512, [
                Components.Label.Label([50, 550], 60, "Our gear mechanism is a pocket which was designed \n" +
                                                       " to pick up gears from the feeding station. Two  \n" +
                                                        "flaps controlled by servos can rotate panels which \n" +
                                                        " hold the gear in place, allowing them to be placed  \n" +
                                                        "onto the lift. Two servos also control a metal piece \n" +
                                                        "which push the gear onto the lift.", ["red", "black"]),

                Components.Button.Button([800, 930], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey"),

            Components.PictureHolder.PictureHolder([600, 50], "Images/BiuldingChassis.JPG", scale=.12)
        ]
