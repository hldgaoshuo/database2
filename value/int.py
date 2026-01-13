from io import BytesIO
from value.value import Value, ValueType, BYTES_VALUE_TYPE

BYTES_INT = 8


class Int(Value):

    def __init__(self, content: int) -> None:
        super().__init__(ValueType.INT, content)

    def __bytes__(self) -> bytes:
        value_type_row = self.value_type.to_bytes(length=BYTES_VALUE_TYPE, byteorder='big')
        content_row = self.content.to_bytes(length=BYTES_INT, byteorder='big')
        result = value_type_row + content_row
        return result

    def __repr__(self):
        return f'Int({self.content})'


def new_int(content: int) -> Int:
    return Int(content)


def new_int_from_bytes(buf: BytesIO) -> Int:
    bs = buf.read(BYTES_INT)
    content = int.from_bytes(bs, byteorder='big')
    return Int(content)
