import yaml
from tools.game_read_write.i_game_read_write import I_GameReadWriter
from server.engine.game_state import GameState
from server.engine.game_state_item import History, Context, Character, Inventory
from server.common.i_game_state_item import I_GameStateItem


class YamlGameReadWrite(I_GameReadWriter):
    def __init__(self):
        super().__init__()

    def loadGameState(self) -> GameState:
        pass

    def saveGameState(self, gameState: GameState) -> bool:
        self.__saveGameStateItem("history", gameState.history)
        self.__saveGameStateItem("context", gameState.context)
        self.__saveGameStateItem("character", gameState.character)
        self.__saveGameStateItem("inventory", gameState.inventory)

    def __saveGameStateItem(self, gameStateItemName: str, gameStateItem: I_GameStateItem):
        yamlStr: str = yaml.dump(gameStateItem.serialize())

        file = open("game_state.yaml", "a", encoding="utf-8")
        file.write(yamlStr)
        file.close()
