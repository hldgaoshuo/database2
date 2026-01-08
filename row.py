from io import BytesIO

from value.int import new_int_from_bytes
from value.value import Value, ValueType
from value.bool import new_bool_from_bytes
from value.string import new_string_from_bytes


class Row:

    def __init__(self, values: list[Value]):
        self.values: list[Value] = values

    def __bytes__(self):
        r = b''
        for v in self.values:
            r += bytes(v)
        # 添加分隔符表示行结束
        r += b'\0'  # 使用 NUL 作为行分隔符
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
        if value_type == ValueType.INT:
            value = new_int_from_bytes(buf)
            row.values_add(value)
        elif value_type == ValueType.BOOL:
            value = new_bool_from_bytes(buf)
            row.values_add(value)
        elif value_type == ValueType.STRING:
            value = new_string_from_bytes(buf)
            row.values_add(value)
        elif value_type_bs == b'\0':
            return row
        else:
            raise ValueError("未知数据类型")
