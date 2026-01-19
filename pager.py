from io import BytesIO, BufferedRandom
from file import file_open, file_read, file_update

BYTES_PAGE = 4096
BYTES_MAGIC_NUMBER = 2
BYTES_PAGE_INDEX = 4

NULL_PAGE_INDEX = -1
META_PAGE_INDEX = 0
INIT_PAGE_INDEX = 1

MAGIC_NUMBER_BS = b'\x95\x27'


class Pager:

    def __init__(self, filename: str):
        self.file, self.is_new = file_open(filename)
        self.root_page_index: int = NULL_PAGE_INDEX
        self.used_page_index: int = NULL_PAGE_INDEX

    def get_page_bs(self, page_index: int) -> bytes:
        offset = page_index * BYTES_PAGE
        page_bs = file_read(self.file, offset, BYTES_PAGE)
        return page_bs

    def set_page_bs(self, page_index: int, page_bs: bytes):
        offset = page_index * BYTES_PAGE
        file_update(self.file, offset, page_bs)

    def __bytes__(self):
        return self.to_bytes()

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


def new_pager(filename: str) -> Pager:
    pager = Pager(filename)
    meta_bs = pager.get_page_bs(META_PAGE_INDEX)
    meta = BytesIO(meta_bs)
    magic_number_bs = meta.read(BYTES_MAGIC_NUMBER)
    if magic_number_bs != MAGIC_NUMBER_BS:
        r = MAGIC_NUMBER_BS
        pager.root_page_index = INIT_PAGE_INDEX
        r += pager.root_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big')
        pager.used_page_index = META_PAGE_INDEX
        r += pager.used_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big')
        pager.set_page_bs(META_PAGE_INDEX, r)
    else:
        root_page_index_bs = meta.read(BYTES_PAGE_INDEX)
        pager.root_page_index = int.from_bytes(root_page_index_bs, byteorder='big')
        used_page_index_bs = meta.read(BYTES_PAGE_INDEX)
        pager.used_page_index = int.from_bytes(used_page_index_bs, byteorder='big')
    return pager
