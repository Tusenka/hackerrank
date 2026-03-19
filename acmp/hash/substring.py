from functools import cache

M = 12324567891
b = 29
bi = []


def prepare_bi(n: int):
    global bi

    bi = [1] * (n + 1)
    for i in range(1, n + 1):
        bi[i] = (bi[i - 1] * b) % M


def _prepare(s: str) -> list[int]:
    return hash(s)


def hash(s: str) -> list[int]:
    res = [0] * (len(s) + 1)

    for i in range(len(s)):
        res[i + 1] = (res[i] + (ord(s[i]) - ord("a")) * bi[i]) % M

    return res


def hash_sub(i: int, j: int, h: list[int]):
    return (M + h[j] - h[i]) % M


def normalize_hash(h: int, j: int):
    return (bi[j] * h) % M


def solve(s, t):
    prepare_bi(max(len(s), len(t)))
    hs = _prepare(s)
    ht = _prepare(t)[-1]
    res = []

    for i in range(len(s) - len(t) + 1):
        if hash_sub(i, i + len(t), hs) == normalize_hash(h=ht, j=i):
            res.append(i)

    return res


s = input()
t = input()

print(*solve(s, t))
