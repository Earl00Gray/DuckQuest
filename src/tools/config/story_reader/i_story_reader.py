from abc import ABC, abstractmethod

from ..items.i_item import I_Item


class I_StoryReader(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def load(self, pathStoryConfig: str) -> None:
        pass

    @abstractmethod
    def getStartStepId(self) -> str:
        pass

    @abstractmethod
    def getItem(self, id: int) -> I_Item:
        pass
