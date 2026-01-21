from io import BytesIO
from pager import BYTES_PAGE_INDEX, NULL_PAGE_INDEX, Pager

BYTES_LEN_PAGE_INDICES = 4
BYTES_UNUSED = 4

NUM_PAGE_INDICES = 2


class FreeListNode:

    def __bytes__(self):
        return self.to_bytes()

    def __init__(self, pager: Pager, page_index: int, next_page_index: int):
        self.pager: Pager = pager
        self.page_index: int = page_index
        self.next_page_index: int = next_page_index
        self.page_indices: list[int] = []
        self.unused: int = 0

    def to_bytes(self):
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

    def get_unused_page_index(self) -> int:
        if self.have_unused():
            result = self.page_indices[self.unused]
            self.unused += 1
            return result

        # all used
        if self.next_page_index == NULL_PAGE_INDEX:
            return NULL_PAGE_INDEX

        # all used
        # have next
        next_ = new_free_list_node_from_page(self.pager, self.next_page_index)
        unused_page_index = next_.get_unused_page_index()
        return unused_page_index

    def set_unused_page_index(self, page_index: int) -> bool:
        """
        返回链表是否已完成截断
        """
        if not self.is_full():
            self.page_indices.append(page_index)
            self.persist()
            return False

        if self.next_page_index == NULL_PAGE_INDEX:
            next_ = new_free_list_node(self.pager)
            self.next_page_index = next_.page_index
            self.persist()
        else:
            next_ = new_free_list_node_from_page(self.pager, self.next_page_index)
        is_split = next_.set_unused_page_index(page_index)

        # full
        if not is_split and not self.have_unused():
            tail = new_free_list_node_from_page(self.pager, self.pager.tail_page_index)
            tail.set_unused_page_index(self.page_index)
            self.pager.set_head_page_index(next_.page_index)
            if self.pager.tail_page_index == self.page_index:
                self.pager.set_tail_page_index(next_.page_index)
            is_split = True
        return is_split

    def have_unused(self) -> bool:
        return self.unused < len(self.page_indices)

    def is_full(self) -> bool:
        return len(self.page_indices) >= NUM_PAGE_INDICES


def new_free_list_node(pager: Pager) -> FreeListNode:
    page_index = pager.get_page_index()
    node = FreeListNode(pager, page_index, NULL_PAGE_INDEX)
    return node


def new_free_list_node_from_page(pager: Pager, page_index: int) -> FreeListNode:
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


def new_free_list(pager: Pager) -> FreeListNode:
    if pager.is_new:
        head = new_free_list_node(pager)
        head.persist()
    else:
        head = new_free_list_node_from_page(pager, pager.tail_page_index)
    return head
