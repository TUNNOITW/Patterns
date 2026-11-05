import pygame

from Game.Scripts.GameState.Render.CreateNewGameMenuRender import CreateNewGameMenuRender
from Game.Scripts.GameState.Render.StartMenuRender import StartMenuRender


"""
Класс, который будет загружать низкоуровневые классы, отвечающие за рендер отдельных UI
"""


class Render:
    def __init__(self, screen):
        self.screen = screen

        self.renderStartMenu = StartMenuRender()
        self.renderCreateNewGameMenu = CreateNewGameMenuRender()


    def Render(self, currentScreenName, mouseCords):
        self.screen.fill((0, 0, 0))

        renderStartMenuButtonsRectDict = {}
        renderCreateNewGameMenuButtonsRectDict = {}

        if currentScreenName == "StartMenu":
            renderStartMenuButtonsRectDict = self.renderStartMenu.Render(self.screen, mouseCords)

        if currentScreenName == "CreateNewGameMenu":
            renderCreateNewGameMenuButtonsRectDict = self.renderCreateNewGameMenu.Render(self.screen, mouseCords)

        buttonsRectDict = {}

        #print(renderStartMenuButtonsRectDict, "1")
        #print(renderCreateNewGameMenuButtonsRectDict, "2")


        for key, value in renderCreateNewGameMenuButtonsRectDict.items():
            buttonsRectDict[key] = value

        for key, value in renderStartMenuButtonsRectDict.items():
            buttonsRectDict[key] = value


        return buttonsRectDict