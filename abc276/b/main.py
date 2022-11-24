# https://docs.python.org/ja/3/library/
# https://docs.python.org/ja/3/library/stdtypes.html#string-methods
# https://docs.python.org/ja/3/library/stdtypes.html#lists
# https://docs.python.org/ja/3/library/stdtypes.html#set
# https://docs.python.org/ja/3/library/stdtypes.html#dict

from pprint import PrettyPrinter

# https://docs.python.org/ja/3/library/itertools.html
from itertools import count, cycle, repeat, takewhile, dropwhile, groupby, product, permutations, combinations

# https://docs.python.org/ja/3/library/functools.html
from functools import lru_cache, reduce

# https://docs.python.org/ja/3/library/collections.html
from collections import Counter, namedtuple, deque

# https://docs.python.org/ja/3/library/heapq.html
from heapq import heapify, heappop, heappush

# https://docs.python.org/ja/3/library/math.html
from math import factorial

# https://docs.python.org/ja/3/library/re.html
import re

import sys

pp = PrettyPrinter(indent=2)
sys.setrecursionlimit(1000000)


def read_int():
    return int(input())


def read_space_separated_ints():
    return [int(x) for x in input().split()]


def read_int_table(length):
    return [read_space_separated_ints() for x in range(length)]


def main():
    [N, M] = read_space_separated_ints()
    AB = read_int_table(M)

    result = []

    for i in range(N):
        l = []
        heapify(l)
        result.append(l)

    for A, B in AB:
        a = result[A-1]
        heappush(a, B)
        result[A-1] = a

        b = result[B-1]
        heappush(b, A)
        result[B-1] = b

    for cities in result:
        l = [len(cities)]
        for _ in range(l[0]):
            l.append(heappop(cities))
        print(*l)


if __name__ == "__main__":
    main()
