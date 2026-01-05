class Node:

    def __init__(
            self,
            is_leaf: bool,
            page_index: int,
            prev_page_index: int,
            next_page_index: int,
    ):
        self.is_leaf: bool = is_leaf
        self.page_index: int = page_index
        self.prev_page_index: int = prev_page_index
        self.next_page_index: int = next_page_index
        self.keys: list[int] = []
        self.page_indices: list[int] = []
        self.rows: list[Row] = []

