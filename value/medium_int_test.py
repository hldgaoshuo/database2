import pytest

from value.medium_int import new_medium_int


def test_bytes():
    o = new_medium_int(10000000)
    bs = bytes(o)
    assert bs == b'\x03' + b'\x98\x96\x80'


def test_bytes_overflow():
    with pytest.raises(OverflowError):
        o = new_medium_int(20000000)
        bs = bytes(o)


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])
