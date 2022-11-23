# https://docs.python.org/ja/3/library/
from itertools import count, cycle, repeat, takewhile, dropwhile, groupby, product, permutations, combinations
from functools import lru_cache, reduce
from pprint import PrettyPrinter
from collections import Counter, namedtuple, deque
import math
import re

pp = PrettyPrinter(indent=2)


def read_n():
    return int(input())


def read_space_separated_ints():
    return [int(x) for x in input().split()]


def read_int_table(length):
    return [read_space_separated_ints() for x in range(length)]


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def valid_hm(h, m):
    a = h // 10
    b = h % 10
    c = m // 10
    d = m % 10

    rotate_h = a * 10 + c
    rotate_m = b * 10 + d

    return rotate_h < 24 and rotate_m < 60


def main():
    [h, m] = read_space_separated_ints()

    sec = h*60+m
    while True:
        current_h = (sec // 60) % 24
        current_m = sec % 60

        if current_h < 24 and current_m < 60 and valid_hm(current_h, current_m):
            print(current_h, current_m)
            return

        sec += 1


if __name__ == "__main__":
    main()
