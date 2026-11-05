import pygame

from Game.Scripts.GameState.Handlers.BaseHandlerABCClass import HandlerABC


"""
Класс, отвечающий за обработку событий связанных со стартовым меню
"""


class StartMenuHandler(HandlerABC):
    def Handle(self, mouseCords, mouseButtonsPressed, buttonsRectDict, ):
        MouseRect = pygame.rect.Rect(mouseCords[0], mouseCords[1], 1, 1)

        try:
            if MouseRect.colliderect(buttonsRectDict["newGameStartButtonRect"]):
                if mouseButtonsPressed[0]:
                    return "CreateNewGameMenu"
                    print(1)
                else:
                    return "StartMenu"
            else:
                return "StartMenu"

        except KeyError:
            pass