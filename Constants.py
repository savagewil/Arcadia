import pygame
Width = 800
# SCREENSIZE = [500, 500]
SCREENSIZE = [1280, 1024]

pygame.init()
size = SCREENSIZE
done = False
while not done:
    try:
        Screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        done = True
    except:
        size = [size[0], size[1] - 1]

done = False
while not done:
    try:
        Screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
        done = True
    except:
        size = [size[0] - 1, size[1]]

pygame.quit()

scaleConstant = min(float(size[0])/float(SCREENSIZE[0]), float(size[1])/float(SCREENSIZE[1]))


SCREENSIZE = [int(SCREENSIZE[0] * scaleConstant), int(SCREENSIZE[1] * scaleConstant)]
class ArcadiaBoard:
    LeftSquareButton = 53
    RightSquareButton = 54

    SinglePersonBotton = 49
    DoublePersonButton = 50

    RightOrangeButton = 306
    LeftOrangeButton = 308
    GreenButton = 32
    RedButton = 122

    LeftBlueButton = 120
    RightBlueButton = 304

    LeftLeverUp = 114
    LeftLeverDown = 102
    LeftLeverLeft = 100
    LeftLeverRight = 103

    RightLeverUp = 273
    RightLeverDown = 274
    RightLeverLeft = 276
    RightLeverRight = 275
