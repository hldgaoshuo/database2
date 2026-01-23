from value.value import Value


class Record:

    def __init__(self):
        self.cols: list[str] = []
        self.vals: list[Value] = []

    def add(self, col: str, val: Value) -> None:
        self.cols.append(col)
        self.vals.append(val)
