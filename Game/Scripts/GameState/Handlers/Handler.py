import pygame

from Game.Scripts.GameState.Handlers.CreateNewGameMenuHandler import CreateNewGameMenuHandler
from Game.Scripts.GameState.Handlers.StartMenuHandler import StartMenuHandler

"""
Класс для подгрузки низкоуровневых классов отвечающих за обработку событий
"""


class Handler:
    def __init__(self):
        self.StartMenuHandler = StartMenuHandler()
        self.CreateNewGameMenuHandler = CreateNewGameMenuHandler()


    def Handle(self, mouseCords, mouseButtonsPressed, keyboardButtonsPressed,
               buttonsRectDict, saveData, inputData, CurrentScreenName, ScreenNameSetter):
        if CurrentScreenName == "StartMenu":
            self.StartMenuHandler.Handle(mouseCords=mouseCords, mouseButtonsPressed=mouseButtonsPressed,
                                         buttonsRectDict=buttonsRectDict, ScreenNameSetter=ScreenNameSetter)

        if CurrentScreenName == "CreateNewGameMenu":
            self.CreateNewGameMenuHandler.Handle(mouseCords=mouseCords, mouseButtonsPressed=mouseButtonsPressed, keyboardButtonsPressed=keyboardButtonsPressed,
                                                 buttonsRectDict= buttonsRectDict, saveData=saveData, inputData=inputData,)