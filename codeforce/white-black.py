# https://codeforces.com/problemset/problem/1676/G
from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class TreeNode:
    color: int
    childs: list[TreeNode] = field(default_factory=list)

    def sum(self):
        if not self.childs:
            return self.color

        return self.color + sum(color.sum() for color in self.childs)

    @staticmethod
    def load(a: tuple, colors: tuple):
        dp = {}
        for i, x in enumerate(a):
            if x in dp:
                node = dp[x]
            else:
                node = TreeNode(color=colors[x])
                dp[x] = node
            if i == x:
                continue
            dp[i] = TreeNode(color=colors[i])
            node.childs.append(dp[i])
        return dp.values()


def solve(a: tuple, colors: tuple):
    dp = TreeNode.load(a, colors)
    return len([1 for x in dp if x.sum() == 0])


def main():
    pass


t = int(input())

for i in range(t):
    n = int(input())
    a = tuple([0] + [int(x) - 1 for x in input().rstrip().split()])
    colors = tuple(1 if x == "W" else -1 for x in input())
    print(solve(a, colors))
