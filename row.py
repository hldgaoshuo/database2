from io import BytesIO

from value.int import new_int_from_bytes
from value.value import Value, ValueType, BYTES_VALUE_TYPE
from value.bool import new_bool_from_bytes
from value.string import new_string_from_bytes


BYTES_OID = 4


class Row:

    def __init__(self, oid: int, values: list[Value]):
        self.oid: int = oid
        self.values: list[Value] = values

    def __bytes__(self) -> bytes:
        """
        每行除了 values，会多出 5b
        """
        r = b''
        r += self.oid.to_bytes(length=BYTES_OID, byteorder='big')
        for v in self.values:
            r += bytes(v)
        r += b'\0'  # 添加分隔符表示行结束, 使用 NUL 作为行分隔符
        return r

    def __eq__(self, other: 'Row') -> bool:
        if len(self.values) != len(other.values):
            return False
        for i, value in enumerate(self.values):
            if value != other.values[i]:
                return False
        return True


def new_row(oid: int, values: list[Value]) -> Row:
    return Row(oid, values)


def new_row_from_bytes(buf: BytesIO) -> Row:
    oid_bs = buf.read(BYTES_OID)
    oid = int.from_bytes(bytes=oid_bs, byteorder='big')
    values = []
    while True:
        value_type_bs = buf.read(BYTES_VALUE_TYPE)
        value_type = int.from_bytes(bytes=value_type_bs, byteorder='big')
        if value_type == ValueType.INT:
            value = new_int_from_bytes(buf)
            values.append(value)
        elif value_type == ValueType.BOOL:
            value = new_bool_from_bytes(buf)
            values.append(value)
        elif value_type == ValueType.STRING:
            value = new_string_from_bytes(buf)
            values.append(value)
        elif value_type_bs == b'\0':
            row = Row(oid, values)
            return row
        else:
            raise ValueError("未知数据类型")
