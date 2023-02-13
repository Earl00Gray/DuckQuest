from enum import Enum
from .I_Result import I_Result, ResultType


class OperatorType(Enum):
    Add = 0
    Sub = 1
    Set = 2


class ExpereanceResult(I_Result):
    def __init__(self):
        self.m_type = ResultType.EXPEREANCE

    @property
    def var(self) -> str:
        return self.__var

    @property
    def operator(self) -> OperatorType:
        return self.__operator

    @property
    def value(self) -> int:
        return self.__value
