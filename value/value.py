from enum import IntEnum, auto


class ValueType(IntEnum):
    TINY_INT = auto()
    SMALL_INT = auto()
    MEDIUM_INT = auto()
    INT = auto()
    BIG_INT = auto()
    CHAR = auto()


class Value:

    def __init__(self, value_type: ValueType, content: int | str, size: int) -> None:
        self.value_type: ValueType = value_type
        self.content: int | str = content
        self.size: int = size

    def  __bytes__(self) -> bytes:
        raise NotImplementedError

    def __eq__(self, other: 'Value') -> bool:
        return  (
            self.value_type == other.value_type and
            self.content == other.content and
            self.size == other.size
        )
