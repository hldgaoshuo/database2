import typing as t
from io import BytesIO

from row import Row
from pager import Pager

BYTES_IS_LEAF = 1
BYTES_PAGE_INDEX = 4

DEGREE = 2  # todo


class BNode:

    def __init__(self, pager: Pager, degree: int, page_index: int):
        self.pager: Pager = pager
        self.degree: int = degree
        self.page_index: int = page_index
        self.keys: list[int] = []

    def __bytes__(self) -> bytes:
        raise NotImplementedError

    def is_full(self) -> bool:
        return len(self.keys) == 2 * self.degree - 1

    def split(self):
        raise NotImplementedError


class BNodeLeaf(BNode):

    def __init__(self, pager: Pager, degree: int, page_index: int):
        super().__init__(pager, degree, page_index)
        self.rows: list[Row] = []

    def __bytes__(self) -> bytes:
        """
        BNodeLeaf header length: 9b
        """
        r = b''
        is_leaf = True
        r += is_leaf.to_bytes(length=BYTES_IS_LEAF, byteorder='big')
        r += self.page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big')
        keys_num = len(self.keys)
        r += keys_num.to_bytes(length=4, byteorder='big')  # keys_num
        for key in self.keys:
            r += key.to_bytes(length=4, byteorder='big')
        for row in self.rows:
            r += bytes(row)
        return r

    def get(self, key: int) -> t.Optional[Row]:
        try:
            i = self.keys.index(key)
        except ValueError:
            return None
        return self.rows[i]

    def set(self, key: int, row: Row):
        i = len(self.keys) - 1
        while i >= 0 and key < self.keys[i]:
            i = i - 1
        if key == self.keys[i]:
            self.rows[i] = row
        else:
            self.keys.insert(i + 1, key)
            self.rows.insert(i + 1, row)
        self.pager.set_page_bs(self.page_index, bytes(self))

    def split(self) -> 'BNodeLeaf':
        new_keys = self.keys[self.degree:]
        new_rows = self.rows[self.degree:]
        new_node = new_b_node_leaf(self.pager, DEGREE, new_keys, new_rows)
        self.pager.set_page_bs(new_node.page_index, bytes(new_node))
        self.keys = self.keys[:self.degree]
        self.rows = self.rows[:self.degree]
        self.pager.set_page_bs(self.page_index, bytes(self))
        return new_node

    def __getitem__(self, key: int) -> t.Optional[Row]:
        return self.get(key)

    def __setitem__(self, key: int, row: Row):
        self.set(key, row)


class BNodeInternal(BNode):

    def __init__(self, pager: Pager, degree: int, page_index: int):
        super().__init__(pager, degree, page_index)
        self.page_indices: list[int] = []

    def __bytes__(self) -> bytes:
        """
        BNodeInternal header length: 9b
        """
        r = b''
        is_leaf = False
        r += is_leaf.to_bytes(length=BYTES_IS_LEAF, byteorder='big')
        r += self.page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big')
        keys_num = len(self.keys)
        r += keys_num.to_bytes(length=4, byteorder='big')
        for key in self.keys:
            r += key.to_bytes(length=4, byteorder='big')
        for page_index in self.page_indices:
            r += page_index.to_bytes(length=4, byteorder='big')
        return r

    def get(self, key: int) -> t.Optional[Row]:
        _, page_bs = self.get_index_page_bs(key)
        node_down = new_b_node_from_bytes(page_bs, self.pager)
        node_result = node_down.get(key)
        return node_result

    def set(self, key: int, value: Row):
        index, page_bs = self.get_index_page_bs(key)
        node_down = new_b_node_from_bytes(page_bs, self.pager)
        if node_down.is_full():
            new_node = node_down.split()
            if key > self.keys[index]:
                new_node.set(key, value)
            else:
                node_down.set(key, value)
            if type(node_down) is BNodeLeaf:
                self.keys.insert(index, node_down.keys[self.degree])
            elif type(node_down) is BNodeInternal:
                self.keys.insert(index, node_down.keys[self.degree - 1])
            else:
                raise ValueError("未知数据类型")
            self.page_indices.insert(index + 1, new_node.page_index)
            self.pager.set_page_bs(self.page_index, bytes(self))
        else:
            node_down.set(key, value)

    def get_index_page_bs(self, key: int) -> tuple[int, BytesIO]:
        i = len(self.keys) - 1
        while i >= 0 and key < self.keys[i]:
            i = i - 1
        # i 的最小值为 -1，children 的最小下标是 0，所以要加一。
        i = i + 1
        page_index = self.page_indices[i]
        bs = self.pager.get_page_bs(page_index)
        buf = BytesIO(bs)
        return i, buf

    def split(self) -> 'BNodeInternal':
        new_keys = self.keys[self.degree:]
        new_page_indices = self.page_indices[self.degree:]
        new_node = new_b_node_internal(self.pager, DEGREE, new_keys, new_page_indices)
        self.pager.set_page_bs(new_node.page_index, bytes(new_node))
        self.keys = self.keys[:self.degree - 1]
        self.page_indices = self.page_indices[:self.degree]
        self.pager.set_page_bs(self.page_index, bytes(self))
        return new_node

    def __getitem__(self, key: int) -> t.Optional[Row]:
        return self.get(key)

    def __setitem__(self, key: int, value: Row):
        self.set(key, value)


def new_b_node_internal(pager: Pager, degree: int, keys: list[int], page_indices: list[int]) -> BNodeInternal:
    page_index = pager.get_page_index()
    node = BNodeInternal(pager, degree, page_index)
    node.keys = keys
    node.page_indices = page_indices
    return node


def new_b_node_leaf(pager: Pager, degree: int, keys: list[int], rows: list[Row]) -> BNodeLeaf:
    page_index = pager.get_page_index()
    node = BNodeLeaf(pager, degree, page_index)
    node.keys = keys
    node.rows = rows
    return node


def new_b_node_from_bytes(buf: BytesIO, pager: Pager) -> BNodeLeaf | BNodeInternal:
    is_leaf_bs = buf.read(BYTES_IS_LEAF)
    is_leaf = bool.from_bytes(bytes=is_leaf_bs, byteorder='big')
    page_index_bs = buf.read(BYTES_PAGE_INDEX)
    page_index = int.from_bytes(bytes=page_index_bs, byteorder='big')
    if is_leaf:
        return BNodeLeaf(pager, DEGREE, page_index)
    else:
        return BNodeInternal(pager, DEGREE, page_index)
