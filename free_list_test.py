from free_list import new_free_list
from pager import new_pager


def test_set():
    pager = new_pager("test.db")
    list_ = new_free_list(pager)
    for i in range(5):
        list_.set_unused_page_index(i+1)


def test_get():
    pager = new_pager("test.db")
    list_ = new_free_list(pager)
    for i in range(5):
        list_.set_unused_page_index(i+1)
    for _ in range(6):
        r = list_.get_unused_page_index()
        print(r)


def test_zip_1():
    pager = new_pager("test.db")
    list_ = new_free_list(pager)
    for i in range(5):
        list_.set_unused_page_index(i+1)
    for _ in range(2):
        r = list_.get_unused_page_index()
        print(r)
    list_.zip()


def test_zip_2():
    pager = new_pager("test.db")
    list_ = new_free_list(pager)
    for i in range(7):
        list_.set_unused_page_index(i+1)
    for _ in range(4):
        r = list_.get_unused_page_index()
        print(r)
    list_.zip()


def test_zip_3():
    pager = new_pager("test.db")
    list_ = new_free_list(pager)
    for i in range(3):
        list_.set_unused_page_index(i+1)
    for _ in range(4):
        r = list_.get_unused_page_index()
        print(r)
    list_.zip()


def test_zip_4():
    pager = new_pager("test.db")
    list_ = new_free_list(pager)
    for i in range(3):
        list_.set_unused_page_index(i+1)
    for _ in range(4):
        r = list_.get_unused_page_index()
        print(r)
    list_.zip()
    for _ in range(2):
        r = list_.get_unused_page_index()
        print(r)
    list_.zip()
