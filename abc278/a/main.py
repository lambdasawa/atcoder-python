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
    [N, K] = read_space_separated_ints()
    A = input().split(" ")
    answer = A[K:] + ["0"] * min(K, N)
    print(" ".join(answer))


if __name__ == "__main__":
    main()
