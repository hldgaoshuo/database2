from io import BytesIO
from value.value import Value, ValueType


SIZE_OF_SIZE_FIELD = 1


class Char(Value):

    def __init__(self, content: str, size: int) -> None:
        space_num = size - len(content)
        if space_num < 0:
            raise ValueError("字符串长度超出限制")
        content = content + ' ' * space_num
        super().__init__(ValueType.CHAR, content)
        self.size = size

    def __bytes__(self) -> bytes:
        value_type_row = self.value_type.to_bytes(length=1, byteorder='big')
        size_row = self.size.to_bytes(length=SIZE_OF_SIZE_FIELD, byteorder='big')
        content_row = self.content.encode('utf-8')
        result = value_type_row + size_row + content_row
        return result


def new_char(content: str, size: int) -> Char:
    return Char(content, size)


def new_char_from_bytes(buf: BytesIO) -> Char:
    size_bs = buf.read(SIZE_OF_SIZE_FIELD)
    size = int.from_bytes(size_bs, byteorder='big')
    content_bs = buf.read(size)
    content = content_bs.decode('utf-8')
    return Char(content, size)
