# https://codeforces.com/problemset/problem/1948/C
import heapq
from collections import deque
from typing import Generator

D = 20000
M = 10**9 + 7


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


def _bfs(a: list):
    visited = [[False for _ in range(len(a[0]))] for _ in range(2)]
    visited[0][0] = True
    queue = [(0, 0)]

    while queue:
        i, j = queue.pop(0)
        for step in _steps(a=a, i=i, j=j):
            if not visited[step[0]][step[1]]:
                print((i, j), "->", step)
                visited[step[0]][step[1]] = True
                queue.append(step)
            else:
                pass
                print("skip", (i, j), "->", step)
    return visited


def _solve(a: list):
    return "YES" if _bfs(a)[1][-1] else "NO"


if __name__ == "__main__":
    t = int(input().rstrip())

    for _ in range(t):
        a = [[0] for _ in range(2)]
        _ = input()
        a[0] = list(1 if x == ">" else -1 for x in input().rstrip())
        a[1] = list(1 if x == ">" else -1 for x in input().rstrip())
        print(_solve(a))
