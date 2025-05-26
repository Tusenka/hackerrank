import sys
from functools import cache

M = 10 ** 9 + 7
indexes={}
def _build_cubes(n: int):
    _cubes = {}
    i = 1
    while i * i * i <= n:
        _cubes[i * i * i] = i
        i += 1
    return _cubes


def _add_index(indexes: dict, i: int, count: int = 1):
    if i in indexes:
        indexes[i] += count
    else:
        indexes[i] = count


def _remove_index(indexes: dict, i, count: int = 1):
    indexes[i] -= count
    if indexes[i] == 0:
        indexes.pop(i)

@cache
def _try_cubes(i: int, n: int):
    global indexes
    if indexes is None:
        indexes = {}
    if sum(indexes.values()) > 8:
            return False
    if sum(indexes.values()) == 8:
        return n == 0
    if n == 0:
        return True
    if n < 0:
        return False
    if i == 0:
        return False
    sum(indexes.values())
    x = i * i * i
    k = min(8 - sum(indexes.values()), n // x)
    _add_index(indexes, i, k)
    result = _try_cubes(i - 1, n - x * k)
    if result:
        return True
    while k > 0:
        k -= 1
        _remove_index(indexes, i, 1)
        result = _try_cubes(i - 1, n - x * k)
        if result:
            return True
    return False


def build_cubes(N: int):
    global indexes
    possible = _try_cubes(int(N ** (1 / 3)), N)
    result = []
    for x in indexes:
        for i in range(indexes[x]):
            result.append(x)
    result.sort(reverse=True)
    return "IMPOSSIBLE" if not possible else " ".join([str(i) for i in result])

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    n = int(input().rstrip())
    print(build_cubes(n))
