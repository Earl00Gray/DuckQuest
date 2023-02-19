from .I_Result import I_Result, ResultType


class GoToResult(I_Result):
    def __init__(self):
        super().__init__(ResultType.GO_TO)
        self.__nextStepId: int = 0

    @property
    def nextStepId(self) -> int:
        return self.__nextStepId
