from __future__ import annotations

import random
import sys

import loguru

from informatics.stree_k_index import update_node, load, get_value

M = 10**9
sys.setrecursionlimit(10**6)


def generate_init_array():
    upper = random.randint(1, 10)
    len_ = random.randint(1, 10**5)
    return [random.randint(0, upper) for _ in range(len_)]


def generate_next_turn(a: list[int]):
    i = random.choice(["u", "s"])
    if i == "u":
        return ["u", random.randint(1, len(a)), random.randint(0, 2)]
    else:
        return ["s", random.randint(1, len(a))]


def b_get_value(a: list[int], val: int):
    ans = 0
    for i, x in enumerate(a):
        ans += x == 0
        if ans == val:
            return i + 1
    else:
        return -1


t = int(input())

for t in range(t):
    a = generate_init_array()
    res = load(a)
    for i in range(random.randint(1, 3000)):
        c = generate_next_turn(a)
        if c[0] == "u":
            a[int(c[1]) - 1] = int(c[2])
            update_node(res=res, i=int(c[1]) - 1, val=int(c[2]))
        else:
            ans = get_value(res=res, val=int(c[1]))
            if ans != b_get_value(a, int(c[1])):
                loguru.logger.error(
                    f"error at got {ans} expected, {b_get_value(a, int(c[1]))}, array: {a}, query: {c}"
                )
# res=
# for i in range(t):
#     c = input().split()
#     if c[0] == "u":
#         update_node(i=int(c[1]) - 1, val=int(c[2]), res=res)
#     else:
#         ans.append(get_value(res=res, val=int(c[1])))
#
# print(*ans)
