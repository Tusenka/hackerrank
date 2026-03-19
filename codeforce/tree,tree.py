# https://codeforces.com/problemset/problem/2167/F
from __future__ import annotations

import dataclasses
from dataclasses import field


@dataclasses.dataclass
class TreeNode:
    i: int = 0
    parent: TreeNode | None = None
    children: list[TreeNode] = field(default_factory=list)
    size: int = 1

    def iter(self):
        yield self

        for child in self.children:
            for node in child.iter():
                yield node

    @staticmethod
    def from_edges(
        edges: list[tuple[int, int]], i=0, hash=None, parent: TreeNode | None = None
    ) -> TreeNode:
        if hash is None:
            hash = []
        node = TreeNode(i=i, parent=None, size=1, children=[])
        hash.append(i)

        for ich in edges[i]:
            if ich not in hash:
                ch = TreeNode.from_edges(edges, i=ich, hash=hash, parent=node)
                node.children.append(ch)
                node.size += ch.size

        return node

    def remove_root(self, new_root: TreeNode):
        child = None

        for c in self.children:
            if c.i == new_root.i:
                child = c


def solve(edges: list, n: int, k: int):
    ans = 0

    for i in range(n):
        root = TreeNode.from_edges(edges, i)
        ans += len([node.size for node in root.iter() if node.size >= k])

    return ans


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    edges = [set() for _ in range(n)]
    for _ in range(n - 1):
        i, j = map(int, input().split())
        edges[i - 1].add(j - 1)
        edges[j - 1].add(i - 1)

    print(solve(edges=edges, n=n, k=k))
