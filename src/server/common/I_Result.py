from strenum import StrEnum

class ResultType(StrEnum):
    UNKNOWN = "unknown"
    GO_TO = "go_to"
    LOOT = "loot"
    EXPEREANCE = "expereance"


class I_Result:
    def __init__(self, type:ResultType = ResultType.UNKNOWN) -> None:
        self.__m_type = type
    
    def getType(self) -> ResultType:
        return self.__m_type
  