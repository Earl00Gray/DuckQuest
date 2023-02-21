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

    def getStartStepId(self, needDebugPrint: bool = False) -> str:
        value, hasValue = self.__attrValue(
            "start_step_id", self.__loadedData)
        if not hasValue:
            return str()
        return value

    def getItem(self, stepId: int) -> tuple():  # I_Item, bool
        stepList, hasStepListAttribute = self.__attrValue(
            "step_lst", self.__loadedData)
        if not hasStepListAttribute:
            return None, False

        for stepItem in stepList:
            stepItemId, hasStepId = self.__attrValue("step_id", stepItem)
            if stepItemId == stepId:
                item = StepItem()
                item.text, hasText = self.__attrValue("text", stepItem)
                _, item.isFinishStep = self.__attrValue(
                    "is_finish_step", stepItem, False)
                item.actions = self.__getActionList(stepItem)
                return item, True
        return None, False

    # private
    def __getActionList(self, stepItem: dict) -> tuple():  # dict, bool
        actionsList, hasActionList = self.__attrValue("actions", stepItem)
        if not hasActionList:
            return dict(), False

        actions = list()
        for actionItem in actionsList:
            actions.append(self.__getAction(actionItem))
        return actions, True

    def __getAction(self, actionsData: dict) -> tuple():  # I_Actions, bool
        actionType, hasActionType = self.__attrValue("type", actionsData)

        if actionType == "select":
            action = SelectActions()
            action.id, hasActionId = self.__attrValue("id", actionsData)

            actionValueList, hasActionValueList = self.__attrValue(
                "value_lst", actionsData)
            if hasActionValueList:
                action.valueList = self.__getActionValue(actionValueList)
            return action, True
        else:
            print(
                f"Unknown action type '{ actionType }' in '{ self.__loadedFilePath }'")
            return None, False

    def __getActionValue(self, valueList: list) -> list:
        valueItems = list()
        for valueItem in valueList:
            actionValueItem = ActionValueItem()
            actionValueItem.label, hasActionValueItemLabel = self.__attrValue(
                "label", valueItem)
            actionValueItem.value, hasActionValueItemValue = self.__attrValue(
                "value", valueItem)

            resultList, hasResultList = self.__attrValue("results", valueItem)
            if hasResultList:
                for resultItem in resultList:
                    actionValueItem.resultList.append(
                        self.__getResultItem(resultItem))

            valueItems.append(actionValueItem)
        return valueItems

    def __getResultItem(self, resultData: dict) -> I_Result:
        resultType, hasResultType = self.__attrValue("type", resultData)
        if resultType == "go_to":
            resultItem = GoToResult()
            resultItem.nextStepId, hasData = self.__attrValue(
                "next_step_id", resultData)
            return resultItem
        elif resultType == "loot":
            resultItem = LootResult()
            resultItem.lootId, hasData = self.__attrValue("id", resultData)
            return resultItem
        elif resultType == "expereance":
            resultItem = ExpereanceResult()
            resultItem.var, hasData = self.__attrValue("var", resultData)
            resultItem.operator, hasData = self.__attrValue(
                "operation", resultData)
            resultItem.value, hasData = self.__attrValue("value", resultData)
            return resultItem
        else:
            print(f"Unknown result type {type} in {self.__loadedFilePath}")
            return None

    def __attrValue(self, attributeName: str, where: dict, needPrint: bool = True) -> tuple():  # dict, bool
        if attributeName in where:
            return where[attributeName], True
        else:
            if needPrint:
                print(f"Attribute {attributeName} - not found in {where}")
            return None, False
