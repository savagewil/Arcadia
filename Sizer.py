import pygame, Constants
pygame.init()
size = Constants.SCREENSIZE
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
print size