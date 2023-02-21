from strenum import StrEnum
from abc import ABC, abstractmethod


class StoryItemType(StrEnum):
    STEP = "step"
    INVENTORY = "inventory"
    UNKNOWN = "unknown"

# interface


class I_Item(ABC):
    def __init__(self, type: StoryItemType = StoryItemType.UNKNOWN) -> None:
        self.__type = type
        self.__id = 0

    @property
    def type(self) -> StoryItemType:
        return self.__type

    @property
    def id(self) -> int:
        return self.__id

# step item


class StepItem(I_Item):
    def __init__(self):
        super().__init__(StoryItemType.STEP)
        self.__text = ""
        self.__actions = []
        self.__isFinishStep = False

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def isFinishStep(self) -> bool:
        return self.__isFinishStep

    @isFinishStep.setter
    def isFinishStep(self, isFinishStep: bool):
        self.__isFinishStep = isFinishStep

    @property
    def actions(self) -> list:
        return self.__actions

    @actions.setter
    def actions(self, actions: list):
        self.__actions = actions


# inventory item


class InventoryItem(I_Item):
    def __init__(self):
        super().__init__(StoryItemType.INVENTORY)
        self.__inventoryType = ""
        self.__props = {}

    @property
    def inventoryType(self) -> str:
        return self.__inventoryType

    @property
    def props(self) -> dict:
        return self.__props
