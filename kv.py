from pager import Pager, new_pager
from btree import Tree, new_tree_from_page
from row import Row


class KV:

    def __init__(self, path: str, degree: int):
        self.pager: Pager = new_pager(path)
        self.tree: Tree = new_tree_from_page(self.pager, degree)

    def __setitem__(self, key: int, value: Row):
        self.tree[key] = value

    def __getitem__(self, key: int) -> Row:
        return self.tree[key]

    def __delitem__(self, key: int):
        self.tree.delete(key)


def new_kv(path: str):
    degree = 2
    return KV(path, degree)