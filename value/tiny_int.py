from io import BytesIO
from value.value import Value, ValueType


SIZE_TINY_INT = 1


class TinyInt(Value):

    def __init__(self, content: int) -> None:
        super().__init__(ValueType.TINY_INT, content, SIZE_TINY_INT)

    def __bytes__(self) -> bytes:
        value_type_row = self.value_type.to_bytes(length=1, byteorder='big')
        content_row = self.content.to_bytes(length=self.size, byteorder='big')
        result = value_type_row + content_row
        return result


def new_tiny_int(content: int) -> TinyInt:
    return TinyInt(content)


def new_tiny_int_from_bytes(buf: BytesIO) -> TinyInt:
    bs = buf.read(SIZE_TINY_INT)
    content = int.from_bytes(bs, byteorder='big')
    return TinyInt(content)
