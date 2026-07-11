# https://codeforces.com/contest/2137/problem/A?locale=en
def solve(x: int, k: int) -> int:
    return x * (2 ** (k))


t = int(input().rstrip())

for _ in range(t):
    k, x = list(map(int, input().rstrip().split()))
    print(solve(x, k))
