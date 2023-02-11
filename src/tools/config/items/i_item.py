from enum import Enum
from abc import ABC, abstractmethod


class StoryItemType(Enum):
    STEP = 0
    INVENTORY = 1
    UNKNOWN = 2

# interface


class I_Item(ABC):
    def __init__(self, type: StoryItemType = StoryItemType.UNKNOWN) -> None:
        self.__type = type

    @property
    def type(self) -> StoryItemType:
        return self.__type

    @property
    def id(self) -> int:
        return self.__id

# step item


class StepItem(I_Item):
    def __init__(self):
        pass

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str) -> str:
        self.__text = text

    @property
    def actions(self) -> list:
        return self.__actions


# inventory item


class InventoryItem(I_Item):
    def __init__(self):
        pass

    @property
    def inventoryType(self) -> str:
        return self.__inventoryType

    @property
    def props(self) -> dict:
        return self.__props
