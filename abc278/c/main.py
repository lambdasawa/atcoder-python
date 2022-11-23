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
    [N, Q] = read_space_separated_ints()
    TAB = [read_space_separated_ints() for i in range(Q)]

    follow = {}

    for [t, a, b] in TAB:
        if t == 1:  # follow
            follow[a, b] = True
        if t == 2:  # remove
            follow.pop((a, b), None)
        if t == 3:  # query
            if follow.get((a, b), False) and follow.get((b, a), False):
                print("Yes")
            else:
                print("No")
        else:
            pass


if __name__ == "__main__":
    main()
