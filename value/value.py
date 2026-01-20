from enum import IntEnum, auto


BYTES_VALUE_TYPE = 1


class ValueType(IntEnum):
    INT = auto()
    STRING = auto()
    BOOL = auto()


class Value:

    def __eq__(self, other):
        return self.is_eq(other)

    def  __bytes__(self) -> bytes:
        return self.to_bytes()

    def __repr__(self):
        return self.show()

    def __init__(self, value_type: ValueType, content: int | str | bool):
        self.value_type: ValueType = value_type
        self.content: int | str = content

    def is_eq(self, other: 'Value') -> bool:
        return  (
            self.value_type == other.value_type and
            self.content == other.content
        )

    # protocol

    def to_bytes(self) -> bytes:
        raise NotImplementedError

    def show(self) -> str:
        raise NotImplementedError
