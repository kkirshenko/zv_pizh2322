from typing import Callable

class HashFunction:
    def __init__(self, fn: Callable[[str], int], name: str = None):
        self.fn = fn
        self.name = name or fn.__name__

    def __call__(self, key: str) -> int:
        return self.fn(key)

# Простейшая хеш-функция: сумма ASCII-кодов всех символов строки
def sum_hash(key: str) -> int:
    s = 0
    for ch in key:
        s += ord(ch)
    return s

# Полиномиальный хеш (хеш с основанием base, часто используется в rolling hash)
def poly_hash(key: str, base: int = 257) -> int:
    h = 0
    for ch in key:
        h = h * base + ord(ch)
    return h

# Классическая хеш-функция DJB2 от Daniel J. Bernstein
def djb2_hash(key: str) -> int:
    h = 5381
    for ch in key:
        h = ((h << 5) + h) + ord(ch)  # эквивалентно h * 33 + ord(ch)
    return h & 0xFFFFFFFFFFFFFFFF