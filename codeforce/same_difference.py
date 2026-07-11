# https://codeforces.com/contest/2166/problem/A


def solve(s: list):
    ic = s[-1]
    icount = len([c for c in s if c != ic])

    return icount


t = int(input())
for _ in range(t):
    input()
    s = list(map(lambda x: ord(x) - ord("a"), input().strip()))

    print(solve(s))
