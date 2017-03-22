import pygame
import Components
import MainPage
from Pages import Page


class RemotePage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([400, 50], 150, "Controls", ["red", "black"]),

            Components.Container.Container(750, 0, 1280, 512, [
                Components.Label.Label([300, 800], 60, "These are the Operator Controls", ["red", "black"]),

                Components.Button.Button([500, 900], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey"),
            Components.PictureHolder.PictureHolder([25, 175], "Images/Robot Xbox Controller Button Map.png", scale=.7),
        ]
