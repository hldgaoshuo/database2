from enum import IntEnum, auto


BYTES_VALUE_TYPE = 1


class ValueType(IntEnum):
    INT = auto()
    STRING = auto()
    BOOL = auto()


class Value:

    def __init__(self, value_type: ValueType, content: int | str | bool) -> None:
        self.value_type: ValueType = value_type
        self.content: int | str = content

    def  __bytes__(self) -> bytes:
        raise NotImplementedError

    def __eq__(self, other: 'Value') -> bool:
        return  (
            self.value_type == other.value_type and
            self.content == other.content
        )
