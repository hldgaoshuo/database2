from io import BytesIO
from value.value import Value, ValueType, BYTES_VALUE_TYPE

BYTES_STRING_SIZE = 1
BYTES_STRING = 10


class STRING(Value):

    def __init__(self, content: str):
        super().__init__(ValueType.STRING, content)

    def to_bytes(self) -> bytes:
        value_type_row = self.value_type.to_bytes(length=BYTES_VALUE_TYPE, byteorder='big')
        content_size = len(self.content)
        content_size_row = content_size.to_bytes(length=BYTES_STRING_SIZE, byteorder='big')
        content = self.content + ' ' * (BYTES_STRING - content_size)
        content_row = content.encode('utf-8')
        result = value_type_row + content_size_row + content_row
        return result

    def show(self) -> str:
        return f'STRING({self.content})'


def new_string(content: str) -> STRING:
    if len(content) > BYTES_STRING:
        raise ValueError("字符串长度超出限制")
    return STRING(content)


def new_string_from_bytes(buf: BytesIO) -> STRING:
    content_size_bs = buf.read(BYTES_STRING_SIZE)
    content_size = int.from_bytes(content_size_bs, byteorder='big')
    content_bs = buf.read(BYTES_STRING)
    content = content_bs.decode('utf-8')
    content = content[:content_size]
    return STRING(content)
