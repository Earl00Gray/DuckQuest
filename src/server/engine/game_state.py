from typing import List

from game_state_item import History, Context, Character, Inventory, HistoryItem
from common.I_Result import I_Result, ResultType
from action_result import LootResult, ExpereanceResult, LootResultType

class GameState:
    def __init__(self, story_config_path: str = "") -> None:
        self.__m_story_config_path: str = story_config_path
        self.__m_history: History
        self.__m_context: Context
        self.__m_character: Character
        self.__m_inventory: Inventory
  
    @property
    def story_config_path(self) -> str:
        return self.__m_story_config_path
  
    @property
    def history(self) -> History:
        return self.__m_history
  
    @property
    def context(self) -> Context:
        return self.__m_context
  
    @property
    def character(self) -> Character:
        return self.__m_character
  
    @property
    def inventory(self) -> Inventory:
        return self.__m_inventory

    def storeStep(self, step_id: int, result_lst: List[I_Result]) -> None:
        if step_id is None or result_lst is None:
            return

        self.__applyStep(HistoryItem(step_id, result_lst))

        for result_item in result_lst:
            result_item_type: ResultType = result_item.getType()
           
            if result_item_type is ResultType.LOOT:
                self.__applyLoot(result_item)
            elif result_item_type is ResultType.EXPEREANCE:
                self.__applyExpereance(result_item)

    def __applyStep(self, history_item: HistoryItem) -> None:
        if history_item is None:
            return

        self.__m_history.appendStep(history_item)

    def __applyLoot(self, result_item: LootResult) -> None:
        if result_item is None:
            return
            
        if result_item.loot_res_type is LootResultType.ADD:
            self.__m_inventory.addLoot(result_item.loot_id)
        elif result_item.loot_res_type is LootResultType.RM:
            self.__m_inventory.rmLoot(result_item.loot_id)

    def __applyExpereance(self, result_item: ExpereanceResult) -> None:
        if result_item is None:
            return

        if result_item.var.startswith(f"{Character.prefix}."):
            self.__m_character.applyOperation(result_item.var, result_item.value, result_item.operation)
        elif result_item.var.startswith(f"{Context.prefix}."):
            self.__m_context.applyOperation(result_item.var, result_item.value, result_item.operation)
        

    
