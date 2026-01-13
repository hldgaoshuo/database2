import typing as t
from io import BytesIO
from row import Row, new_row_from_bytes
from pager import Pager

BYTES_IS_LEAF = 1
BYTES_PAGE_INDEX = 4
BYTES_LEN_KEYS = 4
BYTES_KEY = 4
BYTES_LEN_ROWS = 4
BYTES_LEN_PAGE_INDICES = 4


class Node:

    def __init__(self, pager: Pager, degree: int, page_index: int, is_leaf: bool):
        self.pager: Pager = pager
        self.degree: int = degree
        self.page_index: int = page_index
        self.is_leaf: bool = is_leaf
        self.keys: list[int] = []
        self.rows: list[Row] = []
        self.page_indices: list[int] = []

    def __bytes__(self) -> bytes:
        return self.to_bytes()

    def __getitem__(self, item: int) -> t.Optional[Row]:
        return self.get(item)

    def __setitem__(self, key: int, value: Row):
        self.set(key, value)

    def show(self, count: int):
        indent = '---- ' * count
        keys = ','.join([str(k) for k in self.keys])
        print(f'{indent}key:{keys} page_index:{self.page_index}')
        if not self.is_leaf:
            for page_index in self.page_indices:
                child = new_node_from_page(self.pager, self.degree, page_index)
                child.show(count + 1)
        else:
            print(f'{indent}rows:{self.rows}')

    def to_bytes(self):
        r = b''
        r += self.is_leaf.to_bytes(length=BYTES_IS_LEAF, byteorder='big')
        r += self.page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big')
        r += len(self.keys).to_bytes(length=BYTES_LEN_KEYS, byteorder='big')
        for key in self.keys:
            r += key.to_bytes(length=BYTES_KEY, byteorder='big')
        if self.is_leaf:
            r += len(self.rows).to_bytes(length=BYTES_LEN_ROWS, byteorder='big')
            for row in self.rows:
                r += bytes(row)
        else:
            r += len(self.page_indices).to_bytes(length=BYTES_LEN_PAGE_INDICES, byteorder='big')
            for page_index in self.page_indices:
                r += page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big')
        return r

    def get(self, key: int) -> t.Optional[Row]:
        if self.is_leaf:
            return self.get_row(key)
        else:
            page_index = self.get_page_index(key)
            child = new_node_from_page(self.pager, self.degree, page_index)
            return child.get(key)

    def set(self, key: int, row: Row):
        if self.is_leaf:
            self.set_row(key, row)
            self.persist()
        else:
            index = self.get_index(key)
            page_index = self.page_indices[index]
            child = new_node_from_page(self.pager, self.degree, page_index)
            if child.is_full():
                child_new = child.split()
                if child.is_leaf:
                    self.keys.insert(index, child.keys[child.degree])
                else:
                    self.keys.insert(index, child.keys[child.degree - 1])
                self.page_indices.insert(index + 1, child_new.page_index)
                self.persist()
                if key > self.keys[index]:
                    child_new.set(key, row)
                else:
                    child.set(key, row)
            else:
                child.set(key, row)

    def get_row(self, key: int) -> t.Optional[Row]:
        try:
            i = self.keys.index(key)
        except ValueError:
            return None
        row = self.rows[i]
        return row

    def get_page_index(self, key: int) -> int:
        i = len(self.keys) - 1
        while i >= 0 and key < self.keys[i]:
            i = i - 1
        i = i + 1
        page_index = self.page_indices[i]
        return page_index

    def set_row(self, key: int, row: Row):
        i = len(self.keys) - 1
        while i >= 0 and key < self.keys[i]:
            i = i - 1
        i = i + 1
        self.keys.insert(i, key)
        self.rows.insert(i, row)

    def persist(self):
        self.pager.set_page_bs(self.page_index, bytes(self))

    def get_index(self, key: int) -> int:
        i = len(self.keys) - 1
        while i >= 0 and key < self.keys[i]:
            i = i - 1
        i = i + 1
        return i

    def is_full(self) -> bool:
        return len(self.keys) == 2 * self.degree - 1

    def split(self) -> 'Node':
        new = new_node(self.pager, self.degree, self.is_leaf)
        if self.is_leaf:
            new.keys = self.keys[self.degree:]
            new.rows = self.rows[self.degree:]
            self.keys = self.keys[:self.degree]
            self.rows = self.rows[:self.degree]
        else:
            new.keys = self.keys[self.degree:]
            new.page_indices = self.page_indices[self.degree:]
            self.keys = self.keys[:self.degree - 1]
            self.page_indices = self.page_indices[:self.degree]
        new.persist()
        self.persist()
        return new


def new_node(pager: Pager, degree: int, is_leaf: bool):
    page_index = pager.get_page_index()
    node = Node(pager, degree, page_index, is_leaf)
    return node


def new_node_from_page(pager: Pager, degree: int, page_index: int) -> Node:
    page_bs = pager.get_page_bs(page_index)
    buf = BytesIO(page_bs)
    is_leaf_bs = buf.read(BYTES_IS_LEAF)
    is_leaf = bool.from_bytes(bytes=is_leaf_bs, byteorder='big')
    _page_index_bs = buf.read(BYTES_PAGE_INDEX)
    _page_index = int.from_bytes(bytes=_page_index_bs, byteorder='big')
    if page_index != _page_index:
        raise ValueError("page_index 错误")
    node = Node(pager, degree, page_index, is_leaf)
    keys_num_bs = buf.read(BYTES_LEN_KEYS)
    keys_num = int.from_bytes(bytes=keys_num_bs, byteorder='big')
    keys = [int.from_bytes(bytes=buf.read(BYTES_KEY), byteorder='big') for _ in range(keys_num)]
    node.keys = keys
    if is_leaf:
        rows_num_bs = buf.read(BYTES_LEN_ROWS)
        rows_num = int.from_bytes(bytes=rows_num_bs, byteorder='big')
        rows = [new_row_from_bytes(buf) for _ in range(rows_num)]
        node.rows = rows
    else:
        page_indices_num_bs = buf.read(BYTES_LEN_PAGE_INDICES)
        page_indices_num = int.from_bytes(bytes=page_indices_num_bs, byteorder='big')
        page_indices = [int.from_bytes(bytes=buf.read(BYTES_PAGE_INDEX), byteorder='big') for _ in range(page_indices_num)]
        node.page_indices = page_indices
    return node


class Tree:

    def __init__(self, pager: Pager, degree: int):
        self.pager: Pager = pager
        self.degree: int = degree
        self.root: Node = new_node(pager, degree, True)
        self.root.persist()

    def __getitem__(self, item: int) -> t.Optional[Row]:
        return self.get(item)

    def __setitem__(self, key: int, value: Row):
        self.set(key, value)

    def show(self):
        print()
        self.root.show(0)

    def get(self, key: int):
        return self.root.get(key)

    def set(self, key: int, row: Row):
        if self.root.is_full():
            child = self.root
            new_root = new_node(self.pager, self.degree, False)
            new_root.page_indices = [child.page_index]
            if child.is_leaf:
                new_root.keys.insert(0, child.keys[child.degree])
            else:
                new_root.keys.insert(0, child.keys[child.degree - 1])
            child_new = child.split()
            new_root.page_indices.insert(1, child_new.page_index)
            new_root.persist()
            self.root = new_root
        self.root.set(key, row)


def new_tree(pager: Pager, degree: int) -> Tree:
    tree = Tree(pager, degree)
    return tree
