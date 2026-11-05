import pygame

from Game.Scripts.GameState.Handlers.StartMenuHandler import StartMenuHandler

"""
Класс для подгрузки низкоуровневых классов отвечающих за обработку событий
"""


class Handler:
    def __init__(self):
        self.StartMenuHandler = StartMenuHandler()


    def Handle(self, mouseCords, mouseButtonsPressed, buttonsRectDict,
               CurrentScreenName,ScreenNameSetter):
        if CurrentScreenName == "StartMenu":
            screenName = self.StartMenuHandler.Handle(mouseCords, mouseButtonsPressed, buttonsRectDict)
            ScreenNameSetter(screenName)