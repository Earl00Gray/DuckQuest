from .I_Result import I_Result, ResultType


class LootResult(I_Result):
    def __init__(self):
        super().__init__(ResultType.LOOT)
        self.__lootId: str = ""

    @property
    def lootId(self) -> str:
        return self.__lootId
