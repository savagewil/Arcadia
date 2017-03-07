import pygame
import Constants



class Mouse():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.CHANGE = 2
        self.clicked = False

    def display(self, Screen):
        if not self.clicked:
            pygame.draw.circle(Screen, pygame.Color("Black"), [self.x, self.y], 5)
            pygame.draw.circle(Screen, pygame.Color("white"), [self.x, self.y], 2)
        else:
            pygame.draw.circle(Screen, pygame.Color("white"), [self.x, self.y], 5)
            pygame.draw.circle(Screen, pygame.Color("black"), [self.x, self.y], 2)

    def HandleEvents(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == Constants.ArcadiaBoard.RightLeverUp or event.key == Constants.ArcadiaBoard.LeftLeverUp:
                    self.y -= self.CHANGE
                elif event.key == Constants.ArcadiaBoard.RightLeverDown or event.key == Constants.ArcadiaBoard.LeftLeverDown:
                    self.y += self.CHANGE
                elif event.key == Constants.ArcadiaBoard.RightLeverLeft or event.key == Constants.ArcadiaBoard.LeftLeverLeft:
                    self.x -= self.CHANGE
                elif event.key == Constants.ArcadiaBoard.RightLeverRight or event.key == Constants.ArcadiaBoard.LeftLeverRight:
                    self.x += self.CHANGE
                elif event.key == pygame.K_SPACE or event.key == Constants.ArcadiaBoard.LeftBlueButton or event.key == Constants.ArcadiaBoard.RightBlueButton:
                    self.clicked = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE or event.key == Constants.ArcadiaBoard.LeftBlueButton or event.key == Constants.ArcadiaBoard.RightBlueButton:
                    self.clicked = False
