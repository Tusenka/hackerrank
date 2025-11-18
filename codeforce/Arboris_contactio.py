# https://codeforces.com/contest/2131/problem/D
from __future__ import annotations

import dataclasses


def lca_tree(root: Node) -> tuple[list[int], list[Node]]:
    h = []

    def bfs():
        a = []
        h = []


@dataclasses.dataclass
class Node:
    p: Node | None
    val: int = 0
    children: list[Node] = dataclasses.field(default_factory=list)


def solve(node1, node2, _max_level: int = -1):
    level1 = node1.level
    level2 = node2.level

    if node1 is node2:
        return node1

    if level1 > level2:
        node1 = jump(node1, level2 - level1)
    elif level1 < level2:
        node2 = jump(node2, level2 - level1)

    if _max_level == -1:
        _max_level = max(node1.values.keys())

    while node1.values[_max_level] is node2.values[_max_level]:
        _max_level >>= 1

    if _max_level == x:
        return node1.values[_max_level]

    if _max_level == 2:
        return node1.values[_max_level * 2]

    return solve(node1.values[_max_level], node2.values[_max_level], _max_level)


n = int(input().rstrip())

for i, x in enumerate(int(x) for x in input().rstrip().split()):
    if x == -1:
        root = i
        arr[i].p = arr[i]

    else:
        arr[i].p = arr[x]
        arr[x].children.append(arr[i])

prepare(arr[root])

i, j = tuple(int(x) for x in input().rstrip().split())

print(arr[root])
print(solve(arr[i], arr[j]))
