from kv import new_kv
from row import new_row
from value.bool import new_bool
from value.int import new_int
from value.string import new_string


def test_init():
    new_kv('test.db')


def test_set():
    kv = new_kv('test.db')
    k = 1
    v = new_row(1, [new_int(1), new_string('hello'), new_bool(True)])
    kv[k] = v


def test_get():
    kv = new_kv('test.db')
    k = 1
    v = kv[k]
    print()
    print(v)
