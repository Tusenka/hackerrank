# https://codeforces.com/contest/2148/problem/B
def solve(m, n, x, y) -> int:
    return m + n


t = int(input().rstrip())

for _ in range(t):
    m, n, x, y = tuple(map(int, input().rstrip().split()))
    _ = input()
    _ = input()

    print(solve(m, n, x, y))
