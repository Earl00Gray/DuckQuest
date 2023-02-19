import yaml
from strenum import StrEnum
from .i_story_reader import I_StoryReader
from ..items.i_item import I_Item, StepItem
from ..items.actions.i_action import I_Actions, ActionType, ActionValueItem
from ..items.actions.select_action import SelectActions
from server.common.results.I_Result import I_Result
from server.common.results.goto_result import GoToResult
from server.common.results.loot_result import LootResult
from server.common.results.expereance_result import ExpereanceResult


class YamlStoryReader(I_StoryReader):
    def __init__(self):
        pass

    def load(self, pathStoryConfig: str, needDebugPrintContent: bool = False) -> None:
        with open(pathStoryConfig) as file:
            self.__loadedData = yaml.load(file, Loader=yaml.FullLoader)
            self.__loadedFilePath = pathStoryConfig
            if needDebugPrintContent:
                print(self.__loadedData)

    def getStartStepId(self) -> str:
        value, hasValue = self.__getAttributeValue(
            "start_step_id", self.__loadedData)
        if not hasValue:
            return ""
        return value

    def getItem(self, stepId: int) -> I_Item:
        pass

    def getItem(self, stepId: int) -> tuple():  # I_Item, bool
        stepList, hasStepListAttribute = self.__getAttributeValue(
            "step_lst", self.__loadedData)
        if not hasStepListAttribute:
            return None, False

        for stepItem in stepList:
            if stepItem["step_id"] == stepId:
                item = StepItem()
                item.text = stepItem["text"]
                item.isFinishStep = "is_finish_step" in stepItem
                item.actions = self.__getActionList(stepItem)
                return item, True
        return None, False

    # private
    def __getAttributeValue(self, attributeName: str, where: dict, needPrint: bool = True) -> tuple():  # dict, bool
        if attributeName in where:
            return where[attributeName], True
        else:
            if needPrint:
                print(f"Element {attributeName} - not found in {where}")
            return None, False

    def __getActionList(self, stepItem: dict) -> tuple():  # dict, bool
        actions = list()
        for actionItem in stepItem["actions"]:
            actions.append(self.__getAction(actionItem))
        return actions, True

    def __getAction(self, actionsData: dict) -> tuple():  # I_Actions, bool
        actionType = actionsData["type"]
        if actionsData["type"] == ActionType.SELECT:
            action = SelectActions()
            action.id = actionsData["id"]
            action.valueList = self.__getActionValue(action["value_lst"])
        else:
            print(
                f"Unknown action type {actionType} in {self.__loadedFilePath}")
            return

    def __getActionValue(self, valueList: list) -> list:
        valueItems = list()
        for valueItem in valueList:
            actionValueItem = ActionValueItem()
            actionValueItem.label = valueItem["label"]
            actionValueItem.value = valueItem["value"]

            for resultItem in valueItem["results"]:
                actionValueItem.resultList.append(
                    self.__getResultItem(resultItem))

            valueItems.append(actionValueItem)
        return valueItems

    def __getResultItem(self, resultData: dict) -> I_Result:
        resultType = resultData["type"]
        if resultType == "go_to":
            resultItem = GoToResult()
            resultItem.nextStepId = resultData["next_step_id"]
            return resultItem
        elif resultType == "loot":
            resultItem = LootResult()
            resultItem.lootId = resultData["id"]
            return resultItem
        elif resultType == "expereance":
            resultItem = ExpereanceResult()
            resultItem.var = resultData["var"]
            resultItem.operation = resultData["operation"]
            resultItem.value = resultData["value"]
            return resultItem
        else:
            print(f"Unknown result type {type} in {self.__loadedFilePath}")
            return None
