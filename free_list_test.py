from free_list import new_free_list
from pager import new_pager


def test_set():
    pager = new_pager("test.db")
    list_ = new_free_list(pager)
    pager.set_free_list(list_)
    list_.set_unused_page_index(1)
    list_.set_unused_page_index(2)
