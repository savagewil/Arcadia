import pygame, Constants
"""
Component Class
Author: William Savage
Email:savage.programing@gmail.com

This is the Superclass case for the Components

Instance data:
    Components all have a rectangle (self.rect) which they represent on the page.
    All components have a background color (self.color) for their rectangle
    All components should have a visibility marker (self.visible)

Methods:
    check(mouse) Handles the input, returns any function the component is meant to preform if necessary
    display(screen) Displays the component on the screen
"""


class Component:
    def __init___(self):
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.color = pygame.Color("black")
        self.visible = True
        self.function = None
        self.hover = False
        self.clicked = False

    def check(self, mouse):
        x, y = mouse.x, mouse.y
        if int(self.rect.left * Constants.scaleConstant)  < x < int(self.rect.right * Constants.scaleConstant) and\
                                int(self.rect.top * Constants.scaleConstant) < y < int(self.rect.bottom * Constants.scaleConstant):
            self.hover = True
            if mouse.clicked:
                self.clicked = True
                if isinstance(self.function, basestring) or self.function is None:
                    return [True, self.function]
                else:
                    # print self.text
                    return [True, self.function()]
            else:
                return [False, None]
        else:
            self.hover = False
            self.clicked = False
            return [False, None]

    def display(self, Screen, sizeConstants):
        rect = self.rect.copy()
        rect.x *= sizeConstants
        rect.y *= sizeConstants
        rect.width *= sizeConstants
        rect.height *= sizeConstants
        pygame.draw.rect(Screen, self.rect, self.color)

    def __str__(self):
        return self.__class__.__name__ + " at (" + str(self.rect.top) + "," + str(
            self.rect.left) + ")\n" + "Width:" + str(self.rect.width) + "\n" + "Height:" + str(self.rect.height)
