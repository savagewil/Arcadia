import pygame
import Component
"""
PictureHolder Class
Author: William Savage
Email:savage.programing@gmail.com
This class displays and handles buttons.
"""


class PictureHolder(Component.Component):

    def __init__(self, loc, imagePath, **kwargs):

        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_bounding_rect()
        self.location = loc

        self.hover = False
        self.clicked = False
        self.visible = True

        if "backgroundColor" in kwargs:
            self.backColor = pygame.Color(kwargs["backgroundColor"])
            self.back = True
        else:
            self.back = False

        if "border" in kwargs:
            self.border = kwargs["border"]
        elif self.back:
            self.border = 5

        if "function" in kwargs:
            self.function = kwargs["function"]
        else:
            self.function = None

    def display(self, screen):

        if self.visible:

            if self.back:

                rect = pygame.Rect([self.location[0] - self.border, self.location[1] - self.border],
                                   [self.rect.height + 2 * self.border, self.rect.width + 2 * self.border])
                pygame.draw.rect(screen, self.backColor, rect)

            screen.blit(self.image, self.location)




