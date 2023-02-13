from .I_Result import I_Result, ResultType


class GoToResult(I_Result):
    def __init__(self):
        self.m_type = ResultType.GO_TO

    @property
    def nextStepId(self) -> int:
        return self.__nextStepId
