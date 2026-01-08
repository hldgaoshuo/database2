from io import BytesIO
from value.value import Value, ValueType, BYTES_VALUE_TYPE

BYTES_BOOL = 1


class Bool(Value):

    def __init__(self, content: bool) -> None:
        super().__init__(ValueType.BOOL, content)

    def __bytes__(self) -> bytes:
        value_type_row = self.value_type.to_bytes(length=BYTES_VALUE_TYPE, byteorder='big')
        content_row = self.content.to_bytes(length=BYTES_BOOL, byteorder='big')
        result = value_type_row + content_row
        return result


def new_bool(content: bool) -> Bool:
    return Bool(content)


def new_bool_from_bytes(buf: BytesIO) -> Bool:
    bs = buf.read(BYTES_BOOL)
    content = bool.from_bytes(bs, byteorder='big')
    return Bool(content)
