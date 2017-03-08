import pygame
import Components
import MainPage
from Pages import Page


class ClimberPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([120, 200], 150, "Climber", ["red", "black"]),

            Components.Container.Container(512, 0, 1280, 512, [
                Components.Label.Label([100, 560], 60, "Our climber is a rotating drum that sticks \n" +
                                                       "to the velcro at the end of our rope. There\n" +
                                                       " is also a small arm at the bottom of our \n" +
                                                       "climber that extends after our climer starts\n" +
                                                       " rotating, which helps push on the touchpad.", ["red", "black"]),

                Components.Button.Button([100, 940], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey"),

            Components.PictureHolder.PictureHolder([600, 50], "Images/Climber.JPG", scale=.12)
        ]
