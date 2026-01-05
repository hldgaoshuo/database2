from io import BytesIO
from value.value import Value, ValueType


SIZE_BIG_INT = 8


class BigInt(Value):

    def __init__(self, content: int) -> None:
        super().__init__(ValueType.BIG_INT, content, SIZE_BIG_INT)

    def __bytes__(self) -> bytes:
        value_type_row = self.value_type.to_bytes(length=1, byteorder='big')
        content_row = self.content.to_bytes(length=self.size, byteorder='big')
        result = value_type_row + content_row
        return result


def new_big_int(content: int) -> BigInt:
    return BigInt(content)


def new_big_int_from_bytes(buf: BytesIO) -> BigInt:
    bs = buf.read(SIZE_BIG_INT)
    content = int.from_bytes(bs, byteorder='big')
    return BigInt(content)
