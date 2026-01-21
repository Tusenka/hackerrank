def solve(a: list):
    _max = max(a)
    _sum = 0
    return _max * len(a)


t = int(input())

for _ in range(t):
    n = int(input())

    a = list(map(int, input().split()))
    print(solve(a))
