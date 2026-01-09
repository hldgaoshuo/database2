# todo degree 应该是计算出来的，但下面为了方便，先统一传 2
import threading
import typing as t
from io import BytesIO

from row import Row
from pager import Pager

BYTES_IS_LEAF = 1
BYTES_PAGE_INDEX = 4


class BNode:

    def __init__(self, pager: Pager, degree: int, page_index: int):
        self.pager: Pager = pager
        self.degree: int = degree
        self.page_index: int = page_index
        self.keys: list[int] = []

    def is_full(self) -> bool:
        return len(self.keys) == 2 * self.degree - 1


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

    def __getitem__(self, key: int) -> t.Optional[Row]:
        try:
            i = self.keys.index(key)
        except ValueError:
            return None
        return self.rows[i]

    def __setitem__(self, key: int, value: Row):
        # 实现 Copy-on-Write 语义
        # 1. 找到插入位置
        i = 0
        n = len(self.keys)
        while i < n and key > self.keys[i]:
            i += 1

        # 2. 创建新列表并插入新键值对
        new_keys = self.keys[:]
        new_rows = self.rows[:]
        new_keys.insert(i, key)
        new_rows.insert(i, value)

        # 3. 获取新页面索引并创建新节点
        new_node = new_b_node_leaf(self.pager, new_keys, new_rows)

        # 4. 将新节点数据写入新页面
        self.pager.set_page_bs(new_node.page_index, bytes(new_node))

        # 5. 更新当前节点为新节点状态
        with self.lock:
            self.keys = new_keys
            self.rows = new_rows
            self.page_index = new_node.page_index  # 更新页面索引为新页面


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

    def __get_page_index_page_bs(self, key: int) -> tuple[int, BytesIO]:
        i = 0
        n = len(self.keys)
        while i < n and key > self.keys[i]:
            i += 1
        page_index = self.page_indices[i]
        bs = self.pager.get_page_bs(page_index)
        buf = BytesIO(bs)
        return i, buf

    def __getitem__(self, key: int) -> t.Optional[Row]:
        _, page_bs = self.__get_page_index_page_bs(key)
        node_down = new_b_node_from_bytes(page_bs, self.pager)
        node_result = node_down[key]
        return node_result

    def __setitem__(self, key: int, value: Row):
        page_index, page_bs = self.__get_page_index_page_bs(key)
        node_down = new_b_node_from_bytes(page_bs, self.pager)
        if node_down.is_full():
            if type(node_down) is BNodeLeaf:
                pass
            elif type(node_down) is BNodeInternal:
                node_down_left, node_down_right = new_b_node_internal_in_split(self.pager, node_down)
                if key < node_down_right.keys[0]:
                    node_down_left[key] = value
                else:
                    node_down_right[key] = value
                self.pager.set_page_bs(node_down_left.page_index, bytes(node_down_left))
                self.pager.set_page_bs(node_down_right.page_index, bytes(node_down_right))

                new_node_keys = self.keys[:]
                new_node_page_indices = self.page_indices[:]

                new_node_keys.insert(page_index, key)
                new_node_page_indices.insert(page_index + 1, node_down_right.page_index)

                new_node = new_b_node_internal(self.pager, new_node_keys, new_node_page_indices)
                self.pager.set_page_bs(new_node.page_index, bytes(new_node))

                with self.lock:
                    self.keys = new_node_keys
                    self.page_indices = new_node_page_indices
                    self.page_index = new_node.page_index
            else:
                raise ValueError("未知节点类型")


def new_b_node_internal_in_split(pager: Pager, node_split: BNodeInternal) -> tuple[BNodeInternal, BNodeInternal]:
    # 分裂后的左节点
    node_left_keys = node_split.keys[:node_split.degree - 1]
    node_left_page_indices = node_split.page_indices[:node_split.degree]
    node_left = new_b_node_internal(pager, node_left_keys, node_left_page_indices)
    # 分裂后的右节点
    node_right_keys = node_split.keys[node_split.degree:]
    node_right_page_indices = node_split.page_indices[node_split.degree:]
    node_right = new_b_node_internal(pager, node_right_keys, node_right_page_indices)
    return node_left, node_right


def new_b_node_internal(pager: Pager, keys: list[int], page_indices: list[int]) -> BNodeInternal:
    degree = 2
    page_index = pager.get_page_index()
    node = BNodeInternal(pager, degree, page_index)
    node.keys = keys
    node.page_indices = page_indices
    return node


def new_b_node_leaf(pager: Pager, keys: list[int], rows: list[Row]) -> BNodeLeaf:
    degree = 2
    page_index = pager.get_page_index()
    node = BNodeLeaf(pager, degree, page_index)
    node.keys = keys
    node.rows = rows
    return node


def new_b_node_from_bytes(buf: BytesIO, pager: Pager) -> BNodeLeaf | BNodeInternal:
    degree = 2
    is_leaf_bs = buf.read(BYTES_IS_LEAF)
    is_leaf = bool.from_bytes(bytes=is_leaf_bs, byteorder='big')
    page_index_bs = buf.read(BYTES_PAGE_INDEX)
    page_index = int.from_bytes(bytes=page_index_bs, byteorder='big')
    if is_leaf:
        return BNodeLeaf(pager, degree, page_index)
    else:
        return BNodeInternal(pager, degree, page_index)
