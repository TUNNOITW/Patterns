import pygame

from Game.Scripts.GameState.Handlers.BaseHandlerABCClass import HandlerABC


"""
Класс, отвечающий за обработку событий связанных со стартовым меню
"""


class StartMenuHandler(HandlerABC):
    def Handle(self, mouseCords, mouseButtonsPressed, buttonsRectDict, ScreenNameSetter):
        MouseRect = pygame.rect.Rect(mouseCords[0], mouseCords[1], 1, 1)

        try:
            if MouseRect.colliderect(buttonsRectDict["newGameStartButtonRect"]):
                if mouseButtonsPressed[0]:
                    ScreenNameSetter("CreateNewGameMenu")
                else:
                    ScreenNameSetter("StartMenu")
            else:
                ScreenNameSetter("StartMenu")

        except KeyError:
            pass