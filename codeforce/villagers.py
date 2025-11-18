# https://codeforces.com/contest/2133/problem/B?locale=en
def _get_p(p: list, i):
    if p[i] == -1:
        return i
    else:
        p[i] = _get_p(p, p[i])

    return p[i]


def solve(a):
    n = len(a)
    cost = 0
    a.sort(reverse=True)
    for i in range(0, n, 2):
        cost += a[i]
    return cost


t = int(input().rstrip())

for _ in range(t):
    n = int(input().rstrip())
    a = list(map(int, input().rstrip().split()))
    print(solve(a))
