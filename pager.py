import threading

from file import file_open, file_read, file_update

SIZE_PAGE = 4096


class Pager:

    def __init__(self, filename: str):
        self.file = file_open(filename)
        self.page_index: int = 1  # 第 0 页用于存储元数据
        file_size = self.file.tell()
        if file_size != 0:
            self.page_index = file_size // SIZE_PAGE
        self.page_index_lock: threading.Lock = threading.Lock()

    def offset(self, page_index: int) -> int:
        return page_index * SIZE_PAGE

    def set_page_bs(self, page_index: int, page_bs: bytes):
        offset = self.offset(page_index)
        file_update(self.file, offset, page_bs)

    def set_meta_page_bs(self, page_bs: bytes):
        self.set_page_bs(0, page_bs)

    def get_page_bs(self, page_index: int) -> bytes:
        offset = self.offset(page_index)
        page_bs = file_read(self.file, offset, SIZE_PAGE)
        return page_bs

    def get_meta_page_bs(self) -> bytes:
        return self.get_page_bs(0)

    def get_page_index(self) -> int:
        with self.page_index_lock:
            index = self.page_index
            self.page_index += 1
            return index


def new_pager(filename: str) -> Pager:
    return Pager(filename)
