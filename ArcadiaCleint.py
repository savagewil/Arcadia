import pygame
import Pages
import Mouse
import Constants
import Components
import Games
import Combos



    
pygame.init()

Screen = pygame.display.set_mode(Constants.SCREENSIZE, pygame.FULLSCREEN) #

pygame.key.set_repeat(30, 1)
mouse = Mouse.Mouse(int(Constants.SCREENSIZE[0] * Constants.scaleConstant/2),
                    int(Constants.SCREENSIZE[1] * Constants.scaleConstant/2))

Currentpage = Pages.MainPage.MainPage()
Currentpage.display(Screen, Constants.scaleConstant)

LastPage = [Currentpage]
Done = False
x = 0
Wait = 0
count = 0
timeCount = 0
secretCombos = []
##exitCode = [273, 274, 102, 114, 122, 32, 308, 306, 50]
##otherCode = [Constants.ArcadiaBoard.LeftLeverUp,
##             Constants.ArcadiaBoard.RightLeverUp,
##             Constants.ArcadiaBoard.LeftLeverDown,
##             Constants.ArcadiaBoard.RightLeverDown,
##             Constants.ArcadiaBoard.LeftLeverLeft,
##             Constants.ArcadiaBoard.LeftLeverRight,
##             Constants.ArcadiaBoard.RightLeverLeft,
##             Constants.ArcadiaBoard.RightLeverRight,
##             Constants.ArcadiaBoard.DoublePersonButton,
##             Constants.ArcadiaBoard.SinglePersonBotton,
##             Constants.ArcadiaBoard.LeftSquareButton]
##otherCode = [Constants.ArcadiaBoard.LeftSquareButton]
codeIndex = 0
otherCodeIndex = 0
def terminate():
    global Done
    Done =False
while not Done:
    try:
        timeCount += 1
        if timeCount > 10000:
            timeCount = 0
            Currentpage = Pages.MainPage.MainPage()
            LastPage = [Currentpage]

        mouse.CHANGE = Currentpage.mouseSpeed

        pygame.time.delay(1)
        events = pygame.event.get()
        mouse.HandleEvents(events)
        if not Wait == 0:
            mouse.clicked = False


        for event in events:
            if event.type == pygame.KEYUP:
                timeCount = 0
                # print event.unicode
                if event.key == pygame.K_END:
                    Done = True
                for Combo in Combos.SecretCombos:
                    
                    if Combo[1] < len(Combo[0]) and Combo[0][Combo[1]] == event.key:
                        Combo[1] += 1
                        if Combo[1] >= len(Combo[0]):
                            Done = Combo[2]()
                            Combo[1] = 0
                        
                    else:
                        Combo[1] = 0
                if event.key == pygame.K_BACKSPACE or event.key == 50:
                    if len(LastPage) - 1 >= 0:
                        Currentpage = LastPage[len(LastPage) - 1]
                        LastPage.__delitem__(len(LastPage) - 1)
                    
                elif event.key == pygame.K_7 or event.key == 32:
                    LastPage.append(Currentpage)
                    Currentpage = Pages.Current2017Page.Current2017Page()

                elif event.key == pygame.K_m or event.key == 122:
                    LastPage.append(Currentpage)
                    Currentpage = Pages.MainPage.MainPage()
                    
                elif event.key == pygame.K_c or event.key == 49:
                    mouse.x, mouse.y = Constants.SCREENSIZE[0]/2, Constants.SCREENSIZE[1]/2
        
        output = Currentpage.check(mouse)

        if output[0] and Wait == 0:
            if output[1] == "x":
                Done = True
            elif output[1] == "b":
                if len(LastPage) - 1 >= 0:
                    Currentpage = LastPage[len(LastPage) - 1]
                    LastPage.__delitem__(len(LastPage) - 1)
            elif not output[1] is None and not isinstance(output[1], basestring):
                LastPage.append(Currentpage)
                Currentpage = output[1]
                Wait = 50

        if Wait > 0:
            Wait -= 1

        if count % 2 == 0:
            Currentpage.display(Screen, Constants.scaleConstant)
        mouse.display(Screen)
        pygame.display.flip()
        count += 1
    except Exception as e:
        pygame.quit()
        pygame.init()

        Screen = pygame.display.set_mode(Constants.SCREENSIZE, pygame.FULLSCREEN) #

        pygame.key.set_repeat(30, 1)
        mouse = Mouse.Mouse(Constants.SCREENSIZE[0]/2, Constants.SCREENSIZE[1]/2)

        Currentpage = Pages.MainPage.MainPage()
        Currentpage.display(Screen, Constants.scaleConstant)

        LastPage = [Currentpage]
        Done = False
        x = 0
        Wait = 0
        count = 0
        timeCount = 0
        exitCode = [273, 274, 102, 114, 122, 32, 308, 306, 50]
        codeIndex = 0
        print e
pygame.quit()
print Done

