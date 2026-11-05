from abc import ABC, abstractmethod


"""
Абстрактный класс, который будет использоваться для более высокоуровневых классов
"""


class RenderABC(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def Render(self):
        pass