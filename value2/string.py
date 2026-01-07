from io import BytesIO
from value2.value import Value, ValueType, BYTES_VALUE_TYPE

BYTES_STRING_SIZE = 1
BYTES_STRING = 255


class STRING(Value):

    def __init__(self, content: str) -> None:
        self.content_size = len(content)
        space_num = BYTES_STRING - self.content_size
        if space_num < 0:
            raise ValueError("字符串长度超出限制")
        content = content + ' ' * space_num
        super().__init__(ValueType.STRING, content)

    def __bytes__(self) -> bytes:
        value_type_row = self.value_type.to_bytes(length=BYTES_VALUE_TYPE, byteorder='big')
        content_size_row = self.content_size.to_bytes(length=BYTES_STRING_SIZE, byteorder='big')
        content_row = self.content.encode('utf-8')
        result = value_type_row + content_size_row + content_row
        return result


def new_string(content: str) -> STRING:
    return STRING(content)


def new_string_from_bytes(buf: BytesIO) -> STRING:
    content_size_bs = buf.read(BYTES_STRING_SIZE)
    content_size = int.from_bytes(content_size_bs, byteorder='big')
    content_bs = buf.read(content_size)
    content = content_bs.decode('utf-8')
    return STRING(content)
