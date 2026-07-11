vals = []


def _prepare(N: int = 20):
    global vals
    vals = [i * i for i in range(1, N + 1)]


def solve(n: int):
    global vals

    return vals[:n]


t = int(input())
_prepare(N=20)

for _ in range(t):
    n = int(input())
    print(*solve(n))
