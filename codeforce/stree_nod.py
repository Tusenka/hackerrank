from __future__ import annotations
import dataclasses
from functools import cache
import sys
# https://informatics.mccme.ru/mod/statements/view.php?id=51325&chapterid=3321#1

M = 10**9
sys.setrecursionlimit(10**6)


def gcd(val1: int, val2: int):
    if val1 < val2:
        val1, val2 = val2, val1

    while val2 >= 1:
        val2, val1 = val1 % val2, val2

    return val1


@dataclasses.dataclass
class TreeNode:
    left_child: TreeNode | None = None
    right_child: TreeNode | None = None
    gcd_value: int | None = 0
    range: tuple[int, int] | None = None

    def load(self, a: list, i=0, j=-1):
        if j == -1:
            j = len(a) - 1

        self.range = (i, j)
        if i == j:
            self.gcd_value = a[i]
            return
        self.left_child = TreeNode()
        self.right_child = TreeNode()

        self.left_child.load(a=a, i=i, j=(i + j) // 2)
        self.right_child.load(a=a, i=(i + j) // 2 + 1, j=j)
        self.gcd_value = gcd(self.left_child.gcd_value, self.right_child.gcd_value)

    def find_gcd(self, l: int, r: int):
        if self.range[0] > r or self.range[1] < l:
            return 0

        if self.range[0] >= l and self.range[1] <= r:
            return self.gcd_value

        return gcd(self.left_child.find_gcd(l, r), self.right_child.find_gcd(l, r))

    def change_value(self, i: int, val: int):
        if self.range[0] == self.range[1]:
            if self._in_range_i(i):
                self.gcd_value = val
            return

        if self.left_child._in_range_i(i):
            self.left_child.change_value(i=i, val=val)
        else:
            self.right_child.change_value(i=i, val=val)

        self.gcd_value = gcd(self.left_child.gcd_value, self.right_child.gcd_value)

    def _in_range_i(self, i: int):
        return self.range[0] <= i <= self.range[1]


_ = input().strip()
stree = TreeNode()
stree.load(list(map(int, input().split())))

t = int(input())
ans = []

for i in range(t):
    c = input().split()
    if c[0] == "u":
        stree.change_value(i=int(c[1]) - 1, val=int(c[2]))
    else:
        ans.append(stree.find_gcd(l=int(c[1]) - 1, r=int(c[2]) - 1))

print(*ans)
