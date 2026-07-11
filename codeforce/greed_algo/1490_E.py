def solve(a: list[int]):
    h = [(a[i], i) for i in range(len(a))]
    h.sort()
    if len(h) == 2:
        if h[-1][0] == h[0][0]:
            return trans(h=h, start=0)
        else:
            return trans(h=h, start=len(h) - 1)

    ps = [0] * len(a)
    ps[0] = h[0][0]
    for i in range(1, len(h)):
        ps[i] = ps[i - 1] + h[i][0]

    _start = 0
    for i in range(len(h) - 2, -1, -1):
        for j in range(i + 1, len(h) - 1):
            if ps[i] < h[j][0]:
                _start = i + 1

    return trans(h=h, start=_start)


def trans(h: list, start):
    return sorted([h[i][1] + 1 for i in range(start, len(h))])


t = int(input())

for _ in range(t):
    input()
    a = list(map(int, input().split()))
    ans = solve(a=a)
    print(len(ans))
    print(*ans)
