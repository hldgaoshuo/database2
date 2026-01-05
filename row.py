from io import BytesIO

from value.big_int import new_big_int_from_bytes
from value.char import new_char_from_bytes
from value.int import new_int_from_bytes
from value.medium_int import new_medium_int_from_bytes
from value.small_int import new_small_int_from_bytes
from value.tiny_int import new_tiny_int_from_bytes
from value.value import Value, ValueType


class Row:

    def __init__(self, values: list[Value]):
        self.values: list[Value] = values

    def __bytes__(self):
        r = b''
        for v in self.values:
            r += bytes(v)
        # 添加分隔符表示行结束
        r += b'\n'  # 使用换行符作为行分隔符
        return r

    def __eq__(self, other: 'Row') -> bool:
        if len(self.values) != len(other.values):
            return False
        for i, value in enumerate(self.values):
            if value != other.values[i]:
                return False
        return True

    def values_add(self, value: Value):
        self.values.append(value)


def new_row(values: list[Value]) -> Row:
    return Row(values)


def new_row_from_bytes(buf: BytesIO) -> Row:
    values = []
    row = Row(values)
    while True:
        value_type_bs = buf.read(1)
        value_type = int.from_bytes(value_type_bs, byteorder='big')
        if value_type == ValueType.TINY_INT:
            value = new_tiny_int_from_bytes(buf)
            row.values_add(value)
        elif value_type == ValueType.SMALL_INT:
            value = new_small_int_from_bytes(buf)
            row.values_add(value)
        elif value_type == ValueType.MEDIUM_INT:
            value = new_medium_int_from_bytes(buf)
            row.values_add(value)
        elif value_type == ValueType.INT:
            value = new_int_from_bytes(buf)
            row.values_add(value)
        elif value_type == ValueType.BIG_INT:
            value = new_big_int_from_bytes(buf)
            row.values_add(value)
        elif value_type == ValueType.CHAR:
            value = new_char_from_bytes(buf)
            row.values_add(value)
        elif value_type_bs == b'\n':
            return row
        else:
            raise ValueError("未知数据类型")
