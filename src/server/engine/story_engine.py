from enum import Enum
from typing import List

from game_state import GameState, HistoryItem
from action_result import GoToResult, ResultType

class StoryItem:
    pass

class I_StoryReader:
    def __init__(self, story_config_path: str = "") -> None:
        self.__m_story_config_path: str
        self.load(story_config_path)

    def load(self, story_config_path: str) -> bool:
        self.__m_story_config_path = story_config_path
        return True

    def getItem(self, step_id: int) -> StoryItem:
        return StoryItem()

class StoryEngineError(Enum):
    UNKNOWN_ERROR = -1
    SUCCESS = 0
    NOT_VALID_GAME_STATE_ERROR = 1
    READ_GAME_STATE_ERROR = 2

class StoryEngine:
    def __init__(self) -> None:
        self.__m_game_state: GameState = None
        self.__m_in_progress: bool = False
        self.__m_story_reader: I_StoryReader = I_StoryReader()
        self.__m_current_story_item: StoryItem = None

    def loadGame(self, gameState: GameState) -> None:
        if gameState is None:
            raise Exception(StoryEngineError.NOT_VALID_GAME_STATE_ERROR, "Game state object is None")

        if self.__m_in_progress:
            self.__stopGame()

        self.__m_game_state = gameState
       
        if not self.__read_current_step():
            raise Exception(StoryEngineError.READ_GAME_STATE_ERROR, "Reading game state error")
        
        self.__startGame()

    def saveGame(self) -> GameState:
        return self.__m_game_state

    def __read_current_step(self) -> bool:
        if self.__m_game_state is None:
            return False

        if not self.__m_story_reader.load(self.__m_game_state.story_config_path):
            return False

        current_step_id: int = self.__read_current_step_id()

        if current_step_id is None:
            return False
        
        current_story_item: StoryItem = self.__m_story_reader.getItem(current_step_id)

        if not current_story_item:
            return False

        self.__m_current_story_item = current_story_item

        return True

    def __read_current_step_id(self) -> int:
        last_history_item: HistoryItem = self.__m_game_state.history.getStep(-1)

        if last_history_item is None:
            return None

        last_goto_result_lst: List[GoToResult] = [goto_result for goto_result in last_history_item.result_lst if goto_result.getType is ResultType.GO_TO]

        if not last_goto_result_lst:
            return None

        return last_goto_result_lst[0].next_step_id
       
    def __stopGame(self) -> None:
        self.__m_in_progress = False
        

    def __startGame(self) -> None:
        self.__m_in_progress = True
        

  