import pygame
import Components
import MainPage
import Constants
from Pages import Page


class ArcadiaPage(Page.Page):
    def __init__(self):
        Page.Page.__init__(self)
        self.imageHolder = Components.PictureHolder.PictureHolder([650, 10], "Images/Softwareclass.jpg", scale=.150,
                                                                  border= 5, backgroundColor= "black")
        self.backgroundColor = pygame.Color("dark red")
        self.components = [

            Components.Label.Label([50, 50], 150, "The Arcadia", ["red", "black"]),
            Components.Label.Label([150, 170], 150, "Project", ["red", "black"]),

            Components.Container.Container(300, 0, 1280, 1000, [
                Components.Label.Label([50, 350], 60, "", ["gray", "black"], file="TextDocs/ArcadiaPageInfo.txt"),

                Components.Button.Button([900, 850], 235, 60, "Main Page", ["black", "white"],
                                         textHeight=68,
                                         function=MainPage.MainPage),

                Components.Button.Button([900, 650], 120, 60, "Back", ["black", "white"],
                                         textHeight=68,
                                         function="b"),
                self.imageHolder
            ], "grey"),
        ]

    # def draw(self, num, size, location, PositionChange, scale, sizeConstant, screen):
    #     if num > 0:
    #         print "num, size, location, PositionChange, scale, sizeConstant, screen"
    #         print num, size, location, PositionChange, scale, sizeConstant, screen
    #
    #         size = [size[0] * scale, size[1] * scale]
    #         print size
    #
    #         location[0] += PositionChange[0]
    #         location[1] += PositionChange[1]
    #         sizeConstant *= scale
    #         surface = pygame.Surface(size)
    #         self.displaynon(surface, sizeConstant)
    #         screen.blit(surface, location)
    #         PositionChange = [PositionChange[0] * scale, PositionChange[1] * scale]
    #         self.draw(num - 1, size, location, PositionChange , scale, sizeConstant, screen)

    def display(self, screen, sizeConstant):
        print "-"
        screen.fill(self.backgroundColor)
        self.imageHolder.image = screen
        for component in self.components:
            component.display(screen, sizeConstant)
        for i in range(0, 3):
            self.imageHolder.display(screen, sizeConstant)
