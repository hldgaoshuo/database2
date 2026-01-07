import pytest

from value2.bool import new_bool


def test_bytes():
    o = new_bool(True)
    bs = bytes(o)
    assert bs == b'\x03' + b'\x01'


if __name__ == "__main__":
    # 可以直接运行此文件来执行测试
    pytest.main([__file__])
