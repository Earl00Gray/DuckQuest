from tools.config.story_reader.yaml_story_reader import YamlStoryReader
from tools.game_read_write.yaml_game_read_write import YamlGameReadWrite
from server.engine.game_state import GameState


def testYamlStoryReader():
    yamlStoryReader = YamlStoryReader()
    configPath: str = "D:\\project\\text_quest\\DuckQuest.git\\test_config.yaml"
    yamlStoryReader.load(configPath)
    print(f"initial step id: { yamlStoryReader.getStartStepId() }")

    stepId: int = 3
    item, hasItem = yamlStoryReader.getItem(stepId)
    if not hasItem:
        print(f"There is no step with id '{ stepId }' in '{ configPath }' ")
    else:
        print(f"item.text: '{ item.text }' ")


def testGameReadWrite():
    yamlGameReadWrite = YamlGameReadWrite()
    gameState = GameState()
    yamlGameReadWrite.saveGameState(gameState)


testGameReadWrite()
