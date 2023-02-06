from game_state_item import History, Context, Character, Inventory

class GameState:
    def __init__(self) -> None:
        self.__m_history: History
        self.__m_context: Context
        self.__m_character: Character
        self.__m_inventory: Inventory
  
    def storeStep(self, step_id: int, result: int, res_value: int) -> None:
        pass
