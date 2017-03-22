import pygame
import SafetyPage
import Current2017Page
import Components
from Pages import Page


class MainPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")

        self.components = [

            Components.Label.Label([350, 120], 200, "REDSHIFT", ["red", "black"]),

            Components.Container.Container(512, 0, 1280, 512,[

                Components.Button.Button([1280-(180 + 200), 670], 180, 100, "2017", ["black", "white"], textHeight=108,
                                         function=Current2017Page.Current2017Page),

                Components.Button.Button([200, 670], 260, 100, "Safety", ["black", "white"], textHeight=108,
                                         function=SafetyPage.SafetyPage),

            ], "grey")
        ]
