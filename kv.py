import typing as t
from pager import Pager, new_pager
from btree import BTree, new_b_tree
from free_list import FreeListNode, new_free_list
from row import Row


class KV:

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __delitem__(self, key):
        self.delete(key)

    def __init__(self, pager: Pager, list_: FreeListNode, tree: BTree):
        self.pager: Pager = pager
        self.list_: FreeListNode = list_
        self.tree: BTree = tree

    def set(self, key: int, value: Row) -> None:
        self.tree[key] = value

    def get(self, key: int) -> t.Optional[Row]:
        return self.tree[key]

    def delete(self, key: int) -> None:
        self.tree.delete(key)


def new_kv(path: str):
    pager = new_pager(path)
    list_ = new_free_list(pager)
    degree = 2
    tree = new_b_tree(pager, degree)
    return KV(pager, list_, tree)