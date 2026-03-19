# Phoenix and Beauty
# https://codeforces.com/contest/1348/problem/B


t = int(input())


def solve(k: int, a: list):
    s_ = set(a)
    if len(s_) > k:
        return -1
    if len(s_) < k:
        i = max(a) + 1
        for _ in range(k - len(s_)):
            s_.add(i)
            i += 1

    p = list(s_)

    return len(a) * p


for _ in range(t):
    n, k = tuple(map(int, input().split()))
    a = list(map(int, input().split()))

    ans = solve(k, a)
    if ans == -1:
        print(ans)
    else:
        print(len(ans))
        print(*ans)
