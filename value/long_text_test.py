import pytest
from value.long_text import new_long_text, SIZE_MAX


def test_bytes():
    o = new_long_text("abc")
    bs = bytes(o)
    assert bs == b'\x0b' + b'\x00\x00\x00\x03' + b'abc'


def test_bytes_overflow():
    with pytest.raises(ValueError):
        text = "a" * (SIZE_MAX + 1)
        o = new_long_text(text)
        bs = bytes(o)


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])