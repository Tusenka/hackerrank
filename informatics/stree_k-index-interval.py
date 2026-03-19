from __future__ import annotations

import dataclasses
import sys

# https://informatics.mccme.ru/mod/statements/view.php?id=51325&chapterid=3324#1

M = 10**9
sys.setrecursionlimit(10**6)


def load(a: list, i=0, begin=0, end=-1, result: list[int] | None = None):
    n = (len(a)) * 4
    end = len(a) - 1 if end == -1 else end
    if result is None:
        result = [-1] * n

    if begin == end:
        result[i] = 1 if a[begin] == 0 else 0
        return result

    l = i * 2 + 1
    r = i * 2 + 2
    m = (begin + end) // 2
    load(a, l, begin, m, result=result)
    load(a, r, m + 1, end, result=result)

    result[i] = result[l] + result[r]

    if i == 0:
        return result

    return None


def update_node(res: list[int], i: int, val, idx: int = 0, begin=0, end=-1):
    end = len(res) // 4 - 1 if end == -1 else end
    if begin == end:
        res[idx] = 1 if val == 0 else 0
        return

    m = (begin + end) // 2
    if i <= m:
        update_node(res, i, val, idx * 2 + 1, begin, m)
    else:
        update_node(res, i, val, idx * 2 + 2, m + 1, end)

    res[idx] = res[idx * 2 + 1] + res[idx * 2 + 2]


def _get_value(res: list[int], val, idx: int, begin, end):
    if begin == end:
        return begin + 1

    if res[idx] < val:
        return -1

    m = (begin + end) // 2
    if res[idx * 2 + 1] >= val:
        return _get_value(res, val, idx * 2 + 1, begin, m)
    else:
        return _get_value(res, val - res[idx * 2 + 1], idx * 2 + 2, m + 1, end)


def get_value(res: list[int], val, begin, end):
    val = (
        val
        + _get_value_count(res=res, i=begin - 1, idx=0, begin=0, end=len(res) // 4 - 1)
        if begin > 0
        else val
    )

    if val <= 0:
        return -1

    ans = _get_value(res, val, idx=0, begin=0, end=(len(res) // 4 - 1))

    return ans if begin <= ans - 1 <= end else -1


def _get_value_count(res: list[int], i, idx, begin, end):
    if begin > i:
        return 0

    if end <= i:
        return res[idx]

    m = (begin + end) // 2

    return _get_value_count(res, i, idx * 2 + 1, begin, m) + _get_value_count(
        res, i, idx * 2 + 2, m + 1, end
    )


_ = input().strip()

res = load(list(map(int, input().split())))

t = int(input())
ans = []

for i in range(t):
    c = input().split()
    if c[0] == "u":
        update_node(i=int(c[1]) - 1, val=int(c[2]), res=res)
    else:
        ans.append(
            get_value(res=res, val=int(c[3]), begin=int(c[1]) - 1, end=int(c[2]) - 1)
        )

print(*ans)
