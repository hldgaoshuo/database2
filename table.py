from value.value import ValueType


class Table:

    def __init__(self, name: str):
        self.name: str = name
        self.col_names: list[str] = []
        self.col_types: list[ValueType] = []
