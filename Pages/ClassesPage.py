import pygame
import IndependentProjectsPage
import RobotMechanicsPage
import SoftwarePage
import MainPage
import BayStateBrawlPage
import Components
import MechanicalDesignClassPage
import AnatomyRobotClassPage
import SoftwareClassPage
import FirstAidClass
import ProjectManagementClassPage
from Pages import Page


class ClassesPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.backgroundColor = pygame.Color("dark red")
        self.components = [
            Components.Label.Label([200, 100], 150, "2017", ["red", "black"]),
            Components.Label.Label([100, 220], 150, "Classes", ["red", "black"]),
            Components.Container.Container(512, 0, 1280, 512, [
                Components.Button.Button([100, 550], 440, 60, "Mechanical Design", ["black", "white"],
                                         textHeight=68,
                                         function=MechanicalDesignClassPage.MechanicalDesignClassPage),

                Components.Button.Button([1280-(230 + 100), 550], 230, 60, "Software", ["black", "white"],
                                         textHeight=68, function=SoftwareClassPage.SoftwareClassPage),

                Components.Button.Button([100, 850], 460, 60, "Anatomy of a Robot", ["black", "white"],
                                         textHeight=68,
                                         function=AnatomyRobotClassPage.AnatomyRobotClassPage),

                Components.Button.Button([100, 700], 480, 60, "Project Management", ["black", "white"],
                                         textHeight=68, function=ProjectManagementClassPage.ProjectManagementClassPage),

                Components.Button.Button([1280-(210 + 100), 850], 210, 60, "First Aid", ["black", "white"],
                                         textHeight=68, function=FirstAidClass.FirstAidClass),

                Components.Button.Button([1280 - (235 + 100), 700], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68, function=MainPage.MainPage),
            ], "grey")
        ]
