"""
- https://xiaoxing.us/2018/04/15/singleton-in-python/
"""

import functools
import threading

lock = threading.Lock()


def synchronized(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        with lock:
            return f(*args, **kwargs)
    return synchronized


class Singleton(object):
    _instance = None

    @synchronized(lock)
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance


def main():
    instanceA = Singleton()
    instanceB = Singleton()
    assert id(instanceA) == id(instanceB)


if __name__ == "__main__":
    main()
