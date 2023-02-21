from .i_action import I_Actions, ActionType


class SelectActions(I_Actions):
    def __init__(selt):
        super().__init__(ActionType.SELECT)
