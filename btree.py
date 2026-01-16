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

    def __init__(self, pager: Pager, degree: int, is_leaf: bool, page_index: int):
        self.pager: Pager = pager
        self.degree: int = degree
        self.is_leaf: bool = is_leaf
        self.page_index: int = page_index
        self.keys: list[int] = []
        self.rows: list[Row] = []
        self.page_indices: list[int] = []
        self.left_page_index: int = -1
        self.right_page_index: int = -1

    def __bytes__(self) -> bytes:
        return self.to_bytes()

    def __getitem__(self, item: int) -> t.Optional[Row]:
        return self.get(item)

    def __setitem__(self, key: int, value: Row):
        self.set(key, value)

    def __delitem__(self, key: int):
        self.delete(key)

    def show(self, count: int):
        indent = '---- ' * count
        keys = ','.join([str(k) for k in self.keys])
        print(f'{indent}key:{keys} page_index:{self.page_index}')
        if not self.is_leaf:
            for page_index in self.page_indices:
                child = new_node_from_page(self.pager, self.degree, page_index)
                child.show(count + 1)
        else:
            print(f'{indent}left:{self.left_page_index} right:{self.right_page_index}')
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
            r += self.left_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big', signed=True)
            r += self.right_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big', signed=True)
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

    def delete(self, key: int) -> int:
        if self.is_leaf:
            key_r = self.delete_row(key)
            self.persist()
            return key_r
        else:
            index = self.get_index(key)
            page_index = self.page_indices[index]
            child = new_node_from_page(self.pager, self.degree, page_index)
            print(f"delete 1")
            key_r = child.delete(key)
            if child.is_enough():
                if key in self.keys and key_r != -1:
                    self.replace_key(key, key_r)
                    self.persist()
                return key_r
            else:
                l_child = None
                if self.left_page_index != -1:
                    l_child = new_node_from_page(self.pager, self.degree, self.left_page_index)
                if self.can_borrow_left_child(index, l_child):
                    self.borrow_left_child(index, child, l_child)
                    return key_r

                r_child = None
                if self.right_page_index != -1:
                    r_child = new_node_from_page(self.pager, self.degree, self.right_page_index)
                if self.can_borrow_right_child(index, r_child):
                    self.borrow_right_child(index, child, r_child)
                    return key_r

                if index < len(self.page_indices) - 1:
                    self.merge_right_child(child, r_child, index)
                    return key_r
                else:
                    self.merge_right_child(l_child, child, index)
                    return key_r

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
        if i >= 0 and key == self.keys[i]:
            self.rows[i] = row
        else:
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
            if self.right_page_index != -1:
                right = new_node_from_page(self.pager, self.degree, self.right_page_index)
                self.right_page_index = new.page_index
                right.left_page_index = new.page_index
                new.left_page_index = self.page_index
                new.right_page_index = right.page_index
                right.persist()
            else:
                self.right_page_index = new.page_index
                new.left_page_index = self.page_index
        else:
            new.keys = self.keys[self.degree:]
            new.page_indices = self.page_indices[self.degree:]
            self.keys = self.keys[:self.degree - 1]
            self.page_indices = self.page_indices[:self.degree]
        new.persist()
        self.persist()
        return new

    def delete_row(self, key: int) -> int:
        key_r = -1
        try:
            i = self.keys.index(key)
        except ValueError:
            return key_r
        self.keys.pop(i)
        self.rows.pop(i)
        try:
            key_r = self.keys[i]
        except IndexError:
            if self.right_page_index != -1:
                right = new_node_from_page(self.pager, self.degree, self.right_page_index)
                key_r = right.keys[0]
        return key_r

    def replace_key(self, key: int, key_r: int):
        i = self.keys.index(key)
        self.keys[i] = key_r

    def is_enough(self) -> bool:
        return len(self.keys) >= self.degree - 1

    def can_borrow(self):
        return len(self.keys) >= self.degree

    def can_borrow_left_child(self, index: int, left_child: 'Node'):
        return index > 0 and left_child is not None and left_child.can_borrow()

    def borrow_left_child(self, index: int, child: 'Node', left_child: 'Node'):
        if child.is_leaf:
            _key = left_child.keys.pop(-1)
            _row = left_child.rows.pop(-1)
            child.keys.insert(0, _key)
            child.rows.insert(0, _row)
        else:
            _key = self.keys[index - 1]
            _page_index = left_child.page_indices.pop(-1)
            child.keys.insert(0, _key)
            child.page_indices.insert(0, _page_index)
        if child.is_leaf:
            _key = child.keys[0]
            self.keys[index - 1] = _key
        else:
            _key = left_child.keys.pop(-1)
            self.keys[index - 1] = _key
        self.persist()
        child.persist()
        left_child.persist()

    def can_borrow_right_child(self, index: int, right_child: 'Node'):
        return index < len(self.page_indices) - 1 and right_child is not None and right_child.can_borrow()

    def borrow_right_child(self, index: int, child: 'Node', right_child: 'Node'):
        if child.is_leaf:
            _key = right_child.keys.pop(0)
            _row = right_child.rows.pop(0)
            child.keys.append(_key)
            child.rows.append(_row)
        else:
            _key = self.keys[index]
            _page_index = right_child.page_indices.pop(0)
            child.keys.append(_key)
            child.page_indices.append(_page_index)
        if child.is_leaf:
            _key = right_child.keys[0]
            self.keys[index] = _key
        else:
            _key = right_child.keys.pop(0)
            self.keys[index] = _key
        self.persist()
        child.persist()
        right_child.persist()

    def merge_right_child(self, left_child: 'Node', right_child: 'Node', index: int):
        if left_child.is_leaf:
            left_child.keys.extend(right_child.keys)
            left_child.rows.extend(right_child.rows)
            left_child.right_page_index = right_child.right_page_index
            if left_child.right_page_index != -1:
                rr_child = new_node_from_page(self.pager, self.degree, left_child.right_page_index)
                rr_child.left_page_index = left_child.page_index
                rr_child.persist()
        else:
            _key = self.keys.pop(index)
            left_child.keys.append(_key)
            left_child.keys.extend(right_child.keys)
            left_child.page_indices.extend(right_child.page_indices)
        self.page_indices.pop(index + 1)
        self.persist()
        left_child.persist()
        # todo right 进入 free list

    def is_empty(self) -> bool:
        return len(self.keys) == 0


def new_node(pager: Pager, degree: int, is_leaf: bool):
    page_index = pager.get_page_index()
    node = Node(pager, degree, is_leaf, page_index)
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
    node = Node(pager, degree, is_leaf, page_index)
    keys_num_bs = buf.read(BYTES_LEN_KEYS)
    keys_num = int.from_bytes(bytes=keys_num_bs, byteorder='big')
    keys = [int.from_bytes(bytes=buf.read(BYTES_KEY), byteorder='big') for _ in range(keys_num)]
    node.keys = keys
    if is_leaf:
        rows_num_bs = buf.read(BYTES_LEN_ROWS)
        rows_num = int.from_bytes(bytes=rows_num_bs, byteorder='big')
        rows = [new_row_from_bytes(buf) for _ in range(rows_num)]
        node.rows = rows
        left_page_index_bs = buf.read(BYTES_PAGE_INDEX)
        node.left_page_index = int.from_bytes(bytes=left_page_index_bs, byteorder='big', signed=True)
        right_page_index_bs = buf.read(BYTES_PAGE_INDEX)
        node.right_page_index = int.from_bytes(bytes=right_page_index_bs, byteorder='big', signed=True)
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

    def __delitem__(self, key: int):
        self.delete(key)

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

    def delete(self, key: int):
        self.root.delete(key)
        if self.root.is_empty() and not self.root.is_leaf:
            pi = self.root.page_indices[0]
            new_root = new_node_from_page(self.pager, self.degree, pi)
            self.root = new_root
            # todo 需要更新表的元数据


def new_tree(pager: Pager, degree: int) -> Tree:
    tree = Tree(pager, degree)
    return tree
