from __future__ import annotations
import dataclasses
from functools import cache

# https://informatics.mccme.ru/mod/statements/view.php?id=51325&chapterid=3321#1

M = 10**9


@dataclasses.dataclass
class TreeNode:
    left_child: TreeNode | None = None
    right_child: TreeNode | None = None
    null_count: int | None = 0
    range: tuple[int, int] | None = None
    is_leaf = False

    def load(self, a: list, i=0, j=-1):
        if j == -1:
            j = len(a) - 1

        self.range = (i, j)
        if i == j:
            self.is_leaf = True
            self.null_count = int(a[i] == 0)
            return

        self.left_child = TreeNode()
        self.right_child = TreeNode()

        self.left_child.load(a=a, i=i, j=(i + j) // 2)
        self.right_child.load(a=a, i=(i + j) // 2 + 1, j=j)

        self.null_count = self.left_child.null_count + self.right_child.null_count

    def find_null_count(self, l: int, r: int):
        if not self._in_range(l, r):
            return 0

        if self.is_leaf:
            return self.null_count

        if self.range[0] == l and self.range[1] == r:
            return self.null_count

        if self.left_child._in_range(l, r) and self.right_child._in_range(l, r):
            return self.left_child.find_null_count(
                l, r
            ) + self.right_child.find_null_count(l, r)

        if self.left_child._in_range(l, r):
            return self.left_child.find_null_count(l, r)

        if self.right_child._in_range(l, r):
            return self.right_child.find_null_count(l, r)

        return None

    def change_value(self, i: int, val: int):
        if self.is_leaf:
            ans = self.null_count != int(val == -1)
            self.null_count = int(val == 0)
            return ans

        if self.left_child._in_range_i(i):
            changed = self.left_child.change_value(i=i, val=val)
        else:
            changed = self.right_child.change_value(i=i, val=val)

        if changed:
            self.null_count = self.left_child.null_count + self.right_child.null_count

    def _in_range(self, i, j):
        return (
            self.range[0] <= i <= self.range[1] or self.range[0] <= j <= self.range[1]
        )

    def _in_range_i(self, i: int):
        return self.range[0] <= i <= self.range[1]


n = tuple(map(int, input().split()))
stree = TreeNode()
stree.load(list(map(int, input().split())))

t = int(input())
ans = []

for i in range(t):
    o = input().split()
    if o[0] == "u":
        stree.change_value(i=int(o[1]) - 1, val=int(o[2]))
    else:
        ans.append(stree.find_null_count(l=int(o[1]) - 1, r=int(o[2]) - 1))

print(*ans)
