# https://codeforces.com/contest/2143/problem/A
def sign(a):
    return 1 if a > 0 else 0 if a == 0 else -1


def _is_sorted(p: list, sdiff: int) -> bool:
    if len(p) < 2:
        return True
    for i in range(1, len(p)):
        s = sign(p[i] - p[i - 1])
        if s != sdiff:
            return False
    return True


def solve(p: list):
    n = len(p)
    find_maxi = [i for i in range(n) if p[i] == n][0]

    if _is_sorted(p[:find_maxi], 1) and _is_sorted(p[find_maxi + 1 :], -1):
        return True
    else:
        return False


t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    a = list(map(int, input().rstrip().split()))
    print("YES" if solve(a) else "NO")
