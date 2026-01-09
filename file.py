from io import BufferedRandom


def file_open(filename: str) -> BufferedRandom:
    f = open(filename, 'wb+')
    return f


def file_read(file: BufferedRandom, offset: int, length: int) -> bytes:
    file.seek(offset)
    return file.read(length)


def file_update(file: BufferedRandom, offset: int, data: bytes):
    file.seek(offset)
    file.write(data)
    file.flush()
