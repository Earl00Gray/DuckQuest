from typing import Dict, List, Any
from common.i_game_state_item import I_GameStateItem, GameStateItemType
from common.I_Result import I_Result

class History(I_GameStateItem):
    def __init__(self) -> None:
        super().__init__(GameStateItemType.HISTORY)
        self.__m_step_dict: Dict[int, List[I_Result]]
  
    def appendStep(self, step_res_lst: List[I_Result]) -> None:
        pass

    def getStep(step_id: int) -> List[I_Result]:
        pass

class Context(I_GameStateItem): # for save expereance and relationship
    def __init__(self) -> None:
        super().__init__(GameStateItemType.CONTEXT)
        self.__m_var_dict: Dict[str, Any]
  
    def getVar(var_name: str) -> Any:
        pass

    def setVar(var_name: str, var_value: Any) -> None:
        pass

class Character(I_GameStateItem): #for save character state
    def __init__(self) -> None:
        super().__init__(GameStateItemType.CHARACTER)
        self.__m_var_dict: Dict[str, Any]
  
    def getVar(var_name: str) -> Any:
        pass

    def setVar(var_name: str, var_value: Any) -> None:
        pass

class InventoryItem: #TODO: blob
    pass

class Inventory(I_GameStateItem):
    def __init__(self) -> None:
        super().__init__(GameStateItemType.INVENTORY)
        self.__m_loot_dict: Dict[int, InventoryItem]

        def getLoot(loot_id: int) -> InventoryItem: #TODO: think about it
            pass

        def getLootLst(loot_id: int) -> List[InventoryItem]:
            pass

        def addLoot(loot_id: int) -> None:
            pass

        def rmLoot(loot_id: int) -> None:
            pass