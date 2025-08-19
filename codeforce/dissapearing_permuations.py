# https://codeforces.com/problemset/problem/2086/C
import heapq
from collections import deque
from typing import Generator

D = 20000
M = 10 ** 9 + 7


def _steps(a: list, i: int, j: int) -> Generator[tuple[int, int], None, None]:
    n = len(a[0])
    x = int(i == 0)
    if j < n - 1 and a[i][j + 1] > 0:
        yield i, j + 1

    if j > 0 and a[i][j - 1] < 0:
        yield i, j - 1

    if j == n - 2 and i == 1:
        yield i, n - 1

    yield x, j + a[x][j]


def _solve(a: list, a2i: dict, i: int):
    return update(a, a2i, i)


def encode(a: list):
    return dict((a[i], i) for i in range(len(a)))


def update(a, a2i, i):
    j = a2i[i+1]
    if  j<0:
        return 0
    if j == i:
        return 1
    a2i[i+1] = -1
    a[i] = i+1

    return 1 + update(a, a2i, j)


if __name__ == '__main__':
    t = int(input().rstrip())

    for _ in range(t):
        _ = input()
        a = list(int(x) for x in input().rstrip().split())
        p = list(int(x)-1 for x in input().rstrip().split())
        a2i = encode(a)
        last=0
        res=[]
        for x in p:
            last+=_solve(a, a2i, x)
            res.append(last)
        print (*res)