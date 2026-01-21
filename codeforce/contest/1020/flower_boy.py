# https://codeforces.com/contest/2106/problem/D


def _check_beauty(a: list, b: list) -> bool:
    j = 0
    for x in a:
        if x >= b[j]:
            j += 1
        if j > len(b) - 1:
            return True

    return False


def solve(m: int, a: list[int], b: list[int]) -> int:  # sourcery skip: use-next
    b_maxes = sorted([(b[i], i) for i in range(len(b))], reverse=False)

    if _check_beauty(a=a, b=b):
        return 0

    for x, k in b_maxes:
        if _check_beauty(a=a, b=b[:k] + b[k + 1 :]):
            return x

    return -1
    # return next(
    #     (
    #         b[k] + 1
    #         for _, k in b_maxes
    #         if _check_beauty(a=a, b=b[:k] + b[k + 1 :])
    #     ),1
    #     -1,
    # )


t = int(input())
ans = []
for _ in range(t):
    n, m = tuple(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans += [solve(m, a, b)]

for x in ans:
    print(x)
