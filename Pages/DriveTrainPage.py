import pygame
import Components
import MainPage
from Pages import Page


class DriveTrainPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([150, 150], 150, "Drive", ["red", "black"]),
            Components.Label.Label([200, 270], 150, "Train", ["red", "black"]),

            Components.Container.Container(512, 0, 1280, 512, [
                Components.Label.Label([100, 600], 60, "has a set of four swerve wheels which allow for fluid  \n" +
                                                       "and fast movement across the field. Our chassis was \n" +
                                                       "custom-built to the short robot dimensions, as \n" +
                                                       "this gives more length to our intake.", ["red", "black"]),

                Components.Button.Button([100, 900], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey"),

            Components.PictureHolder.PictureHolder([600, 50], "Images/BiuldingChassis.JPG", scale=.12)
        ]
