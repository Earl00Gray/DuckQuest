from strenum import StrEnum
from common.I_Result import I_Result, ResultType

class GoToResult(I_Result):
    def __init__(self, step_id: int) -> None:
        super().__init__(ResultType.GO_TO)
       
        self.__m_next_step_id = step_id

    @property
    def next_step_id(self) -> int:
        return self.__m_next_step_id

class LootResultType(StrEnum):
    UNKNOWN = "UNKNOWN"
    ADD = "add"
    RM = "rm"

class LootResult(I_Result):
    def __init__(self, id: str, loot_res_type: LootResultType) -> None:
        super().__init__(ResultType.LOOT)
       
        self.__m_loot_id = id
        self.__m_loot_res_type = loot_res_type

    @property
    def loot_id(self) -> str:
        return self.__m_loot_id

    @property
    def loot_res_type(self) -> LootResultType:
        return self.__m_loot_res_type
    
class ExpereanceOperatorType(StrEnum):
    UNKNOWN = "UNKNOWN"
    ADD = "add"
    SUB = "sub"
    SET = "set"

class ExpereanceResult(I_Result):
    def __init__(self, var_name: str, operator: ExpereanceOperatorType, value: float) -> None:
        super().__init__(ResultType.EXPEREANCE)
       
        self.__m_var = var_name
        self.__m_operation = operator
        self.__m_value = value
    
    @property
    def var(self) -> str:
        return self.__m_var
    
    @property
    def operation(self) -> ExpereanceOperatorType:
        return self.__m_operation
    
    @property
    def value(self) -> float:
        return self.__m_value