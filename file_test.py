from file import file_open


def test_file_open():
    f = file_open('test.txt')
    f_size = f.tell()
    print(f"新建文件大小: ({f_size})")
