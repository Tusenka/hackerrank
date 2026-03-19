def solve(n: int, w: int):
    if w == 1:
        return 0
    if w > n:
        return n

    if w == n:
        return w - 1

    c = n // w
    rest = n % w
    return c * (w - 1) + rest


t = int(input())

for _ in range(t):
    n, w = tuple(map(int, input().split()))
    print(solve(n=n, w=w))
