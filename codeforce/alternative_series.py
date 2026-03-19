from collections import defaultdict


def solve(a: dict, b: dict, k: int) -> bool:
    for y in b:
        if b[y] == 0:
            continue
        for x in a:
            if (abs(x - y) % k == 0 or abs(x + y) % k == 0) and a[x] > 0:
                a[x] -= 1
                b[y] -= 1
                break
        else:
            return False

    return True


t = int(input().rstrip())

for _ in range(t):
    _, k = tuple(int(x) for x in input().rstrip().split())
    a = defaultdict(int)

    for x in (int(x) for x in input().rstrip().split()):
        a[x] += 1

    b = defaultdict(int)
    for x in (int(x) for x in input().rstrip().split()):
        b[x] += 1
        if a[x] > 0:
            a[x] -= 1
            b[x] -= 1

    print("YES" if solve(a, b, k) else "NO")
