from io import BytesIO
from file import file_open, file_read, file_update

BYTES_PAGE = 4096
BYTES_MAGIC_NUMBER = 2
BYTES_PAGE_INDEX = 4

NULL_PAGE_INDEX = -1
META_PAGE_INDEX = 0

MAGIC_NUMBER_BS = b'\x95\x27'


def get_page_bs(fd: int, page_index: int) -> bytes:
    offset = page_index * BYTES_PAGE
    page_bs = file_read(fd, offset, BYTES_PAGE)
    return page_bs


def set_page_bs(fd: int, page_index: int, page_bs: bytes):
    offset = page_index * BYTES_PAGE
    file_update(fd, offset, page_bs)


class Pager:

    def __bytes__(self):
        return self.to_bytes()

    def __init__(self, fd: int, is_new: bool, used_page_index: int, table_page_index: int, head_page_index: int, tail_page_index: int):
        self.fd: int = fd
        self.is_new: bool = is_new
        self.used_page_index: int = used_page_index
        self.table_page_index: int = table_page_index
        self.head_page_index: int = head_page_index
        self.tail_page_index: int = tail_page_index

    def get_page_bs(self, page_index: int) -> bytes:
        page_bs = get_page_bs(self.fd, page_index)
        return page_bs

    def set_page_bs(self, page_index: int, page_bs: bytes) -> None:
        set_page_bs(self.fd, page_index, page_bs)

    def to_bytes(self) -> bytes:
        r = MAGIC_NUMBER_BS
        r += self.used_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big', signed=True)
        r += self.table_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big', signed=True)
        r += self.head_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big', signed=True)
        r += self.tail_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big', signed=True)
        return r

    def get_page_index(self) -> int:
        self.used_page_index += 1
        meta_bs = bytes(self)
        self.set_page_bs(META_PAGE_INDEX, meta_bs)
        return self.used_page_index

    def set_table_page_index(self, table_page_index: int) -> None:
        self.table_page_index = table_page_index
        meta_bs = bytes(self)
        self.set_page_bs(META_PAGE_INDEX, meta_bs)

    def set_head_page_index(self, head_page_index: int) -> None:
        self.head_page_index = head_page_index
        meta_bs = bytes(self)
        self.set_page_bs(META_PAGE_INDEX, meta_bs)

    def set_tail_page_index(self, tail_page_index: int) -> None:
        self.tail_page_index = tail_page_index
        meta_bs = bytes(self)
        self.set_page_bs(META_PAGE_INDEX, meta_bs)


def new_pager(path: str) -> Pager:
    fd = file_open(path)
    meta_bs = get_page_bs(fd, META_PAGE_INDEX)
    meta = BytesIO(meta_bs)
    magic_number_bs = meta.read(BYTES_MAGIC_NUMBER)
    is_new = False
    used_page_index = META_PAGE_INDEX
    table_page_index = NULL_PAGE_INDEX
    head_page_index = NULL_PAGE_INDEX
    tail_page_index = NULL_PAGE_INDEX
    if magic_number_bs != MAGIC_NUMBER_BS:
        is_new = True
        r = MAGIC_NUMBER_BS
        r += used_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big', signed=True)
        r += table_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big', signed=True)
        r += head_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big', signed=True)
        r += tail_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big', signed=True)
        set_page_bs(fd, META_PAGE_INDEX, r)
    else:
        used_page_index_bs = meta.read(BYTES_PAGE_INDEX)
        used_page_index = int.from_bytes(used_page_index_bs, byteorder='big', signed=True)
        table_page_index_bs = meta.read(BYTES_PAGE_INDEX)
        table_page_index = int.from_bytes(table_page_index_bs, byteorder='big', signed=True)
        head_page_index_bs = meta.read(BYTES_PAGE_INDEX)
        head_page_index = int.from_bytes(head_page_index_bs, byteorder='big', signed=True)
        tail_page_index_bs = meta.read(BYTES_PAGE_INDEX)
        tail_page_index = int.from_bytes(tail_page_index_bs, byteorder='big', signed=True)
    pager = Pager(fd, is_new, used_page_index, table_page_index, head_page_index, tail_page_index)
    return pager
