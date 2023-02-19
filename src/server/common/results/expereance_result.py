from strenum import StrEnum
from .I_Result import I_Result, ResultType


class OperatorType(StrEnum):
    Add = "add"
    Sub = "sub"
    Set = "set"


class ExpereanceResult(I_Result):
    def __init__(self):
        super().__init__(ResultType.EXPEREANCE)
        self.__var: str = ""
        self.__operator: OperatorType = OperatorType.Add
        self.__value: int = 0

    @property
    def var(self) -> str:
        return self.__var

    @property
    def operator(self) -> OperatorType:
        return self.__operator

    @property
    def value(self) -> int:
        return self.__value
