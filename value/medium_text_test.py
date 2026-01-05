import pytest

from value.medium_text import new_medium_text


def test_bytes():
    o = new_medium_text("abc")
    bs = bytes(o)
    assert bs == b'\x0a' + b'\x00\x00\x03' + b'abc'


def test_bytes_overflow():
    with pytest.raises(ValueError):
        # for 循环创建字符串过慢，改为 * 生成字符串
        text = "a" * 17000000
        o = new_medium_text(text)
        bs = bytes(o)


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])
