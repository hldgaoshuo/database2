import threading

__id = 0
__lock = threading.Lock()


def get_oid():
    with __lock:
        oid = __id
        oid += 1
        return oid
