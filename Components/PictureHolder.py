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
        if "scalex" in kwargs:
            self.image = pygame.transform.scale(self.image, [kwargs["scalex"], self.rect.height])
            self.rect = self.image.get_bounding_rect()

        if "scaley" in kwargs:
            self.image = pygame.transform.scale(self.image, [self.rect.width, kwargs["scaley"]])
            self.rect = self.image.get_bounding_rect()

        if "scalexy" in kwargs:
            self.image = pygame.transform.scale(self.image, kwargs["scalexy"])
            self.rect = self.image.get_bounding_rect()

        if "scale" in kwargs:
            self.image = pygame.transform.scale(self.image, [int(kwargs["scale"] * self.rect.width),
                                                             int(kwargs["scale"] * self.rect.height)])
            self.rect = self.image.get_bounding_rect()

        if "rotate" in kwargs:
            self.image = pygame.transform.rotate(self.image, kwargs["rotate"])
            self.rect = self.image.get_bounding_rect()

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

    def display(self, screen, sizeConstant):

        if self.visible:
            surface = pygame.transform.scale(self.image,
                                               [int(sizeConstant * self.rect.width),
                                                int(sizeConstant * self.rect.height)])

            if self.back:

                rect = pygame.Rect([int(self.location[0] * sizeConstant - self.border),
                                    int(self.location[1] * sizeConstant - self.border)],
                                   [int(self.rect.width * sizeConstant + 2 * self.border),
                                    int(self.rect.height * sizeConstant + 2 * self.border)])
                pygame.draw.rect(screen, self.backColor, rect)

            screen.blit(surface, [int(self.location[0] * sizeConstant), int(self.location[1] * sizeConstant)])




