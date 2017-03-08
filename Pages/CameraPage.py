import pygame
import Components
import MainPage
from Pages import Page


class CameraPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([150, 200], 150, "Camera", ["red", "black"]),

            Components.Container.Container(550, 0, 1280, 812, [
                Components.Label.Label([100, 600], 60, "Our robot's camera is mounted on a servo that rotates 180 \n" +
                                                       "degrees. Controlled by the driver, this can capture from \n" +
                                                       "the gear inside to help putting gears on the lift or   \n" +
                                                       "swivel around to help climbing at the end of the match.", ["red", "black"]),

                Components.Button.Button([100, 900], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey"),
        ]
