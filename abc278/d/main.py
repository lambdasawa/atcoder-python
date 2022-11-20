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


def main():
    N = read_n()
    A = read_space_separated_ints()
    Q = read_n()
    base = 0
    changed_indexes = set(range(N))
    for _ in range(Q):
        query = read_space_separated_ints()
        if query[0] == 1:
            base = query[1]
            for i in changed_indexes:
                A[i] = 0
            changed_indexes = set()
        elif query[0] == 2:
            i, x = query[1:]
            A[i-1] += x
            changed_indexes.add(i-1)
        elif query[0] == 3:
            print(base + A[query[1]-1])


if __name__ == "__main__":
    main()
