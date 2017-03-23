import pygame
import Components
import MainPage
from Pages import Page


class ProjectManagementClassPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([350, 50], 150, "Project", ["red", "black"]),
            Components.Label.Label([300, 170], 150, "Management Class", ["red", "black"]),

            Components.Container.Container(350, 0, 1280, 900, [
                Components.Label.Label([200, 400], 60, "How do we finish a robot in 6 weeks?\n" +
                                                       "How do we stay on track, with 65 students? \n " +
                                                       "What happens if we run out of time?\n" +
                                                       "Making decisions at the right time is incredibly important.\n" +
                                                       "Our project management class helped enable \n " +
                                                       "our experienced students to do just that.", ["red", "black"]),

                Components.Button.Button([500, 890], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),
            ], "grey"),

        ]
