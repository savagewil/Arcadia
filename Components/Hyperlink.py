import Label
import pygame

class Hyperlink(Label.Label):
    def __init__(self, loc, height, text, colors, **kwargs):
        Label.Label.__init__(self, loc, height, text, colors, **kwargs)

    def display(self, surface):
        if self.visible:
            color2 = self.colors[1]
            color = self.colors[0]
            if self.background:
                rect = pygame.Rect(self.Backloc, self.backLength_Width)
                pygame.draw.rect(surface, color, rect)
            font = pygame.font.Font(self.font, self.height)
            if not self.hover:
                font.set_underline(True)
            text = font.render(self.text, 1, color2)
            surface.blit(text, self.loc)
