import typing as t
from pager import Pager, new_pager
from btree import Tree, new_tree
from free_list import Node, new_list
from row import Row


class KV:

    def __setitem__(self, key, value):
        self.set(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __delitem__(self, key):
        self.delete(key)

    def __init__(self, pager: Pager, tree: Tree, list_: Node):
        self.pager: Pager = pager
        self.tree: Tree = tree
        self.list_: Node = list_

    def set(self, key: int, value: Row) -> None:
        self.tree[key] = value

    def get(self, key: int) -> t.Optional[Row]:
        return self.tree[key]

    def delete(self, key: int) -> None:
        self.tree.delete(key)


def new_kv(path: str):
    pager = new_pager(path)
    degree = 2
    tree = new_tree(pager, degree)
    list_ = new_list(pager)
    return KV(pager, tree, list_)