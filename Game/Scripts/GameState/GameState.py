import pygame


"""
Класс для хранения всей информации об игре
"""


class GameState:
    def __init__(self):
        self.screen = pygame.display.set_mode((1440, 900))

        self.currentScreenName = "StartMenu"

        self.mouseCords = [0, 0]
        self.mouseButtonsPressed = []
        self.keyboardButtonsPressed = []

        self.buttonsRectDict = {}

    def EveryTickUpdateData(self):
        self.mouseCords = pygame.mouse.get_pos()
        self.mouseButtonsPressed = pygame.mouse.get_pressed()
        self.keyboardButtonsPressed = pygame.key.get_pressed()


    def CurrentScreenNameGetter(self):
        return self.currentScreenName

    def CurrentScreenNameSetter(self, screenName):
        self.currentScreenName = str(screenName)


    def CurrentButtonsRectDictGetter(self):
        return self.buttonsRectDict

    def CurrentButtonsRectDictSetter(self, buttonsRectDict):
        self.buttonsRectDict = buttonsRectDict