from io import BytesIO
import pytest

from row import new_row, new_row_from_bytes
from value.char import new_char
from value.int import new_int


def test_bytes():
    value1 = new_int(4000000000)
    value2 = new_char("abc", 4)
    row = new_row([value1, value2])
    row_bs = bytes(row)
    assert row_bs == b'\x04' + b'\xEE\x6B\x28\x00' + b'\x06' + b'\x04' + b'abc ' + b'\n'


def test_new_row_from_bytes():
    row_bs = b'\x04' + b'\xEE\x6B\x28\x00' + b'\x06' + b'\x04' + b'abc ' + b'\n'
    row = new_row_from_bytes(BytesIO(row_bs))
    value1 = new_int(4000000000)
    value2 = new_char("abc", 4)
    row_other = new_row([value1, value2])
    assert row == row_other


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])
