import pytest

from value.char import new_char


def test_bytes():
    o = new_char("abc", 4)
    bs = bytes(o)
    assert bs == b'\x06' + b'\x04' + b'abc '


def test_bytes_overflow():
    with pytest.raises(ValueError):
        o = new_char("abc", 2)
        bs = bytes(o)


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])
