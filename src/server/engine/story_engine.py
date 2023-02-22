from enum import Enum
from typing import List

from engine.game_state import GameState, HistoryItem
from engine.action_result import GoToResult, ResultType
from common.i_story_view import I_StoryView

class StoryItem:
    pass

class I_StoryReader:
    def __init__(self, story_config_path: str = "") -> None:
        self.__story_config_path: str = ""
        self.load(story_config_path)

    def load(self, story_config_path: str) -> bool:
        self.__story_config_path = story_config_path
        return True

    def getItem(self, step_id: int) -> StoryItem:
        return StoryItem()

    def getStartStepId(self) -> int:
        return 0



class StoryEngineError(Enum):
    UNKNOWN_ERROR = -1
    SUCCESS = 0
    NOT_VALID_GAME_STATE_ERROR = 1
    READ_GAME_STATE_ERROR = 2
    START_GAME_ERROR = 3
    ENGINE_INITIALIZATION_ERROR = 4

class StoryEngineException(Exception):
    def __init__(self, e_code: StoryEngineError, desc: str = "") -> None:
        super().__init__(e_code, desc)

        self.__e_code: StoryEngineError = e_code
        self.__description: str = desc

    @property
    def code(self) -> StoryEngineError:
        return self.__e_code

    @property
    def description(self) -> str:
        return self.__description

class StoryEngine:
    def __init__(self, story_reader: I_StoryReader = None, story_view: I_StoryView = None) -> None:
        if not story_reader:
            raise StoryEngineException(StoryEngineError.ENGINE_INITIALIZATION_ERROR, "Story reader not specified")
        
        if not story_view:
            raise StoryEngineException(StoryEngineError.ENGINE_INITIALIZATION_ERROR, "Story viewer not specified")
        
        self.__game_state: GameState = None
        self.__in_progress: bool = False
        self.__story_reader: I_StoryReader = story_reader
        self.__story_view: I_StoryView = story_view
        self.__current_story_item: StoryItem = None

    def newGame(self, path: str) -> None:
        self.loadGame(GameState(path))

    def loadGame(self, gameState: GameState) -> None:
        if gameState is None:
            raise StoryEngineException(StoryEngineError.NOT_VALID_GAME_STATE_ERROR, "Game state object is None")

        if self.__in_progress:
            self.__stopGame()

        self.__game_state = gameState
        
        if not self.__load_current_step():
            raise StoryEngineException(StoryEngineError.READ_GAME_STATE_ERROR, "Reading game state error")
        
        self.__startGame()

    def saveGame(self) -> GameState:
        return self.__game_state

    def __load_current_step(self) -> bool:
        if self.__game_state is None:
            return False

        if not self.__game_state.story_config_path \
        or not self.__story_reader.load(self.__game_state.story_config_path):
            return False

        current_step_id: int = self.__load_current_step_id()

        if current_step_id is None:
            return False
        
        current_story_item: StoryItem = self.__story_reader.getItem(current_step_id)

        if not current_story_item:
            return False

        self.__current_story_item = current_story_item

        return True

    def __load_current_step_id(self) -> int:
        if not self.__game_state.history:
            return self.__story_reader.getStartStepId()

        last_history_item: HistoryItem = self.__game_state.history.getStep(-1)

        if last_history_item is None:
            return None

        last_goto_result_lst: List[GoToResult] = [goto_result for goto_result in last_history_item.result_lst if goto_result.getType() is ResultType.GO_TO]

        if not last_goto_result_lst:
            return None

        return last_goto_result_lst[0].next_step_id
       
    def __stopGame(self) -> None:
        self.__in_progress = False
        

    def __startGame(self) -> None:
        if not self.__current_story_item:
            raise StoryEngineException(StoryEngineError.START_GAME_ERROR, "Current step is not loaded")
        
        self.__in_progress = True

        self.__process()

    def __process(self) -> None:
        pass
        

  
