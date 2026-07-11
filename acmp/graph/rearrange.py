# https://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=32&id_topic=55&id_problem=1043
import heapq
import sys

M = 10**9 + 7


def _solve(s: int, a: list):
    dp = {0: 0, 1: 0, 2: 0}
    for x in a:
        dp[x] += 1
    if sum(a) > s:
        return a
    if sum(a) == s:
        return [-1]
    if s - sum(a) == 1:
        res = [0] * dp[0] + dp[1] * [2] + dp[2] * [1]
    else:
        res = [-1]
    return res


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n, s = tuple(int(x) for x in input().rstrip().split())
        a = list(int(x) for x in input().rstrip().split())
        print(*_solve(s, a))
