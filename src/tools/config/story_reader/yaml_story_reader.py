import yaml
from .i_story_reader import I_StoryReader
from ..items.i_item import I_Item, StepItem
from ..items.actions.i_action import SelectAction, ActionValueItem


class YamlStoryReader(I_StoryReader):
    def __init__(self):
        pass

    def load(self, pathStoryConfig: str) -> None:
        with open(pathStoryConfig) as file:
            self.__loadedData = yaml.load(file, Loader=yaml.FullLoader)
            self.__loadedPath = pathStoryConfig

    def getStartStepId(self) -> str:
        if "start_step_id" in self.__loadedData:
            return self.__loadedData["start_step_id"]
        else:
            print(
                f"Element 'start_step_id' - not found in {self.__loadedPath}")
            return 0

    def getItem(self, stepId: int) -> I_Item:
        for key, value in self.__loadedData.items():
            if isinstance(value, dict):
                for key, valueNested in value.items():
                    if key == "-step." + str(stepId):
                        item = StepItem()
                        item.text = valueNested["text"]
                        
                        for key, valueAction in valueNested["-actions"]:
                            actions = list()
                            action = SelectAction()
                            action.type = valueAction["type"]
                            action.id = valueAction["id"]

                            for key, valueListItem in valueAction["value_lst"]:
                                valueItems = list()
                                valueItem = ActionValueItem()
                                valueItem.label = valueListItem["label"]
                                valueItem.value = valueListItem["value"]

                                for key, valueResult in valueListItem["results"]:
                                    
                            actions.append(action)
                return item
