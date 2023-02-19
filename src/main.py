from tools.config.story_reader.yaml_story_reader import YamlStoryReader


def testYamlStoryReader():
    yamlStoryReader = YamlStoryReader()
    yamlStoryReader.load(
        "D:\\project\\text_quest\\DuckQuest.git\\test_config.yaml")
    print(f"initial step id: { yamlStoryReader.getStartStepId() }")

    item = yamlStoryReader.getItem(0)
    print(f"item.text: { item.text } ")


testYamlStoryReader()
