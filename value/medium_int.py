from io import BytesIO
from value.value import Value, ValueType


SIZE_MEDIUM_INT = 3


class MediumInt(Value):

    def __init__(self, content: int) -> None:
        super().__init__(ValueType.MEDIUM_INT, content, SIZE_MEDIUM_INT)

    def __bytes__(self) -> bytes:
        value_type_row = self.value_type.to_bytes(length=1, byteorder='big')
        content_row = self.content.to_bytes(length=self.size, byteorder='big')
        result = value_type_row + content_row
        return result


def new_medium_int(content: int) -> MediumInt:
    return MediumInt(content)


def new_medium_int_from_bytes(buf: BytesIO) -> MediumInt:
    bs = buf.read(SIZE_MEDIUM_INT)
    content = int.from_bytes(bs, byteorder='big')
    return MediumInt(content)
