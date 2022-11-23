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
    QUERY = [read_space_separated_ints() for i in range(Q)]

    changed_indices = set(range(N))

    base = 0

    for query in QUERY:
        if query[0] == 1:  # assign
            for idx in changed_indices:
                A[idx] = 0
            changed_indices.clear()
            base = query[1]
        elif query[0] == 2:  # increment
            idx = query[1]-1
            A[idx] += query[2]
            changed_indices.add(idx)
        elif query[0] == 3:  # log
            idx = query[1]-1
            print(base + A[idx])
        else:
            pass


if __name__ == "__main__":
    main()
