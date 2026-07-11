def solve(a: list, x: int, s: int):
    _sum = sum(a)
    return _sum <= s and (_sum - s) % x == 0


t = int(input())

for _ in range(t):
    n, s, x = tuple(map(int, input().split()))
    a = list(map(int, input().split()))

    print("YES" if solve(a, x, s) else "NO")
