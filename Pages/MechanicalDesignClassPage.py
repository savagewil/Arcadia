import pygame
import Components
import MainPage
from Pages import Page


class MechanicalDesignClassPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([350, 50], 150, "Mechanical", ["red", "black"]),
            Components.Label.Label([300, 170], 150, "Design Class", ["red", "black"]),

            Components.Container.Container(350, 0, 1280, 900, [
                Components.Label.Label([700, 400], 60, "This class is for those  \n " +
                                                       "students who want to be \n" +
                                                       "involved in the actual  \n" +
                                                       "design and implementation \n" +
                                                       "of the physical robot. \n" +
                                                       "It was a 2-day class", ["red", "black"]),

                Components.Button.Button([500, 890], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey"),

            Components.PictureHolder.PictureHolder([50, 420], "Images/MechanicalCadDesigning.jpg", scale=.150)
        ]
