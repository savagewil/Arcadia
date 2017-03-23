import Constants
import Games
import pygame


def Quit():
    return True

def runWorm():
    pygame.quit()
    Games.wormy.setup()
    Games.wormy.main()

def runink():
    pygame.quit()
    Games.inkspill.main()
    
SecretCombos = [[[273, 274, 102, 114, 122, 32, 308, 306, 50], 0, Quit],

                [[Constants.ArcadiaBoard.LeftLeverUp,
                  Constants.ArcadiaBoard.RightLeverUp,
                  Constants.ArcadiaBoard.LeftLeverDown,
                  Constants.ArcadiaBoard.RightLeverDown,
                  Constants.ArcadiaBoard.LeftLeverLeft,
                  Constants.ArcadiaBoard.LeftLeverRight,
                  Constants.ArcadiaBoard.RightLeverLeft,
                  Constants.ArcadiaBoard.RightLeverRight,
                  Constants.ArcadiaBoard.DoublePersonButton,
                  Constants.ArcadiaBoard.SinglePersonBotton,
                  Constants.ArcadiaBoard.LeftSquareButton],
                 0, runWorm],

                [[ 122, 32, 308, 306,
                   Constants.ArcadiaBoard.LeftLeverUp,
                   Constants.ArcadiaBoard.LeftLeverLeft,
                   Constants.ArcadiaBoard.LeftLeverDown,
                   Constants.ArcadiaBoard.LeftLeverRight,
                   Constants.ArcadiaBoard.LeftSquareButton], 0, runink],

                [[ pygame.K_w,
                   pygame.K_i,
                   pygame.K_l,
                   pygame.K_l,
                   pygame.K_i,
                   pygame.K_a,
                   pygame.K_m], 0, runWorm],

                [[ pygame.K_s,
                   pygame.K_a,
                   pygame.K_v,
                   pygame.K_a,
                   pygame.K_g,
                   pygame.K_e], 0, runink],
                ]



