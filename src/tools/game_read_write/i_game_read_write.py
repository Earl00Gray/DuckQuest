from abc import ABC, abstractmethod
from server.engine.game_state import GameState


class I_GameReadWriter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def loadGameState(self) -> GameState:
        pass

    @abstractmethod
    def saveGameState(self, gameState: GameState) -> bool:
        pass
