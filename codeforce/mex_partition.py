# https://codeforces.com/contest/2160/problem/A


def solve(a: list):
    a.sort()
    if a[0] == 0:
        for i in range(1, len(a)):
            if a[i] > a[i - 1] + 1:
                return a[i - 1] + 1
        return a[-1] + 1
    return a[0] - 1


t = int(input())

for _ in range(t):
    _ = input()
    a = list(map(int, input().split()))
    print(solve(a))
