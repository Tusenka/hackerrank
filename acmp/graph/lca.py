from __future__ import annotations

import dataclasses
from cmath import log


@dataclasses.dataclass
class Node:
    p: Node | None
    values: dict[int, tuple[int, Node]] = dataclasses.field(default_factory=dict)
    level: int = 0
    children: list[Node] = dataclasses.field(default_factory=list)


def prepare(node: Node):
    node.values = {}
    node.level = node.p.level + 1
    x = node
    j = 1

    while x != x.p:
        x = jump(x.p, j - 1)
        node.values[j] = (x.level, x)
        j <<= 1

    for child in node.children:
        prepare(child)


def jump(node, j):
    if j == 0:
        return node

    if j == 1:
        return node.p

    jj = int(log(j, 2).real)

    if jj == j:
        return node.values[jj]

    return jump(node.values[jj], j - jj)


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
arr = [Node(p=None) for i in range(n)]
root = 0

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
