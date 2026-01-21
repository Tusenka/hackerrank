from __future__ import annotations

import dataclasses
import sys

# https://informatics.mccme.ru/mod/statements/view.php?id=51325&chapterid=3327#1

M = 10**9
sys.setrecursionlimit(10**6)


def load(a: list, i=0, begin=0, end=-1, result: list[list[int]] | None = None) -> list[list[int]]:
    n = (len(a)) * 4
    end = len(a) - 1 if end == -1 else end

    if result is None:
        result = [[0, 0] for _ in range(n)]

    if begin == end:
        result[i] = [a[begin],0]
        return result

    l = i * 2 + 1
    r = i * 2 + 2
    m = (begin + end) // 2
    load(a, l, begin, m, result=result)
    load(a, r, m + 1, end, result=result)

    result[i]=[max(result[l][0],result[r][0]), 0]

    if i == 0:
        return result

    return None


def update_nodes(res: list[list[int]], l: int, r: int, val, idx=0, begin=0, end=-1):
    end = len(res) // 4 - 1 if end == -1 else end

    if begin>r or end<l:
        return res[idx][0]+res[idx][1]

    if begin==end:
       res[idx][1] = res[idx][1]+val
       return res[idx][0]+res[idx][1]

    if begin == l and r==end:
        res[idx][1] = res[idx][1]+val
        return res[idx][0]+res[idx][1]

    m = (begin + end) // 2

    lvalue=update_nodes(res=res, l=l, r=min(m, r), val=val, idx=idx * 2 + 1, begin=begin, end=m)
    rvalue=update_nodes(res=res, l=max(m+1, l), r=r, val=val, idx=idx * 2 + 2, begin=m + 1, end=end)

    res[idx][0]=max(lvalue, rvalue)

    return res[idx][0]+res[idx][1]


def push(res: list[list[int]], idx: int):
    res[idx*2+1][1] += res[idx][1]
    res[idx*2+2][1] += res[idx][1]

    res[idx][1]=0


def _get_value(res: list[list[int]],l: int, r: int, idx: int, begin:int, end:int):
    if begin>r or end<l:
        return -1

    if begin==end:
        return res[idx][0]+res[idx][1]

    if begin == l and r==end:
        return res[idx][0]+res[idx][1]

    if res[idx][1]!=0:
       push(res=res, idx=idx)

    m = (begin + end) // 2
    return max(_get_value(res=res, l=l, r=r, idx=idx * 2 + 1, begin=begin, end=m), _get_value(res, l,r, idx * 2 + 2, m + 1, end))


def get_value(res: list[list[int]], l:int, r:int):
    return _get_value(res=res, l=l, r=r, idx=0, begin=0, end=len(res) // 4 - 1)


_ = input().strip()

res = load(list(map(int, input().split())))

t = int(input())
ans = []

for i in range(t):
    c = input().split()
    if c[0] == "a":
        update_nodes(l=int(c[1]) - 1, r=int(c[2])-1, val=int(c[3]), res=res)
    else:
        ans.append(
            get_value(res=res, l=int(c[1]) - 1, r=int(c[2]) - 1)
        )

print(*ans)
