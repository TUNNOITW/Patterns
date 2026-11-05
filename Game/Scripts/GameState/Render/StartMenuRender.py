import pygame
pygame.font.init()


from Game.Scripts.GameState.Render.BaseRenderABSClass import RenderABC


"""
Класс, отвечающий за рендер UI стартового меню
"""


class StartMenuRender(RenderABC):
    def Render(self, screen, mouseCords):
        font = pygame.font.SysFont("Cambria", 100)

        if 470 <= mouseCords[0] <= 970 and 450 <= mouseCords[1] <= 600:
            newGameStartButtonRect = pygame.draw.rect(screen, (200, 200, 200), (470, 450, 500, 150),
                                                      border_radius= 10)
        else:
            newGameStartButtonRect = pygame.draw.rect(screen, (255, 255, 255), (470, 450, 500, 150),
                                                      border_radius= 10)

        if 470 <= mouseCords[0] <= 970 and 700 <= mouseCords[1] <= 850:
            loadSaveGameButtonRect = pygame.draw.rect(screen, (200, 200, 200), (470, 700, 500, 150),
                                                      border_radius= 10)
        else:
            loadSaveGameButtonRect = pygame.draw.rect(screen, (255, 255, 255), (470, 700, 500, 150),
                                                      border_radius= 10)

        text = font.render("Start", True, (0, 0, 0))
        screen.blit(text, (610, 455))

        text = font.render("Load Save", True, (0, 0, 0))
        screen.blit(text, (510, 705))

        buttonsRectDict = {
            "newGameStartButtonRect": newGameStartButtonRect,
            "loadSaveGameButtonRect": loadSaveGameButtonRect
        }

        return buttonsRectDict