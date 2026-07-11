# https://codeforces.com/contest/2128/problem/A


def get_middle(a: list, c: int, visited, m=1):
    for i, x in enumerate(a):
        if visited[max(i - 1, 0)]:
            continue
        if x * m > c:
            return max(i - 1, 0)
    for i in range(len(a) - 1, -1, -1):
        if not visited[i]:
            return i
    raise ArithmeticError()


def solve(a: list, c: int):
    a.sort()
    visited = [False] * len(a)
    _cost = 0
    m = 1

    while m < 2 ** len(a):
        i = get_middle(a, c, visited, m)
        _cost += int(a[i] * m > c)
        visited[i] = True
        m = m << 1

    return _cost


t = int(input())

for i in range(t):
    n, c = tuple(int(x) for x in input().rstrip().split())
    a = list(int(x) for x in input().rstrip().split())
    print(solve(a, c))
