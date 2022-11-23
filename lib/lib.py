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


# slice,
l = [n for n in range(10)]
assert l == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert l[2:5] == [2, 3, 4]
assert l[99:] == []
assert l[:99] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# get or else
l = [n for n in range(5)]
assert (l[1] if 1 < len(l) else None) == 1
assert (l[9] if 9 < len(l) else None) == None

# max, max by
l = [41, 53, 62]
assert max(l) == 62
assert max(l, key=lambda n: n % 10) == 53

# find element
l = [5, 8, 3]
assert next(n for n in l if n % 2 == 0) == 8

# find index
l = [5, 7, 3]
assert l.index(7) == 1

# count by
l = [n for n in range(5)]
assert sum(1 for _ in l) == 5

# exists, include
l = [n for n in range(5)]
assert (3 in l) == True

# map, filter
l = [n for n in range(5)]
assert [n * 10 for n in l if n % 2 == 0] == [0, 20, 40]

# all, every
l = [n for n in range(5)]
assert all(n <= 10 for n in l) == True

# any, some
l = [n for n in range(5)]
assert any(n > 1 for n in l) == True

# take, take while
l = [n for n in range(5)]
assert l[:2] == [0, 1]
assert list(takewhile(lambda n: n < 3, l)) == [0, 1, 2]

# drop drop while
l = [n for n in range(5)]
assert l[2:] == [2, 3, 4]
assert list(dropwhile(lambda n: n < 3, l)) == [3, 4]

# sort
l = [41, 53, 62]
assert sorted(l, key=lambda x: x % 10, reverse=True) == [53, 62, 41]

# sort (side effect)
l = [41, 53, 62]
l.sort(key=lambda x: x % 10, reverse=True)
assert l == [53, 62, 41]

# zip with index
l = [3, 7, 5]
assert [(i, n) for (i, n) in enumerate(l)] == [(0, 3), (1, 7), (2, 5)]

# concat
l = [n for n in range(3)]
assert (l + l) == [0, 1, 2, 0, 1, 2]

# set check
s = set(range(3))
assert (1 in s) == True
assert (10 in s) == False

# set add
s = set(range(3))
s.add(10)
assert s == {0, 1, 2, 10}

# set remove, delete
s = set(range(3))
s.remove(1)
s.discard(9)
assert s == {0, 2}

# dict get or else
d = {1: 10, 2: 20, 3: 30}
assert d[1] == 10
assert d.get(9, None) == None

# dict include key
d = {1: 10, 2: 20, 3: 30}
assert (1 in d) == True

# dict add
d = {1: 10, 2: 20, 3: 30}
d[9] = 90
assert d == {1: 10, 2: 20, 3: 30, 9: 90}

# dict delete, remove
d = {1: 10, 2: 20, 3: 30}
del d[1]
d.pop(9, None)
assert d == {2: 20, 3: 30}

# permutations
expected = list(permutations(range(3), 2))
actual = [
    (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1),
]
assert expected == actual

# permutation count
l = [n for n in range(5)]
n = len(l)
r = 3
actual = factorial(n) / factorial(n - r)
expected = len(list(permutations(l, r)))
assert actual == expected

# combinations
expected = list(combinations(range(3), 2))
actual = [(0, 1), (0, 2), (1, 2)]
assert expected == actual

# combinations count
l = [n for n in range(5)]
n = len(l)
r = 3
actual = factorial(n) / (factorial(r) * factorial(n - r))
expected = len(list(combinations(l, r)))
assert actual == expected

# queue
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
assert queue.popleft() == 1

# stack
stack = deque([])
stack.append(1)
stack.append(2)
stack.append(3)
assert stack.pop() == 3

# priority queue
queue = []
heapify(queue)
heappush(queue, 7)
heappush(queue, 3)
heappush(queue, 5)
assert heappop(queue) == 3
assert queue == [5, 7]


@ lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


# memoize
assert fib(100) == 354224848179261915075
