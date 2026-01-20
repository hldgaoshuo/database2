from pager import Pager, new_pager
from btree import Tree, new_tree
from row import Row


class KV:

    def __init__(self, pager: Pager, tree: Tree):
        self.pager: Pager = pager
        self.tree: Tree = tree

    def __setitem__(self, key: int, value: Row):
        self.tree[key] = value

    def __getitem__(self, key: int) -> Row:
        return self.tree[key]

    def __delitem__(self, key: int):
        self.tree.delete(key)


def new_kv(path: str):
    pager = new_pager(path)
    degree = 2
    tree = new_tree(pager, degree)
    return KV(pager, tree)