from typing import Any, Callable

M = 12324567891
b = 29
bii = []


def prepare_bi(n: int):
    global bii

    bii = [1] * (n + 1)
    for i in range(1, n + 1):
        bii[i] = (bii[i - 1] * b) % M


def bi(i: int) -> int:
    global bii
    return bii[i]


def _prepare(s: str) -> list[int]:
    return hash(s)


def hash(s: str) -> list[int]:
    res = [0] * (len(s) + 1)

    for i in range(len(s)):
        res[i + 1] = (res[i] + (ord(s[i]) - ord('A')) * bi(i)) % M

    return res


def hash_sub(h: list[int], i: int, j: int,) -> int:
    return (M + h[j] - h[i]) % M


def normalize_hash(h: int, i: int, j: int):
    if i < j:
        return (bi(j - i) * h) % M
    else:
        return h

def get_substr_hashes(l: int, hs: list[int]) -> list[int]:
    j=len(hs)-l
    res=[0]*(j)
    for i in range(j):
        res[i]=normalize_hash(hash_sub(hs, i, i+l), i, j-1)

    return res

def bin_search(r:int, f: Callable[[int], int]) -> tuple[int, int]:
    l=0
    if res:=f(r)>-1:
        return res, r

    while r-l>1:
        m=(r+l)//2
        if f(m)>-1:
            l=m
        else:
            r=m
    return f(l), l



def solve(s: str, t: str):
    prepare_bi(len(s))
    hs = _prepare(s)
    ht = _prepare(t)

    def compare(n: int) -> int:
        if n>len(s):
            return -1

        nhs=get_substr_hashes(l=n, hs=hs)
        nht=set(get_substr_hashes(l=n, hs=ht))

        for i, h1 in enumerate(nhs):
            if h1 in nht:
                return i
        return -1

    res=bin_search(r=min(len(s), len(t))+1, f=compare)

    return s[res[0]:res[0]+res[1]] if res[1]>0 else ''


_ = input()
s = input()
t = input()

print(solve(s, t))
