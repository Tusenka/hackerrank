from collections import defaultdict


def solve(a: list):
    vals = [0] * (len(a) + 1)
    for x in a:
        vals[x] += 1

    if not vals[0]:
        return False

    if vals[1] == 1:
        return True

    if max(a) == 1:
        return False

    if not vals[1]:
        return False

    return True


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print("YES" if solve(a) else "NO")
