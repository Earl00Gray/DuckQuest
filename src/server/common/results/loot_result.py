from .I_Result import I_Result, ResultType


class LootResult(I_Result):
    def __init__(self):
        self.m_type = ResultType.LOOT

    @property
    def lootId(self) -> str:
        return self.__lootId
