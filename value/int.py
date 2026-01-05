from io import BytesIO
from value.value import Value, ValueType


SIZE_INT = 4


class Int(Value):

    def __init__(self, content: int) -> None:
        super().__init__(ValueType.INT, content, SIZE_INT)

    def __bytes__(self) -> bytes:
        value_type_row = self.value_type.to_bytes(length=1, byteorder='big')
        content_row = self.content.to_bytes(length=self.size, byteorder='big')
        result = value_type_row + content_row
        return result


def new_int(content: int) -> Int:
    return Int(content)


def new_int_from_bytes(buf: BytesIO) -> Int:
    bs = buf.read(SIZE_INT)
    content = int.from_bytes(bs, byteorder='big')
    return Int(content)
