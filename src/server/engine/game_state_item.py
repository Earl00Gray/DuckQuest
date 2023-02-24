from typing import Dict, List, Any
from dataclasses import dataclass, field

from server.common.i_game_state_item import I_GameStateItem, GameStateItemType
from server.common.results.I_Result import I_Result
from server.engine.action_result import ExpereanceOperatorType

@dataclass
class HistoryItem:
    step_id: int = field(default = -1)
    result_lst: List[I_Result] = field(default_factory = List[I_Result])

class History(I_GameStateItem):
    def __init__(self) -> None:
        super().__init__(GameStateItemType.HISTORY)
        self.__step_lst: List[HistoryItem] = []
  
    def appendStep(self, history_item: HistoryItem) -> None:
        self.__step_lst.append(history_item)

    def getStep(self, index: int) -> HistoryItem:
        if len(self.__step_lst) >= index:
            return self.__step_lst[index:1]
        
        return None
    
    def serialize(self) -> dict:
        pass

    def deserialize(dict_in: dict):
        pass

class Context(I_GameStateItem): # for save expereance and relationship
    prefix = "Context"

    def __init__(self) -> None:
        super().__init__(GameStateItemType.CONTEXT)
        self.__var_dict: Dict[str, Any] = {}
  
    def getVar(self, var_name: str) -> Any:
        if var_name in self.__var_dict:
            return self.__var_dict[var_name]

        return None

    def setVar(self, var_name: str, var_value: Any) -> None:
        self.__var_dict[var_name] = var_value

    def applyOperation(self, var_name: str, var_value: Any, operation: ExpereanceOperatorType) -> None:
        if operation is ExpereanceOperatorType.ADD:
            if var_name in self.__var_dict:
                self.__var_dict[var_name] += var_value
            else:
                self.__var_dict[var_name] = var_value

        elif operation is ExpereanceOperatorType.SET:
            self.__var_dict[var_name] = var_value

        elif operation is ExpereanceOperatorType.SUB:
            if var_name in self.__var_dict:
                self.__var_dict[var_name] -= var_value
    
    def serialize(self) -> dict:
        pass

    def deserialize(dict_in: dict):
        pass

class Character(I_GameStateItem): #for save character state
    prefix = "Character"

    def __init__(self) -> None:
        super().__init__(GameStateItemType.CHARACTER)
        self.__var_dict: Dict[str, Any] = {}
  
    def getVar(self, var_name: str) -> Any:
        if var_name in self.__var_dict:
            return self.__var_dict[var_name]

    def setVar(self, var_name: str, var_value: Any) -> None:
        self.__var_dict[var_name] = var_value

    def applyOperation(self, var_name: str, var_value: Any, operation: ExpereanceOperatorType) -> None:
        if operation is ExpereanceOperatorType.ADD:
            if var_name in self.__var_dict:
                self.__var_dict[var_name] += var_value
            else:
                self.__var_dict[var_name] = var_value

        elif operation is ExpereanceOperatorType.SET:
            self.__var_dict[var_name] = var_value

        elif operation is ExpereanceOperatorType.SUB:
            if var_name in self.__var_dict:
                self.__var_dict[var_name] -= var_value

    
    def serialize(self) -> dict:
        pass

    def deserialize(dict_in: dict):
        pass

class Inventory(I_GameStateItem):
    def __init__(self) -> None:
        super().__init__(GameStateItemType.INVENTORY)
        self.__loot_lst: List[int] = []

    def getLoot(self, index: int) -> int: ##TODO: think about it
        if len(self.__loot_lst) >= index:
            return self.__loot_lst[index]

        return None

    def getLootLst(self) -> List[int]:
        return self.__loot_lst

    def addLoot(self, loot_id: int) -> None:
        self.__loot_lst.append(loot_id)

    def rmLoot(self, loot_id: int) -> None:
        if loot_id in self.__loot_lst:
            self.__loot_lst.remove(loot_id)

    
    def serialize(self) -> dict:
        pass

    def deserialize(dict_in: dict):
        pass
