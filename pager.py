import threading

from file import file_open


SIZE_PAGE = 4096


class Pager:

    def __init__(self, filename: str):
        self.file = file_open(filename)

        self.page_index: int = 0
        self.page_index_lock: threading.Lock = threading.Lock()

    def get_page_index(self) -> int:
        with self.page_index_lock:
            index = self.page_index
            self.page_index += 1
            return index
