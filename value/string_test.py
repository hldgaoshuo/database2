import pytest

from value.string import new_string, BYTES_STRING


def test_bytes():
    o = new_string("abc")
    bs = bytes(o)
    assert bs == b'\x02' + b'\x03' + b'abc' + b' ' * (BYTES_STRING - 3)


def test_bytes_overflow():
    with pytest.raises(ValueError):
        o = new_string("a" * (BYTES_STRING + 1))
        bs = bytes(o)


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])
