import pygame
pygame.font.init()


from Game.Scripts.GameState.Render.BaseRenderABSClass import RenderABC


"""
Класс, отвечающий за рендер UI меню для создания нового сейва
"""


class CreateNewGameMenuRender(RenderABC):
    def Render(self, screen, mouseCords):
        font = pygame.font.SysFont("Cambria", 100)

        if 200 <= mouseCords[0] <= 600 and 200 <= mouseCords[1] <= 350:
            saveNameInputRect = pygame.draw.rect(screen, (200, 200, 200), (200, 200, 400, 150), 10)
        else:
            saveNameInputRect = pygame.draw.rect(screen, (255, 255, 255), (200, 200, 400, 150), 10)

        ButtonsRectDict = {
            "saveNameInputRect": saveNameInputRect,
        }

        return ButtonsRectDict