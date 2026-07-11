# https://codeforces.com/contest/2147/problem/A


def solve(x: int, y: int):
    if y > x:
        return 2
    if y == 1:
        return -1
    d = x - y + 1
    if d > y:
        return 3
    return -1


for _ in range(int(input())):
    x, y = map(int, input().rstrip().split())

    print(solve(x, y))
