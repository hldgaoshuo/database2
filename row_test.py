from io import BytesIO
import pytest

from oid import get_oid
from row import new_row, new_row_from_bytes
from value.int import new_int
from value.string import new_string, BYTES_STRING


def test_new_row_from_bytes_int():
    row_bs = b'\x00\x00\x00\x00' + b'\x01' + b'\x00\x00\x00\x00\x00\x00\x00\x64' + b'\0'
    row = new_row_from_bytes(BytesIO(row_bs))
    oid = get_oid()
    value = new_int(100)
    values = [value]
    row_other = new_row(oid, values)
    assert row == row_other


def test_new_row_from_bytes_int_char():
    row_bs = b'\x00\x00\x00\x00' + b'\x01' + b'\x00\x00\x00\x00\x00\x00\x00\x64' + b'\x02' + b'\x03' + b'abc' + b' ' * (BYTES_STRING - 3) + b'\0'
    row = new_row_from_bytes(BytesIO(row_bs))
    oid = get_oid()
    value1 = new_int(100)
    value2 = new_string("abc")
    values = [value1, value2]
    row_other = new_row(oid, values)
    assert row == row_other


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])
