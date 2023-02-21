from strenum import StrEnum
from abc import ABC, abstractmethod


class ActionType(StrEnum):
    SELECT = "select"
    UNKNOWN = "unknown"


class ActionValueItem:
    def __init__(self) -> None:
        
        self.__label: str = ""
        self.__value: str = ""
        self.__result_lst: list = []

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def resultList(self) -> list:
        return self.__result_lst

    @resultList.setter
    def resultList(self, resultList: list):
        self.__result_lst = resultList


class I_Actions(ABC):
    def __init__(self, type: ActionType = ActionType.UNKNOWN) -> None:
        self.__type: ActionType = type
        self.__id: int = 0
        self.__valueList: list = []

    @property
    def type(self) -> ActionType:
        return self.__type

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def valueList(self) -> list:  # ActionValueItem
        return self.__valueList

    @valueList.setter
    def valueList(self, valueList: list):
        self.__valueList = valueList
