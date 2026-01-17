import threading

from file import file_open, file_read, file_update

SIZE_PAGE = 4096


class Pager:

    def __init__(self, filename: str):
        self.file = file_open(filename)

        self.page_index: int = 0
        self.page_index_lock: threading.Lock = threading.Lock()

    def set_page_bs(self, page_index: int, page_bs: bytes):
        file_update(self.file, page_index * SIZE_PAGE, page_bs)

    def get_page_bs(self, page_index: int) -> bytes:
        page_bs = file_read(self.file, page_index * SIZE_PAGE, SIZE_PAGE)
        return page_bs

    def get_page_index(self) -> int:
        with self.page_index_lock:
            index = self.page_index
            self.page_index += 1
            return index


def new_pager(filename: str) -> Pager:
    return Pager(filename)
