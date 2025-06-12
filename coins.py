from functools import cache

M = 10 ** 9 + 7


def _build_coins(a: tuple, i: int):
    if len(a)==0:
        yield 0, 0
        return
    if i == len(a) - 1:
        yield 0, 0
        yield a[-1], 1
        yield a[-1] * 2, 2
        return
    for x in _build_coins(a, i + 1):
        yield x[0], x[1]
        yield x[0] + a[i], x[1] + 1
        yield x[0] + 2 * a[i], x[1] + 2


def coins(a: list, r: int):
    if sum(a) * 2 < r:
        return -1
    m1 = list(_build_coins(a[:len(a) // 2], 0))
    m2 = list(_build_coins(a[len(a) // 2:], 0))
    m1.sort()
    m2.sort(key=lambda x: (x[0], -x[1]) )
    imin = M
    j = len(m2)-1
    for i in m1:
        while m2[j][0] + i[0] > r and j>=1:
            j-=1
        if m2[j][0] + i[0] == r and imin > m2[j][1] + i[1]:
            imin = m2[j][1] + i[1]
    return imin if imin < M else 0


if __name__ == '__main__':
    (r, n) = tuple([int(x) for x in input().rstrip().split()])
    a = list([int(x) for x in input().rstrip().split()])
    print(coins(a, r))
