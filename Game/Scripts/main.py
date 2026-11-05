import pygame
pygame.font.init()


from Game.Scripts.GameState.GameState import GameState
from Game.Scripts.GameState.Render.Render import Render
from Game.Scripts.GameState.Handlers.Handler import Handler

"""
При использовнии движка pygame, есть такая параша - Исменение размера текста, приложений и других элементов, из-за этого 
окно Pygame может быть куда меньше, чем надо => игрок не видит половину ока игры, так что включаем 100% изменение, т.к. 
я хер знает, как это исправить
"""

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.gameState = GameState()
        self.render = Render(self.gameState.screen)
        self.handler = Handler()

    def Run(self):

        pygame.display.set_caption("PATTERNS")

        while True:
            dt = self.clock.tick(60) / 1000.0

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

            self.gameState.CurrentButtonsRectDictSetter(self.render.Render(self.gameState.currentScreenName, self.gameState.mouseCords))
            self.handler.Handle(self.gameState.mouseCords, self.gameState.mouseButtonsPressed, self.gameState.buttonsRectDict, self.gameState.currentScreenName,
                                self.gameState.CurrentScreenNameSetter)
            self.gameState.EveryTickUpdateData()

            pygame.display.flip()


if __name__ == '__main__':
    game = Game()
    game.Run()