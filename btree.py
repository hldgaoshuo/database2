from row import Row


class BNodeLeaf:

    def __init__(self, page_index: int):
        self.page_index: int = page_index
        self.keys: list[int] = []
        self.rows: list[Row] = []

    def __bytes__(self) -> bytes:
        """
        BNodeLeaf header length: 9b
        """
        r = b''
        r += True.to_bytes(length=1, byteorder='big')  # is_leaf
        r += self.page_index.to_bytes(length=4, byteorder='big')
        r += len(self.keys).to_bytes(length=4, byteorder='big')  # keys_num
        for key in self.keys:
            r += key.to_bytes(length=4, byteorder='big')
        for row in self.rows:
            r += bytes(row)
        return r


class BNodeInternal:

    def __init__(self, page_index: int):
        self.page_index: int = page_index
        self.keys: list[int] = []
        self.page_indices: list[int] = []

    def __bytes__(self) -> bytes:
        """
        BNodeInternal header length: 9b
        """
        r = b''
        r += False.to_bytes(length=1, byteorder='big')  # is_leaf
        r += self.page_index.to_bytes(length=4, byteorder='big')
        r += len(self.keys).to_bytes(length=4, byteorder='big')  # keys_num
        for key in self.keys:
            r += key.to_bytes(length=4, byteorder='big')
        for page_index in self.page_indices:
            r += page_index.to_bytes(length=4, byteorder='big')
        return r
