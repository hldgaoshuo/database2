from io import BufferedRandom


def file_open(filename: str) -> BufferedRandom:
    f = open(filename, 'wb+')
    return f
