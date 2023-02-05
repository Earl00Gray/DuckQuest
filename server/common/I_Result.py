from strenum import StrEnum

class ResultType(StrEnum):
    GO_TO = "go_to"
    LOOT = "loot"
    EXPEREANCE = "expereance"


class I_Result:
    m_type: ResultType
    
    def getType(self) -> ResultType:
        return self.m_type
  