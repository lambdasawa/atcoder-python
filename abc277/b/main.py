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

pp = PrettyPrinter(indent=2)


def read_int():
    return int(input())


def read_space_separated_ints():
    return [int(x) for x in input().split()]


def read_int_table(length):
    return [read_space_separated_ints() for x in range(length)]


def valid(i, s1, S):
    check1 = s1[0] in 'HDCS'
    check2 = s1[1] in "A23456789TJQK"

    check3 = True
    for j, s2 in enumerate(S):
        if i != j and s1 == s2:
            check3 = False
            break

    return check1 and check2 and check3


def main():
    N = read_int()
    S = [input() for _ in range(N)]

    print("Yes" if all(valid(i, s, S) for i, s in enumerate(S)) else "No")


if __name__ == "__main__":
    main()
