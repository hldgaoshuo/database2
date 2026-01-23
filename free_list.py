import typing as t
from io import BytesIO
from pager import BYTES_PAGE_INDEX, NULL_PAGE_INDEX, Pager

BYTES_LEN_PAGE_INDICES = 4
BYTES_UNUSED = 4

NUM_PAGE_INDICES = 2


class FreeListNode:

    def __repr__(self):
        return self.show()

    def __bytes__(self):
        return self.to_bytes()

    def __init__(self, pager: Pager, page_index: int, next_page_index: int):
        self.pager: Pager = pager
        self.page_index: int = page_index
        self.next_page_index: int = next_page_index
        self.page_indices: list[int] = []
        self.unused: int = 0

    def show(self) -> str:
        return f'FreeListNode[page_index({self.page_index}), next_page_index({self.next_page_index}), page_indices({self.page_indices}), unused({self.unused})]'

    def to_bytes(self) -> bytes:
        r = b''
        r += self.page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big')
        r += self.next_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big', signed=True)
        r += len(self.page_indices).to_bytes(length=BYTES_LEN_PAGE_INDICES, byteorder='big')
        for page_index in self.page_indices:
            r += page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big')
        r += self.unused.to_bytes(length=BYTES_UNUSED, byteorder='big')
        return r

    def persist(self) -> None:
        self.pager.set_page_bs(self.page_index, bytes(self))

    def get_unused_page_index(self, tail: 'FreeListNode') -> int:
        if self.have_unused():
            result = self.page_indices[self.unused]
            self.unused += 1
            self.persist()
            return result

        if self.next_page_index == NULL_PAGE_INDEX:
            return NULL_PAGE_INDEX

        next_ = new_free_list_node_from_page(self.pager, self.next_page_index, tail)
        result = next_.get_unused_page_index(tail)
        return result

    def set_unused_page_index(self, page_index: int) -> None:
        self.page_indices.append(page_index)

    def have_unused(self) -> bool:
        return self.unused < len(self.page_indices)

    def is_full(self) -> bool:
        return len(self.page_indices) >= NUM_PAGE_INDICES


def new_free_list_node(pager: Pager) -> FreeListNode:
    page_index = pager.get_page_index()
    node = FreeListNode(pager, page_index, NULL_PAGE_INDEX)
    return node


def new_free_list_node_from_page(pager: Pager, page_index: int, tail: t.Optional[FreeListNode]) -> FreeListNode:
    if tail is not None and page_index == tail.page_index:
        return tail
    page_bs = pager.get_page_bs(page_index)
    buf = BytesIO(page_bs)
    _page_index_bs = buf.read(BYTES_PAGE_INDEX)
    _page_index = int.from_bytes(bytes=_page_index_bs, byteorder='big')
    if page_index != _page_index:
        raise ValueError("page_index 错误")
    next_page_index_bs = buf.read(BYTES_PAGE_INDEX)
    next_page_index = int.from_bytes(bytes=next_page_index_bs, byteorder='big', signed=True)
    num_bs = buf.read(BYTES_LEN_PAGE_INDICES)
    num = int.from_bytes(bytes=num_bs, byteorder='big')
    page_indices = [int.from_bytes(bytes=buf.read(BYTES_PAGE_INDEX)) for _ in range(num)]
    unused_bs = buf.read(BYTES_UNUSED)
    unused = int.from_bytes(bytes=unused_bs, byteorder='big')
    node = FreeListNode(pager, page_index, next_page_index)
    node.page_indices = page_indices
    node.unused = unused
    return node


class FreeList:

    def __init__(self, pager: Pager, head: FreeListNode, tail: FreeListNode):
        self.pager: Pager = pager
        self.head: FreeListNode = head
        self.tail: FreeListNode = tail

    def get(self) -> int:
        page_index = self.get_unused_page_index()
        if page_index == NULL_PAGE_INDEX:
            page_index = self.pager.get_page_index()
        return page_index

    def set(self, page_index: int) -> None:
        self.set_unused_page_index(page_index)

    def zip(self) -> None:
        """
        单开一个线程处理
        """
        node = self.head
        while node.is_full() and not node.have_unused():
            self.set_unused_page_index(node.page_index)
            if node.next_page_index == NULL_PAGE_INDEX:
                break
            node = new_free_list_node_from_page(self.pager, node.next_page_index, self.tail)
            self.head = node
            self.pager.set_head_page_index(node.page_index)

    def get_unused_page_index(self) -> int:
        result = self.head.get_unused_page_index(self.tail)
        return result

    def set_unused_page_index(self, page_index: int) -> None:
        if not self.tail.is_full():
            self.tail.set_unused_page_index(page_index)
            self.tail.persist()
            return

        # tail is full
        new_tail = new_free_list_node(self.pager)
        new_tail.set_unused_page_index(page_index)
        new_tail.persist()
        self.tail.next_page_index = new_tail.page_index
        self.tail.persist()
        self.tail = new_tail
        self.pager.set_tail_page_index(new_tail.page_index)
        return


def new_free_list(pager: Pager) -> FreeList:
    if pager.is_new:
        head = new_free_list_node(pager)
        head.persist()
        pager.set_head_page_index(head.page_index)
        pager.set_tail_page_index(head.page_index)
        list_ = FreeList(pager, head, head)
    else:
        tail = new_free_list_node_from_page(pager, pager.tail_page_index, None)
        head = new_free_list_node_from_page(pager, pager.head_page_index, tail)
        list_ = FreeList(pager, head, tail)
    return list_
