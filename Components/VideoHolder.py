import pygame
import Component


class VideoHolder(Component.Component):

    def __init__(self, loc, videoPath,L_W, **kwargs):

        self.video = pygame.movie.load(videoPath)

        self.location = loc

        self.hover = False
        self.clicked = False
        self.visible = True
        self.playing = False

        if "backgroundColor" in kwargs:
            self.backColor = pygame.Color(kwargs["backgroundColor"])
            self.back = True
        else:
            self.back = False

        if "size" in kwargs:
            self.size = float(kwargs["border"]) / 100.0
        else:
            self.size = 1

        if "border" in kwargs:
            self.border = kwargs["border"]
        elif self.back:
            self.border = 5

        if "function" in kwargs:
            self.function = kwargs["function"]
        else:
            self.function = None

        self.rect = pygame.Rect(loc[0] - self.border, loc[1] - self.border,
                                int(float(self.video.get_Size()[0]) * self.size) + self.border * 2,
                                int(float(self.video.get_Size()[1]) * self.size) + self.border * 2)

        self.movie_screen = pygame.Surface([int(float(self.video.get_Size()[0]) * self.size),
                                            int(float(self.video.get_Size()[1]) * self.size)]).convert()

    def display(self, screen):

        if self.visible:

            if self.back:
                pygame.draw.rect(screen, self.backColor, self.rect)

            screen.blit(self.movie_screen, self.location)

    def check(self, mouse):
        Output = Component.Component.check(self, mouse)

        if Output[0]:
            if self.playing:
                self.video.stop()
            else:
                self.video.play()

            self.playing = not self.playing

        return Output

