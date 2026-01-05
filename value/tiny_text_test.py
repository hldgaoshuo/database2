import pytest

from value.tiny_text import new_tiny_text


def test_bytes():
    o = new_tiny_text("abc")
    bs = bytes(o)
    assert bs == b'\x08' + b'\x03' + b'abc'


def test_bytes_overflow():
    with pytest.raises(ValueError):
        text = ""
        for _ in range(300):
            text += "a"
        o = new_tiny_text(text)
        bs = bytes(o)


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])
