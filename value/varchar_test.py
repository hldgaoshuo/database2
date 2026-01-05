import pytest

from value.varchar import new_varchar


def test_bytes():
    o = new_varchar("abc", 4)
    bs = bytes(o)
    assert bs == b'\x07' + b'\x04' + b'\x00\x03' + b'abc'


def test_bytes_overflow():
    with pytest.raises(ValueError):
        o = new_varchar("abc", 2)
        bs = bytes(o)


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])
