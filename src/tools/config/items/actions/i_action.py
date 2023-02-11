from enum import Enum
from abc import ABC, abstractmethod


class ActionValueItem:
    @property
    def label(self) -> str:
        return self.__label

    @property
    def value(self) -> str:
        return self.__value

    @property
    def resultList(self) -> list:
        return self.__result_lst


class ActionType(Enum):
    SELECT = 0
    UNKNOWN = 1

# interface


class I_Actions(ABC):
    def __init__(self, type: ActionType = ActionType.UNKNOWN) -> None:
        self.__type = type

    @property
    def type(self) -> ActionType:
        return self.__type

    @property
    def id(self) -> int:
        return self.__id

    @property
    def actions(self) -> list:
        return self.__actions

# select action


class SelectAction(I_Actions):
    def __init__(selt):
        pass
