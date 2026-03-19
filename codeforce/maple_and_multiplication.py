# https://codeforces.com/contest/2139/problem/A
def solve(a: int, b: int):
    if a < b:
        a, b = b, a

    if a == b:
        return 0

    if a % b == 0:
        return 1

    return 2


t = int(input().rstrip())

for _ in range(t):
    a, b = tuple(map(int, input().rstrip().split()))
    print(solve(a, b))
