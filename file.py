import os


def file_open(path: str) -> int:
    fd = os.open(path, os.O_RDWR | os.O_CREAT | os.O_BINARY)
    return fd


def file_read(fd: int, offset: int, length: int) -> bytes:
    os.lseek(fd, offset, os.SEEK_SET)
    bs = os.read(fd, length)
    return bs


def file_update(fd: int, offset: int, data: bytes) -> None:
    os.lseek(fd, offset, os.SEEK_SET)
    os.write(fd, data)
    os.fsync(fd)
