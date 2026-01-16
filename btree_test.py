"""
测试 table，三列，类型分别为 id:int，name:string，ok:bool
"""
from btree import new_tree
from pager import Pager
from row import new_row
from value.bool import new_bool
from value.int import new_int
from value.string import new_string


def test_set():
    pager = Pager("test.db")
    degree = 2
    tree = new_tree(pager, degree)
    datas = [
        new_row(1, [new_int(1), new_string('hello'), new_bool(True)]),
        new_row(2, [new_int(2), new_string('world'), new_bool(False)]),
        new_row(3, [new_int(3), new_string('ok'), new_bool(True)]),
        new_row(4, [new_int(4), new_string('ok'), new_bool(True)]),
        new_row(1, [new_int(1), new_string('ok'), new_bool(True)]),
    ]
    for data in datas:
        tree[data.oid] = data
        tree.show()


def test_get():
    pager = Pager("test.db")
    degree = 2
    tree = new_tree(pager, degree)
    datas = [
        new_row(1, [new_int(1), new_string('hello'), new_bool(True)]),
        new_row(2, [new_int(2), new_string('world'), new_bool(False)]),
        new_row(3, [new_int(3), new_string('ok'), new_bool(True)]),
        new_row(4, [new_int(4), new_string('ok'), new_bool(True)]),
        new_row(1, [new_int(1), new_string('ok'), new_bool(True)]),
    ]
    for data in datas:
        tree[data.oid] = data
    for data in datas:
        print()
        print(tree[data.oid])


def test_delete():
    pager = Pager("test.db")
    degree = 2
    tree = new_tree(pager, degree)
    datas = [
        new_row(1, [new_int(1), new_string('hello'), new_bool(True)]),
        new_row(2, [new_int(2), new_string('world'), new_bool(False)]),
        new_row(3, [new_int(3), new_string('ok'), new_bool(True)]),
        new_row(4, [new_int(4), new_string('ok'), new_bool(True)]),
        new_row(1, [new_int(1), new_string('ok'), new_bool(True)]),
    ]
    for data in datas:
        tree[data.oid] = data
    del tree[2]
    tree.show()
