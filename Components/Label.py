import pygame

from Components import Component


def abc():
    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'
        , 'q', 'r', 's', 't', 'u', 'v', 'w', 's', 'x', 'y', 'z']


def Backspace(string):
    List = []
    for char in string:
        List.append(char)
    if not List.__len__() == 0:
        List.__delitem__(List.__len__() - 1)
    return "".join(List)


class Label(Component.Component):
    def __init__(self, loc, height, text, colors,
                 **kwargs):  # textsize=0, font="font/BebasNeue Bold.otf", background=False
        self.visible = True
        self.loc = self.x, self.y = loc

        self.text = text
        self.height = height

        self.colors = pygame.Color(colors[0]), pygame.Color(colors[1])
        self.clicked = False
        self.hover = False
        self.count = 0

        if "file" in kwargs:
            IN = open(kwargs["file"], 'r')
            self.text = ''.join(IN.readlines())

        if "font" in kwargs:
            self.font = kwargs["font"]
        else:
            self.font = "font/BebasNeue Bold.otf"
        print self.font
        font = pygame.font.Font(self.font, self.height)

        w, h = font.size(self.text)

        if "function" in kwargs:
            self.function = kwargs["function"]
        else:
            self.function = None

        if "background" in kwargs:
            self.background = kwargs["background"]
        else:
            self.background = False

        if "backLocation" in kwargs:
            self.Backloc = kwargs["BackLocation"]
        else:
            self.Backloc = (loc[0] - 5, loc[1] - 5)

        # print text

        if "backWidth" in kwargs:
            self.width = kwargs["backWidth"]
        else:
            self.width = w + 10

        if "backLength_Width" in kwargs:
            self.backLength_Width = kwargs["backLength_Width"]
        else:
            self.backLength_Width = [w + 10, h + 5]

        self.rect = pygame.Rect(self.Backloc, self.backLength_Width)

    def display(self, surface, sizeConstant):
        if self.visible:
            color2 = self.colors[1]
            color = self.colors[0]
            if self.background:
                rect = self.rect.copy()
                rect.x = int(rect.x * sizeConstant)
                rect.y = int(rect.y * sizeConstant)
                rect.width = int(rect.width * sizeConstant)
                rect.height = int(rect.height * sizeConstant)
                pygame.draw.rect(surface, color, rect)
            font = pygame.font.Font(self.font,  int(self.height * sizeConstant))
            if not self.text.__contains__("\n"):
                text = font.render(self.text, 1, color2)
                surface.blit(text, [int(self.loc[0] * sizeConstant), int(self.loc[1] * sizeConstant)])
            else:
                count = 0
                texts = self.text.split("\n")
                for text in texts:

                    if len(text) > 0 and ord(text[len(text) -1]) == 13:
                        text = text[0:len(text) - 1]
                    text = font.render(text, 1, color2)
                    surface.blit(text, [int(self.loc[0] * sizeConstant), int(self.loc[1] * sizeConstant + count * (font.get_height() + 10))])
                    count += 1
