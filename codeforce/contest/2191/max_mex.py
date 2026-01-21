def _mex(a: list[int]):
    for i in range(1, len(a)):
        if a[i] > a[i - 1] + 1:
            return a[i - 1] + 1

    return a[-1] + 1


def solve(a: list[int]):
    a.sort()
    j = 0
    _count = 1
    for i in range(1, len(a)):
        _count = _count + 1
        if a[i] > a[i - 1] + 1:
            _count += 1
            j = i


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))
