import pygame
from abc import ABC, abstractmethod


"""
Абстрактный класс, который будет использоваться для низкоуроневых классов
"""


class HandlerABC(ABC):
    @abstractmethod
    def Handle(self):
        pass