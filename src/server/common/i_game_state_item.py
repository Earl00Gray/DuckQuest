from enum import Enum
from abc import ABC, abstractmethod

class GameStateItemType(Enum):
    UNKNOWN = 0
    HISTORY = 1
    CONTEXT = 2
    CHARACTER = 3
    INVENTORY = 4

class I_GameStateItem(ABC):
    def __init__(self, type: GameStateItemType = GameStateItemType.UNKNOWN) -> None:
        self.__m_type = type
    
    @property
    def type(self) -> GameStateItemType:
        return self.__m_type
    
    @abstractmethod
    def serialize(self) -> dict:
        pass

    @abstractmethod
    def deserialize(dect_in: dict):
        pass