from enum import IntEnum, auto


class ValueType(IntEnum):
    TINY_INT = auto()
    SMALL_INT = auto()
    MEDIUM_INT = auto()
    INT = auto()
    BIG_INT = auto()
    CHAR = auto()
    VARCHAR = auto()
    TINY_TEXT = auto()
    TEXT = auto()
    MEDIUM_TEXT = auto()
    LONG_TEXT = auto()


class Value:

    def __init__(self, value_type: ValueType, content: int | str) -> None:
        self.value_type: ValueType = value_type
        self.content: int | str = content

    def  __bytes__(self) -> bytes:
        raise NotImplementedError

    def __eq__(self, other: 'Value') -> bool:
        return  (
            self.value_type == other.value_type and
            self.content == other.content
        )
