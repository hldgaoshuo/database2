from free_list import new_free_list
from kv import new_kv
from pager import new_pager
from row import new_row
from value.bool import new_bool
from value.int import new_int
from value.string import new_string


def test_init():
    pager = new_pager("test.db")
    list_ = new_free_list(pager)
    new_kv(pager, list_)


def test_set():
    pager = new_pager("test.db")
    list_ = new_free_list(pager)
    kv = new_kv(pager, list_)
    k = 1
    v = new_row(1, [new_int(1), new_string('hello'), new_bool(True)])
    kv[k] = v


def test_get():
    pager = new_pager("test.db")
    list_ = new_free_list(pager)
    kv = new_kv(pager, list_)
    k = 1
    v = kv[k]
    print()
    print(v)
