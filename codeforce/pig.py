from functools import lru_cache


@lru_cache
def _solve(a: tuple, s: tuple, d: tuple):
    count = 0
    if s[0] == d[0] and s[1] == d[1]:
        return 1
    if s[0] == d[0] - 1 and s[1] == d[1]:
        return 1
    if s[0] == d[0] and s[1] == d[1] - 1:
        return 1
    if s[0] > d[0] or s[1] > d[1]:
        return 0

    for dstep in _dsteps(a, s, d):
        ss, sd = dstep
        count += _solve(a, ss, sd)
    return count


def _dsteps(a: tuple, s: tuple, d: tuple):
    for step in _steps(a, s):
        for rstep in _rsteps(a, d):
            if a[step[0]][step[1]] == a[rstep[0]][rstep[1]]:
                yield step, rstep


def _steps(a, s):
    if s[0] < len(a) - 1:
        yield s[0] + 1, s[1]
    if s[1] < len(a[0]) - 1:
        yield s[0], s[1] + 1


def _rsteps(a, s):
    if s[0] > 0:
        yield s[0] - 1, s[1]
    if s[1] > 0:
        yield s[0], s[1] - 1


n, m = tuple(int(x) for x in input().rstrip().split())
a = []

for _ in range(n):
    a.append(tuple(ord(x) for x in input().rstrip()))
a = tuple(a)

print(_solve(a, (0, 0), (n - 1, m - 1)))
