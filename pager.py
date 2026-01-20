from io import BytesIO, BufferedRandom
from file import file_open, file_read, file_update

BYTES_PAGE = 4096
BYTES_MAGIC_NUMBER = 2
BYTES_PAGE_INDEX = 4

NULL_PAGE_INDEX = -1
META_PAGE_INDEX = 0
INIT_PAGE_INDEX = 1

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

    def __init__(self, fd: int, is_new: bool, root_page_index: int, used_page_index: int):
        self.fd: int = fd
        self.is_new: bool = is_new
        self.root_page_index: int = root_page_index
        self.used_page_index: int = used_page_index

    def get_page_bs(self, page_index: int) -> bytes:
        page_bs = get_page_bs(self.fd, page_index)
        return page_bs

    def set_page_bs(self, page_index: int, page_bs: bytes):
        set_page_bs(self.fd, page_index, page_bs)

    def to_bytes(self):
        r = MAGIC_NUMBER_BS
        r += self.root_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big')
        r += self.used_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big')
        return r

    def get_page_index(self):
        self.used_page_index += 1
        meta_bs = bytes(self)
        self.set_page_bs(META_PAGE_INDEX, meta_bs)
        return self.used_page_index

    def set_root_page_index(self, root_page_index: int):
        self.root_page_index = root_page_index
        meta_bs = bytes(self)
        self.set_page_bs(META_PAGE_INDEX, meta_bs)


def new_pager(path: str) -> Pager:
    fd = file_open(path)
    meta_bs = get_page_bs(fd, META_PAGE_INDEX)
    meta = BytesIO(meta_bs)
    magic_number_bs = meta.read(BYTES_MAGIC_NUMBER)
    is_new = False
    root_page_index = INIT_PAGE_INDEX
    used_page_index = META_PAGE_INDEX
    if magic_number_bs != MAGIC_NUMBER_BS:
        is_new = True
        r = MAGIC_NUMBER_BS
        r += root_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big')
        r += used_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big')
        set_page_bs(fd, META_PAGE_INDEX, r)
    else:
        root_page_index_bs = meta.read(BYTES_PAGE_INDEX)
        root_page_index = int.from_bytes(root_page_index_bs, byteorder='big')
        used_page_index_bs = meta.read(BYTES_PAGE_INDEX)
        used_page_index = int.from_bytes(used_page_index_bs, byteorder='big')
    pager = Pager(fd, is_new, root_page_index, used_page_index)
    return pager
