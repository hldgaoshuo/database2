import pytest

from value.small_int import new_small_int


def test_bytes():
    o = new_small_int(1000)
    bs = bytes(o)
    assert bs == b'\x02' + b'\x03\xE8'


def test_bytes_overflow():
    with pytest.raises(OverflowError):
        o = new_small_int(70000)
        bs = bytes(o)


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])
