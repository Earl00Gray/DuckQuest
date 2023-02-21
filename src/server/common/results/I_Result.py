from strenum import StrEnum


class ResultType(StrEnum):
    GO_TO = "go_to"
    LOOT = "loot"
    EXPEREANCE = "expereance"


class I_Result:
    def __init__(self, type: ResultType):
        self.__type = type

    def getType(self) -> ResultType:
        return self.__type
