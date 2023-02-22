from engine.story_engine import StoryEngine, StoryEngineException, I_StoryReader
from engine.game_state import GameState
from common.i_story_view import I_StoryView

class I_GameReaderWriter:
    def __init__(self) -> None:
        self.__game_state: GameState = GameState()

    def load(self) -> GameState:
        return self.__game_state

    def save(self, game_state: GameState) -> bool:
        self.__game_state = game_state
  

def main() -> None:
    game_reader: I_GameReaderWriter = I_GameReaderWriter()

    try:
        story_engine: StoryEngine = StoryEngine(I_StoryReader(""), I_StoryView())
        story_engine.loadGame(game_reader.load())
    except StoryEngineException as e:
        print(f"Stroy engine exception: {e.code} - {e.description}")
        return

if __name__ == "__main__":
    main()