import pygame
import Components
import MainPage
from Pages import Page


class HopperPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([150, 50], 150, "Hopper", ["red", "black"]),

            Components.Container.Container(312, 0, 1280, 812, [
                Components.Label.Label([100, 350], 60, "Our hopper is where the fuel is stored. The \n "+
                                                        "hopper can be filled from the top or from \n "+
                                                        "the field via the intake roller. It can\n "+
                                                        "hold up to 70 balls. A flap hinging in the \n "+
                                                        "back top edge lifts all the balls out of the\n "+
                                                        "hopper while a flap in the front drops down,\n "+
                                                        "dumping all the balls into the low boiler goal.", ["red", "black"]),

                Components.Button.Button([200, 900], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey"),
        ]
