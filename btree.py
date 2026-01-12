# todo degree 应该是计算出来的，但下面为了方便，先统一传 2
import threading
import typing as t
from io import BytesIO

from row import Row
from pager import Pager

BYTES_IS_LEAF = 1
BYTES_PAGE_INDEX = 4

DEGREE = 2


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

    def persist(self):
        self.pager.set_page_bs(self.page_index, bytes(self))


class BNodeLeaf(BNode):

    def __init__(self, pager: Pager, degree: int, page_index: int):
        super().__init__(pager, degree, page_index)
        self.rows: list[Row] = []
        self.lock: threading.Lock = threading.Lock()

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

    def get_add_index(self, key: int) -> int:
        i = 0
        n = len(self.keys)
        while i < n and key > self.keys[i]:
            i += 1
        return i

    def add(self, key: int, value: Row) -> 'BNodeLeaf':
        i = self.get_add_index(key)
        new_keys = self.keys[:]
        new_rows = self.rows[:]
        new_keys.insert(i, key)
        new_rows.insert(i, value)
        new_node = new_b_node_leaf(self.pager, new_keys, new_rows)
        return new_node

    def update(self, keys: list[int], rows: list[Row], page_index: int):
        with self.lock:
            self.keys = keys
            self.rows = rows
            self.page_index = page_index

    def set(self, key: int, value: Row):
        new_node = self.add(key, value)
        new_node.persist()
        self.update(new_node.keys, new_node.rows, new_node.page_index)

    def split(self) -> tuple['BNodeLeaf', 'BNodeLeaf']:
        left_keys = self.keys[:DEGREE]
        left_rows = self.rows[:DEGREE]
        left = new_b_node_leaf(self.pager, left_keys, left_rows)
        right_keys = self.keys[DEGREE:]
        right_rows = self.rows[DEGREE:]
        right = new_b_node_leaf(self.pager, right_keys, right_rows)
        return left, right

    def __getitem__(self, key: int) -> t.Optional[Row]:
        return self.get(key)

    def __setitem__(self, key: int, value: Row):
        self.set(key, value)


class BNodeInternal(BNode):

    def __init__(self, pager: Pager, degree: int, page_index: int):
        super().__init__(pager, degree, page_index)
        self.page_indices: list[int] = []
        self.lock: threading.Lock = threading.Lock()

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
        _, page_bs = self.get_page_index_page_bs(key)
        node_down = new_b_node_from_bytes(page_bs, self.pager)
        node_result = node_down.get(key)
        return node_result

    def set(self, key: int, value: Row):
        page_index, page_bs = self.get_page_index_page_bs(key)
        node_down = new_b_node_from_bytes(page_bs, self.pager)
        if node_down.is_full():
            left, right = node_down.split()
            if key < right.keys[0]:
                left.set(key, value)
                right.persist()
            else:
                right.set(key, value)
                left.persist()
            new_keys = self.keys[:]
            new_page_indices = self.page_indices[:]
            if type(node_down) == BNodeLeaf:
                new_keys.insert(page_index, node_down.keys[DEGREE - 1])
            elif type(node_down) == BNodeInternal:
                new_keys.insert(page_index, node_down.keys[DEGREE])
            else:
                raise ValueError("未知节点类型")
            new_page_indices[page_index] = left.page_index
            new_page_indices.insert(page_index + 1, right.page_index)
            new_node = new_b_node_internal(self.pager, new_keys, new_page_indices)
            new_node.persist()
            self.update(new_keys, new_page_indices, new_node.page_index)
        else:
            node_down.set(key, value)

    def get_page_index_page_bs(self, key: int) -> tuple[int, BytesIO]:
        i = 0
        n = len(self.keys)
        while i < n and key > self.keys[i]:
            i += 1
        page_index = self.page_indices[i]
        bs = self.pager.get_page_bs(page_index)
        buf = BytesIO(bs)
        return i, buf

    def split(self) -> tuple['BNodeInternal', 'BNodeInternal']:
        left_keys = self.keys[:DEGREE - 1]
        left_page_indices = self.page_indices[:DEGREE]
        left = new_b_node_internal(self.pager, left_keys, left_page_indices)
        right_keys = self.keys[DEGREE:]
        right_page_indices = self.page_indices[DEGREE:]
        right = new_b_node_internal(self.pager, right_keys, right_page_indices)
        return left, right

    def update(self, keys: list[int], page_indices: list[int], page_index: int):
        with self.lock:
            self.keys = keys
            self.page_indices = page_indices
            self.page_index = page_index

    def __getitem__(self, key: int) -> t.Optional[Row]:
        return self.get(key)

    def __setitem__(self, key: int, value: Row):
        self.set(key, value)


def new_b_node_internal(pager: Pager, keys: list[int], page_indices: list[int]) -> BNodeInternal:
    page_index = pager.get_page_index()
    node = BNodeInternal(pager, DEGREE, page_index)
    node.keys = keys
    node.page_indices = page_indices
    return node


def new_b_node_leaf(pager: Pager, keys: list[int], rows: list[Row]) -> BNodeLeaf:
    page_index = pager.get_page_index()
    node = BNodeLeaf(pager, DEGREE, page_index)
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
