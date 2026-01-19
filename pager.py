import threading

from file import file_open, file_read, file_update

BYTES_PAGE = 4096

NULL_PAGE_INDEX = -1
META_PAGE_INDEX = 0
INIT_PAGE_INDEX = 1


class Pager:

    def __init__(self, filename: str):
        self.file = file_open(filename)
        self.meta_page_index: int = META_PAGE_INDEX  # 第 0 页用于存储元数据
        self.page_index: int = INIT_PAGE_INDEX
        file_size = self.file.tell()
        if file_size != 0:
            self.page_index = file_size // BYTES_PAGE
        self.page_index_lock: threading.Lock = threading.Lock()

    def offset(self, page_index: int) -> int:
        return page_index * BYTES_PAGE

    def set_page_bs(self, page_index: int, page_bs: bytes):
        offset = self.offset(page_index)
        file_update(self.file, offset, page_bs)

    def set_meta_page_bs(self, page_bs: bytes):
        self.set_page_bs(self.meta_page_index, page_bs)

    def get_page_bs(self, page_index: int) -> bytes:
        offset = self.offset(page_index)
        page_bs = file_read(self.file, offset, BYTES_PAGE)
        return page_bs

    def get_meta_page_bs(self) -> bytes:
        return self.get_page_bs(self.meta_page_index)

    def get_page_index(self) -> int:
        with self.page_index_lock:
            index = self.page_index
            self.page_index += 1
            return index


def new_pager(filename: str) -> Pager:
    return Pager(filename)
