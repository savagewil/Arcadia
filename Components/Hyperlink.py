import Label
import pygame


class Hyperlink(Label.Label):

    def __init__(self, loc, height, text, colors, **kwargs):
        Label.Label.__init__(self, loc, height, text, colors, **kwargs)

    def display(self, surface, sizeConstant):
        if self.visible:
            color2 = self.colors[1]
            color = self.colors[0]
            if self.background:
                rect = pygame.Rect(self.Backloc, self.backLength_Width)

                rect.x = int(rect.x * sizeConstant)
                rect.y = int(rect.y * sizeConstant)
                rect.width = int(rect.width * sizeConstant)
                rect.height = int(rect.height * sizeConstant)

                pygame.draw.rect(surface, color, rect)
            font = pygame.font.Font(self.font, int(self.height * sizeConstant))
            if not self.hover:
                font.set_underline(True)
            text = font.render(self.text, 1, color2)
            surface.blit(text, [int(self.loc[0] * sizeConstant), int(self.loc[1] * sizeConstant)])
