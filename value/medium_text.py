from io import BytesIO
from value.value import Value, ValueType


SIZE_MAX = 16777215
SIZE_OF_CONTENT_SIZE = 3


class MediumText(Value):

    def __init__(self, content: str) -> None:
        if len(content) > SIZE_MAX:
            raise ValueError("字符串长度超出限制")
        super().__init__(ValueType.MEDIUM_TEXT, content)

    def __bytes__(self) -> bytes:
        value_type_row = self.value_type.to_bytes(length=1, byteorder='big')
        content_size = len(self.content)
        content_size_row = content_size.to_bytes(length=SIZE_OF_CONTENT_SIZE, byteorder='big')
        content_row = self.content.encode('utf-8')
        result = value_type_row + content_size_row + content_row
        return result


def new_medium_text(content: str) -> MediumText:
    return MediumText(content)


def new_medium_text_from_bytes(buf: BytesIO) -> MediumText:
    content_size_bs = buf.read(SIZE_OF_CONTENT_SIZE)
    content_size = int.from_bytes(content_size_bs, byteorder='big')
    content_bs = buf.read(content_size)
    content = content_bs.decode('utf-8')
    return MediumText(content)
