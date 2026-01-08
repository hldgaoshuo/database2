import pytest

from value.int import new_int


def test_bytes():
    o = new_int(100)
    bs = bytes(o)
    assert bs == b'\x01' + b'\x00\x00\x00\x00\x00\x00\x00\x64'


def test_bytes_overflow():
    with pytest.raises(OverflowError):
        o = new_int(20000000000000000000)
        bs = bytes(o)


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])
