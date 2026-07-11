# https://codeforces.com/contest/2166/problem/B


def solve(a: int, b: int, n: int):
    # a/m>=b=> a>=b*m=> m<=a/b=>m0=a//b
    if n - a // b > 0 and b < a:
        return 2
    return 1


t = int(input())

for _ in range(t):
    a, b, n = tuple(map(int, input().split()))
    print(solve(a, b, n))
