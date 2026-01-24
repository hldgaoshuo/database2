from io import BytesIO
from pager import NULL_PAGE_INDEX, BYTES_PAGE_INDEX, Pager
from value.value import ValueType
from value.string import String, new_string_from_bytes

BYTES_COL_NUM = 4
BYTES_COL_TYPE = 4
BYTES_LEN_TABLES = 4

NUM_TABLES = 2


class Table:

    def __bytes__(self):
        return self.to_bytes()

    def __init__(self, name: String):
        self.name: String = name
        self.col_names: list[String] = []
        self.col_types: list[ValueType] = []

    def to_bytes(self) -> bytes:
        r = bytes(self.name)
        col_num = len(self.col_names)
        r += col_num.to_bytes(length=BYTES_COL_NUM, byteorder='big')
        for i in range(col_num):
            r += bytes(self.col_names[i])
        for i in range(col_num):
            r += self.col_types[i].to_bytes(length=BYTES_COL_TYPE, byteorder='big')
        return r


def new_table_from_bytes(buf: BytesIO) -> Table:
    name = new_string_from_bytes(buf)
    col_num = int.from_bytes(buf.read(BYTES_COL_NUM), byteorder='big')
    col_names = []
    for _ in range(col_num):
        col_names.append(new_string_from_bytes(buf))
    col_types = []
    for _ in range(col_num):
        col_types.append(int.from_bytes(buf.read(BYTES_COL_TYPE), byteorder='big'))
    table = Table(name)
    table.col_names = col_names
    table.col_types = col_types
    return table


class DatabasePage:

    def __bytes__(self):
        return self.to_bytes()

    def __init__(self, pager: Pager, page_index: int, next_page_index: int):
        self.pager: Pager = pager
        self.page_index: int = page_index
        self.next_page_index: int = next_page_index
        self.tables: list[Table] = []

    def to_bytes(self) -> bytes:
        r = b''
        r += self.page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big')
        r += self.next_page_index.to_bytes(length=BYTES_PAGE_INDEX, byteorder='big', signed=True)
        r += len(self.tables).to_bytes(length=BYTES_LEN_TABLES, byteorder='big')
        for table in self.tables:
            r += bytes(table)
        return r


def new_database_page(pager: Pager) -> DatabasePage:
    page_index = pager.get_page_index()
    page = DatabasePage(pager, page_index, NULL_PAGE_INDEX)
    return page


def new_database_page_from_page(pager: Pager, page_index: int) -> DatabasePage:
    bs = pager.get_page_bs(page_index)
    buf = BytesIO(bs)
    _page_index_bs = buf.read(BYTES_PAGE_INDEX)
    _page_index = int.from_bytes(bytes=_page_index_bs, byteorder='big')
    if page_index != _page_index:
        raise ValueError("page_index 错误")
    next_page_index_bs = buf.read(BYTES_PAGE_INDEX)
    next_page_index = int.from_bytes(bytes=next_page_index_bs, byteorder='big', signed=True)
    num_bs = buf.read(BYTES_LEN_TABLES)
    num = int.from_bytes(bytes=num_bs, byteorder='big')
    tables = [new_table_from_bytes(buf) for _ in range(num)]
    page = DatabasePage(pager, page_index, next_page_index)
    page.tables = tables
    return page


class Database:

    def __init__(self, pager: Pager, head: DatabasePage, tail: DatabasePage):
        self.pager: Pager = pager
        self.head: DatabasePage = head
        self.tail: DatabasePage = tail
        self.tables: dict[str, Table] = {}


def new_database(pager: Pager) -> Database:
    if pager.is_new:
        head = new_database_page(pager)
        tail = new_database_page(pager)
        pager.set_table_head(head.page_index)
        pager.set_table_tail(tail.page_index, 0)
        database = Database(pager, head, tail)
    else:
        head = new_database_page_from_page(pager, pager.table_head_page_index)
        tail = new_database_page_from_page(pager, pager.table_tail_page_index)

        tables = {}
        node = head
        while True:
            tables.update({table.name.content: table for table in node.tables})
            if node.page_index == tail.page_index:
                break
            node = new_database_page_from_page(pager, node.next_page_index)

        database = Database(pager, head, tail)
        database.tables = tables
    return database