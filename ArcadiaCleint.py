import pygame
import Pages
import Mouse
import Constants

pygame.init()

Screen = pygame.display.set_mode(Constants.SCREENSIZE, pygame.FULLSCREEN)

pygame.key.set_repeat(30, 1)
mouse = Mouse.Mouse(Constants.SCREENSIZE[0]/2, Constants.SCREENSIZE[1]/2)

Currentpage = Pages.MainPage.MainPage()
Currentpage.check(mouse)
Currentpage.display(Screen)

LastPage = Currentpage
Done = False
x = 0
Wait = 0
count = 0
exitCode = [273, 274, 102, 114, 122, 32, 308, 306, 50]
codeIndex = 0
while not Done:

    mouse.CHANGE = Currentpage.mouseSpeed

    pygame.time.delay(1)
    events = pygame.event.get()
    mouse.HandleEvents(events)
    if not Wait == 0:
        mouse.clicked = False


    for event in events:
        if event.type == pygame.KEYUP:
            # print event.unicode
            if event.key == pygame.K_ESCAPE:
                Done = True
            if exitCode[codeIndex] == event.key:
                codeIndex += 1
                if codeIndex >= len(exitCode):
                    Done = True
            else:
                codeIndex = 0

            if event.key == pygame.K_BACKSPACE:
                Currentpage = LastPage
                
            elif event.key == pygame.K_7:
                LastPage = Currentpage
                Currentpage = Pages.Current2017Page.Current2017Page()

    output = Currentpage.check(mouse)

    if output[0] and Wait == 0:
        if output[1] == "x":
            Done = True
        elif not output[1] is None:
            LastPage = Currentpage
            Currentpage = output[1]
            Wait = 50

    if Wait > 0:
        Wait -= 1

    if count % 2 == 0:
        Currentpage.display(Screen)
    mouse.display(Screen)
    pygame.display.flip()
    count += 1

pygame.quit()
