from row import Row
from pager import Pager

BYTES_IS_LEAF = 1
BYTES_PAGE_INDEX = 4
BYTES_LEN_KEYS = 4
BYTES_KEY = 4
BYTES_LEN_ROWS = 4
BYTES_LEN_PAGE_INDICES = 4

DEGREE = 2  # todo


class BNode:

    def __init__(self, pager: Pager, degree: int, page_index: int, is_leaf: bool):
        self.pager: Pager = pager
        self.degree: int = degree
        self.page_index: int = page_index
        self.is_leaf: bool = is_leaf
        self.keys: list[int] = []
        self.rows: list[Row] = []
        self.page_indices: list[int] = []

    def __bytes__(self) -> bytes:
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

    def get(self, key: int):
        pass

    def set(self, key: int, row: Row):
        pass

    def is_full(self) -> bool:
        return len(self.keys) == 2 * self.degree - 1

