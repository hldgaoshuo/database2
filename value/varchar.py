from io import BytesIO
from value.value import Value, ValueType


SIZE_OF_SIZE_FIELD = 1
SIZE_OF_CONTENT_SIZE = 2


class Varchar(Value):

    def __init__(self, content: str, size: int) -> None:
        if size - len(content) < 0:
            raise ValueError("字符串长度超出限制")
        super().__init__(ValueType.VARCHAR, content)
        self.size = size

    def __bytes__(self) -> bytes:
        value_type_row = self.value_type.to_bytes(length=1, byteorder='big')
        size_row = self.size.to_bytes(length=SIZE_OF_SIZE_FIELD, byteorder='big')
        content_size = len(self.content)
        content_size_row = content_size.to_bytes(length=SIZE_OF_CONTENT_SIZE, byteorder='big')
        content_row = self.content.encode('utf-8')
        result = value_type_row + size_row + content_size_row + content_row
        return result


def new_varchar(content: str, size: int) -> Varchar:
    return Varchar(content, size)


def new_varchar_from_bytes(buf: BytesIO) -> Varchar:
    size_bs = buf.read(SIZE_OF_SIZE_FIELD)
    size = int.from_bytes(size_bs, byteorder='big')
    content_size_bs = buf.read(SIZE_OF_CONTENT_SIZE)
    content_size = int.from_bytes(content_size_bs, byteorder='big')
    content_bs = buf.read(content_size)
    content = content_bs.decode('utf-8')
    return Varchar(content, size)
