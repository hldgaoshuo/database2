import pytest

from value.big_int import new_big_int


def test_bytes():
    o = new_big_int(18000000000000000000)
    bs = bytes(o)
    assert bs == b'\x05' + b'\xf9\xcc\xd8\xa1\xc5\x08\x00\x00'


def test_bytes_overflow():
    with pytest.raises(OverflowError):
        o = new_big_int(20000000000000000000)
        bs = bytes(o)


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])
