import pygame

from Game.Scripts.GameState.Handlers.BaseHandlerABCClass import HandlerABC


"""
Класс, отвечающий за обработку событий связанных с меню для сохдания нового сейва
"""


class CreateNewGameMenuHandler(HandlerABC):
    def Handle(self, mouseCords, mouseButtonsPressed, keyboardButtonsPressed,
               buttonsRectDict, saveData, inputData):
        MouseRect = pygame.rect.Rect(mouseCords[0], mouseCords[1], 1, 1)


        if mouseButtonsPressed[0]:
            if inputData["inputField"] == "SaveName":
                inputData["inputField"] = ""
            if inputData["inputField"] != "SaveName":
                if MouseRect.colliderect(buttonsRectDict["saveNameInputRect"]):
                    inputData["inputField"] = "SaveName"

            #FoodCoef
            if MouseRect.colliderect(buttonsRectDict["food0_5CoefSegmentControlRect"]):
                saveData["foodCoef"] = 0.5
            if MouseRect.colliderect(buttonsRectDict["food0_75CoefSegmentControlRect"]):
                saveData["foodCoef"] = 0.75
            if MouseRect.colliderect(buttonsRectDict["food1CoefSegmentControlRect"]):
                saveData["foodCoef"] = 1.0
            if MouseRect.colliderect(buttonsRectDict["food1_25CoefSegmentControlRect"]):
                saveData["foodCoef"] = 1.25
            if MouseRect.colliderect(buttonsRectDict["food2CoefSegmentControlRect"]):
                saveData["foodCoef"] = 2

            #EnemyCoef
            if MouseRect.colliderect(buttonsRectDict["enemy0_5CoefSegmentControlRect"]):
                saveData["enemyCoef"] = 0.5
            if MouseRect.colliderect(buttonsRectDict["enemy0_75CoefSegmentControlRect"]):
                saveData["enemyCoef"] = 0.75
            if MouseRect.colliderect(buttonsRectDict["enemy1CoefSegmentControlRect"]):
                saveData["enemyCoef"] = 1.0
            if MouseRect.colliderect(buttonsRectDict["enemy1_25CoefSegmentControlRect"]):
                saveData["enemyCoef"] = 1.25
            if MouseRect.colliderect(buttonsRectDict["enemy2CoefSegmentControlRect"]):
                saveData["enemyCoef"] = 2
        #except KeyError:
        #    pass