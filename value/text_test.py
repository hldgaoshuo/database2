import pytest

from value.text import new_text


def test_bytes():
    o = new_text("abc")
    bs = bytes(o)
    assert bs == b'\x09' + b'\x00\x03' + b'abc'


def test_bytes_overflow():
    with pytest.raises(ValueError):
        text = ""
        for _ in range(70000):
            text += "a"
        o = new_text(text)
        bs = bytes(o)


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])
