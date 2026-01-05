from io import BytesIO
from value.value import Value, ValueType


SIZE_SMALL_INT = 2


class SmallInt(Value):

    def __init__(self, content: int) -> None:
        super().__init__(ValueType.SMALL_INT, content, SIZE_SMALL_INT)

    def __bytes__(self) -> bytes:
        value_type_row = self.value_type.to_bytes(length=1, byteorder='big')
        content_row = self.content.to_bytes(length=self.size, byteorder='big')
        result = value_type_row + content_row
        return result


def new_small_int(content: int) -> SmallInt:
    return SmallInt(content)


def new_small_int_from_bytes(buf: BytesIO) -> SmallInt:
    bs = buf.read(SIZE_SMALL_INT)
    content = int.from_bytes(bs, byteorder='big')
    return SmallInt(content)

