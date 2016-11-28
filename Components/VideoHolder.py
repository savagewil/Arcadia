import pygame
import Component


class VideoHolder(Component):

    def __init__(self, loc, videoPath,L_W, **kwargs):

        self.video = pygame.movie.load(videoPath)
        self.rect = pygame.Rect(loc, self.video.get_Size())
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