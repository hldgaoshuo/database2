from io import BufferedRandom


def file_open(filename: str) -> tuple[BufferedRandom, bool]:
    try:
        f = open(filename, 'rb+')
        is_new = False
    except FileNotFoundError:
        f = open(filename, 'wb+')
        is_new = True
    return f, is_new


def file_read(file: BufferedRandom, offset: int, length: int) -> bytes:
    file.seek(offset)
    return file.read(length)


def file_update(file: BufferedRandom, offset: int, data: bytes):
    file.seek(offset)
    file.write(data)
    file.flush()
