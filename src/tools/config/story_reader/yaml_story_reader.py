import yaml
from .i_story_reader import I_StoryReader
from ..items.i_item import I_Item, StepItem
from ..items.actions.i_action import SelectAction, ActionValueItem
from server.common.results.I_Result import I_Result
from server.common.results.goto_result import GoToResult
from server.common.results.loot_result import LootResult
from server.common.results.expereance_result import ExpereanceResult


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
                        # TODO: check is end step

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

                                results = list()
                                for key, valueResult in valueListItem["results"]:
                                    results.append(
                                        self.__getResultItem(valueResult["type"], valueResult))

                                action.actions.append(results)

                            actions.append(action)
                return item

    def __getResultItem(self, type: str, data: dict) -> I_Result:
        if type == "go_to":
            resultItem = GoToResult()
            resultItem.nextStepId = data["next_step_id"]
            return resultItem
        elif type == "loot":
            resultItem = LootResult()
            resultItem.lootId = data["id"]
            return resultItem
        elif type == "expereance":
            resultItem = ExpereanceResult()
            resultItem.var = data["var"]
            resultItem.operation = data["operation"]
            resultItem.value = data["value"]
            return resultItem
