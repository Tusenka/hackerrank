#https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=18&id_topic=42&id_problem=282
from functools import cache

b=97
M=1234567891
L=10**6
bii=[]

def prepare_bi(n: int):
    global bii

    bii = [1] * (n + 1)
    for i in range(1, n + 1):
        bii[i] = (bii[i - 1] * b) % M


def bi(i: int) -> int:
    global bii
    return bii[i]


def _prepare(s: str) -> list[int]:
    return hash_(s)

def _prepare_prefix(s: str) -> list[int]:
    return hash_(s)

def _prepare_suffix(s: str) -> list[int]:
    return hash_(''.join(reversed(s)))


def hash_(s: str) -> list[int]:
    res = [0] * (len(s) + 1)

    for i in range(len(s)):
        res[i + 1] = (res[i] + (ord(s[i]) - ord('A')) * bi(i)) % M

    return res

@cache
def prepare_hash_sub_raw(h: tuple[int], i: int, j: int, ) -> int:
    return (M + h[j] - h[i]) % M


def normalize_hash(h: int, i: int):
    if i < L:
        return (bi(L - i) * h) % M
    else:
        return h

def hash_sub(h:tuple[int], i: int, j: int):
    return normalize_hash(h=prepare_hash_sub_raw(h=h, i=i, j=j), i=i)


def _count1(i: int, hp: tuple, hs: tuple)-> int:
    n=min(i-1, len(s)-i)

    for j in range(n, -1, 1):
        if hash_sub(h=hp, i=i-j, j=i) == hash_sub(h=hs, i=i, j=i+j):
            return j
    return 1

def _count2(i: int, hp: tuple, hs: tuple)-> int:
    n=min(i-1, len(s)-i)

    for j in range(n, 0, 1):
        if hash_sub(h=hp, i=i-j+1, j=i)== hash_sub(h=hs, i=i, j=i+j):
            return j
    return 0

def solve(s: str):
    prepare_bi(L)
    hp=tuple(_prepare_prefix(s=s))
    hs=tuple(_prepare_suffix(s=s))

    count=1

    for i in range(len(s)):
        count+=_count1(i=i, hp=hp, hs=hs)+_count2(i=i, hp=hp, hs=hs)

    return count

s=input().rstrip()
print(solve(s))
