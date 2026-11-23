import pygame
import time
pygame.font.init()


from Game.Scripts.GameState.Render.BaseRenderABSClass import RenderABC


"""
Класс, отвечающий за рендер UI меню для создания нового сейва
"""


class CreateNewGameMenuRender(RenderABC):
    def __init__(self):
        super().__init__()

        self.Time = {"lastCaretUpdate": 0}
        self.Curete = False

    def Render(self, screen, mouseCords, saveData, inputData):
        font = pygame.font.SysFont("Cambria", 100)

        mouseRect = pygame.rect.Rect(mouseCords[0], mouseCords[1], 1, 1)

        #SaveNameInput
        saveNameInputRect = pygame.draw.rect(screen, (255, 255, 255), (200, 50, 1000, 150), 10)
        if mouseRect.colliderect(saveNameInputRect) or inputData["inputField"] == "SaveName":
            saveNameInputRect = pygame.draw.rect(screen, (170, 170, 170), (200, 50, 1000, 150), 10)

        text = font.render(f"{saveData["saveName"]}", True, (225, 225, 225))

        if inputData["inputField"] == "SaveName":
            if self.Curete == True:
                text = font.render(f"{saveData["saveName"]}|", True, (225, 225, 225))
                if time.time() - self.Time["lastCaretUpdate"] >= 0.5:
                    self.Curete = False
                    self.Time["lastCaretUpdate"] = time.time()

            else:
                text = font.render(f"{saveData["saveName"]}", True, (225, 225, 225))
                if time.time() - self.Time["lastCaretUpdate"] >= 0.5:
                    self.Curete = True
                    self.Time["lastCaretUpdate"] = time.time()

        screen.blit(text, (220, 70))


        #FoodCoefSegmentControl
        foodCoefSegmentControlRect = pygame.draw.rect(screen, (255, 255, 255), (200, 275, 1000, 150), 10)

        text = font.render(f"0.5", True, (225, 225, 225))
        food0_5CoefSegmentControlRect = pygame.draw.rect(screen, (255, 255, 255), (200, 275, 200, 150), 10)
        if mouseRect.colliderect(food0_5CoefSegmentControlRect) or saveData["foodCoef"] == 0.5:
            food0_5CoefSegmentControlRect = pygame.draw.rect(screen, (170, 170, 170), (200, 275, 200, 150), 10)
        screen.blit(text, (235, 275))

        text = font.render(f"0.75", True, (225, 225, 225))
        food0_75CoefSegmentControlRect = pygame.draw.rect(screen, (255, 255, 255), (400, 275, 200, 150), 10)
        if mouseRect.colliderect(food0_75CoefSegmentControlRect) or saveData["foodCoef"] == 0.75:
            food0_75CoefSegmentControlRect = pygame.draw.rect(screen, (170, 170, 170), (400, 275, 200, 150), 10)
        screen.blit(text, (410, 275))

        text = font.render(f"1", True, (225, 225, 225))
        food1CoefSegmentControlRect = pygame.draw.rect(screen, (255, 255, 255), (600, 275, 200, 150), 10)
        if mouseRect.colliderect(food1CoefSegmentControlRect) or saveData["foodCoef"] == 1:
            food1CoefSegmentControlRect = pygame.draw.rect(screen, (170, 170, 170), (600, 275, 200, 150), 10)
        screen.blit(text, (670, 275))

        text = font.render(f"1.25", True, (225, 225, 225))
        food1_25CoefSegmentControlRect = pygame.draw.rect(screen, (255, 255, 255), (800, 275, 200, 150), 10)
        if mouseRect.colliderect(food1_25CoefSegmentControlRect) or saveData["foodCoef"] == 1.25:
            food1_25CoefSegmentControlRect = pygame.draw.rect(screen, (170, 170, 170), (800, 275, 200, 150), 10)
        screen.blit(text, (810, 275))

        text = font.render(f"2", True, (225, 225, 225))
        food2CoefSegmentControlRect = pygame.draw.rect(screen, (255, 255, 255), (1000, 275, 200, 150), 10)
        if mouseRect.colliderect(food2CoefSegmentControlRect) or saveData["foodCoef"] == 2:
            food2CoefSegmentControlRect = pygame.draw.rect(screen, (170, 170, 170), (1000, 275, 200, 150), 10)
        screen.blit(text, (1070, 275))


        #EnemyCoefSegmentControl
        foodCoefSegmentControlRect = pygame.draw.rect(screen, (255, 255, 255), (200, 525, 1000, 150), 10)

        text = font.render(f"0.5", True, (225, 225, 225))
        enemy0_5CoefSegmentControlRect = pygame.draw.rect(screen, (255, 255, 255), (200, 525, 200, 150), 10)
        if mouseRect.colliderect(enemy0_5CoefSegmentControlRect) or saveData["enemyCoef"] == 0.5:
            enemy0_5CoefSegmentControlRect = pygame.draw.rect(screen, (170, 170, 170), (200, 525, 200, 150), 10)
        screen.blit(text, (235, 525))

        text = font.render(f"0.75", True, (225, 225, 225))
        enemy0_75CoefSegmentControlRect = pygame.draw.rect(screen, (255, 255, 255), (400, 525, 200, 150), 10)
        if mouseRect.colliderect(enemy0_75CoefSegmentControlRect) or saveData["enemyCoef"] == 0.75:
            enemy0_75CoefSegmentControlRect = pygame.draw.rect(screen, (170, 170, 170), (400, 525, 200, 150), 10)
        screen.blit(text, (410, 525))

        text = font.render(f"1", True, (225, 225, 225))
        enemy1CoefSegmentControlRect = pygame.draw.rect(screen, (255, 255, 255), (600, 525, 200, 150), 10)
        if mouseRect.colliderect(enemy1CoefSegmentControlRect) or saveData["enemyCoef"] == 1:
            enemy1CoefSegmentControlRect = pygame.draw.rect(screen, (170, 170, 170), (600, 525, 200, 150), 10)
        screen.blit(text, (670, 525))

        text = font.render(f"1.25", True, (225, 225, 225))
        enemy1_25CoefSegmentControlRect = pygame.draw.rect(screen, (255, 255, 255), (800, 525, 200, 150), 10)
        if mouseRect.colliderect(enemy1_25CoefSegmentControlRect) or saveData["enemyCoef"] == 1.25:
            enemy1_25CoefSegmentControlRect = pygame.draw.rect(screen, (170, 170, 170), (800, 525, 200, 150), 10)
        screen.blit(text, (810, 525))

        text = font.render(f"2", True, (225, 225, 225))
        enemy2CoefSegmentControlRect = pygame.draw.rect(screen, (255, 255, 255), (1000, 525, 200, 150), 10)
        if mouseRect.colliderect(enemy2CoefSegmentControlRect) or saveData["enemyCoef"] == 2:
            enemy2CoefSegmentControlRect = pygame.draw.rect(screen, (170, 170, 170), (1000, 525, 200, 150), 10)
        screen.blit(text, (1070, 525))

        ButtonsRectDict = {
            "saveNameInputRect": saveNameInputRect,

            "food0_5CoefSegmentControlRect": food0_5CoefSegmentControlRect,
            "food0_75CoefSegmentControlRect": food0_75CoefSegmentControlRect,
            "food1CoefSegmentControlRect": food1CoefSegmentControlRect,
            "food1_25CoefSegmentControlRect": food1_25CoefSegmentControlRect,
            "food2CoefSegmentControlRect": food2CoefSegmentControlRect,

            "enemy0_5CoefSegmentControlRect": enemy0_5CoefSegmentControlRect,
            "enemy0_75CoefSegmentControlRect": enemy0_75CoefSegmentControlRect,
            "enemy1CoefSegmentControlRect": enemy1CoefSegmentControlRect,
            "enemy1_25CoefSegmentControlRect": enemy1_25CoefSegmentControlRect,
            "enemy2CoefSegmentControlRect": enemy2CoefSegmentControlRect,
        }

        return ButtonsRectDict