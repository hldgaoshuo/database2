from io import BytesIO
import pytest

from row import new_row, new_row_from_bytes
from value.char import new_char
from value.int import new_int


def test_new_row_from_bytes_int():
    row_bs = b'\x04' + b'\xEE\x6B\x28\x00' + b'\0'
    row = new_row_from_bytes(BytesIO(row_bs))
    value = new_int(4000000000)
    row_other = new_row([value])
    assert row == row_other


def test_new_row_from_bytes_int_char():
    row_bs = b'\x04' + b'\xEE\x6B\x28\x00' + b'\x06' + b'\x04' + b'abc ' + b'\0'
    row = new_row_from_bytes(BytesIO(row_bs))
    value1 = new_int(4000000000)
    value2 = new_char("abc", 4)
    row_other = new_row([value1, value2])
    assert row == row_other


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])
